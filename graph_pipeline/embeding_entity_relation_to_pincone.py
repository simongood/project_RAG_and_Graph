# 將所有 實體限制清單、關係限制清單 內的東西向量化進pinecone
import requests
from pinecone import Pinecone
import uuid

def jina_embedding(text, config):
    '''
    進一個文字 => 出一個 1024 維向量
    '''
    # 環境設定
    url = config['jina_url']
    headers = {
        'Content-Type': 'application/json',
        'Authorization': config['jina_headers_Authorization']
    }

    # data 設定
    data = {
        "model": "jina-embeddings-v3",
        "task": "text-matching",
        "late_chunking": False,
        "dimensions": 1024,
        "embedding_type": "float",
        "input": text
    }

    # 發送請求
    response = requests.post(url, headers=headers, json=data)

    # 回應成功 => 萃取資料
    if response.status_code == 200:
        data = response.json()
        embeddings = data['data'][0]['embedding']   # 向量資料 : 1024 維
        return embeddings
    else:
        print(f"jina 呼叫失敗: {response.status_code}, {response.text}")
        return None

def embedding_to_pinecone(config):
    # 修正實體列表和關係列表的格式
    entity = ['青霉菌', '皮鞋', '黑曲霉', '運動鞋', '毛霉菌', '帆布鞋', '木霉菌', '靴子', '高濕度', '70% 酒精溶液', '白醋稀釋液', '矽膠乾燥劑', '軟毛刷', '綠色絨毛狀附著物', '透氣鞋盒', '專業鞋類清潔服務', '收藏級限量版鞋', '霉變評估服務', '輕度霉變', '皮革修復專家', '結構性損壞', '根霉菌', '白色霉菌', '粉紅霉菌', '灰綠霉菌', '交鏈孢菌', '褐腐菌', '黃褐色變色', '白色粉末狀斑點', '色彩褪變', '黑色霉斑', '材質軟化', '纖維分解', '過敏反應', '呼吸道刺激', '皮膚接觸性過敏', '眼部刺激', '氣喘惡化', '接觸性皮膚炎', '天然皮革', '帆布', '麂皮', '棉質材料', '羊毛毛氈', '霉味', '重度霉變', '全面霉變', '深層霉變', '反復霉變', '定制鞋', '零售商庫存防霉服務', '商業防霉噴霧', '專業除濕服務', '專業恆溫恆濕倉庫', '霉菌檢測實驗室', '熱帶氣候', '密閉鞋櫃', '初期霉變', '內襯發霉', '合成皮革', '縫線處霉變', '橡膠', '表面粗糙', '尼龍網面', 'EVA泡棉', '亞熱帶氣候', '雨季環境', '中度霉變', '溫帶氣候', '中等濕度', '大陸性氣候', '海洋性氣候', '低濕度', '局部霉變', '活性炭吸濕包', '鈣氯乾燥劑', '除濕盒', '防霉鞋袋', '防潮箱', '恆溫恆濕櫃', '環境控制顧問', '室內空調環境', '極重度霉變', '塑料袋封存環境', '開放式鞋架', '冷風吹風機', '地下室環境', '浴室環境', '雨靴', '紙盒包裝環境', '灰色斑點', '鞋墊霉變', '邊緣霉變', '表面霉變', '點狀霉斑', '絲狀霉菌蔓延', 'UV殺菌燈', '電子除濕器', '通風鞋架', '木製鞋架', '季風季節', '麂皮專用刷', '舊牙刷', '微纖維布', '皮革專用防霉油', '硼酸鹽防霉劑', '四級銨鹽防霉劑', '茶樹油噴霧', '肥皂', '紙巾', '防霉貼片', '無酸紙', '更新頻率', '批量商業防霉處理', '防霉技術培訓', '全面性霉變', '小蘇打溶液', '電動清潔刷', '防水透氣膜', '敏感人群的特殊風險', '含銀離子防霉劑', '臭氧發生器', '陰暗儲藏室', '手套', '休閒鞋', '室內鞋', '電子防霉鞋架', '雪松木鞋楦', '霉變保險評估', '防霉系統安裝', '納米防霉塗層', '除濕鞋櫃', '智能鞋櫃', '環保型霉菌處理', '防霉抗菌鞋墊']
    
    relation = ['常見於', '需要條件', '導致', '引起', '表現為', '生長於', '損害', '發展為', '識別通過', '活躍於', '反應於', '檢測通過', '維護使用', '保護', '不適合', '由組成', '感染', '協同作用', '加速', '監測使用', '殺滅', '清潔使用', '控制使用', '適用氣候', '費用為', '使用工具', '更新頻率', '清除使用', '特性為', '對抗', '增加風險', '存放於', '適用於', '提供服務', '處理於', '預防使用', '保存於', '保養使用', '評估使用', '修復', '消耗', '受影響', '易感', '適合', '管理通過', '包含', '促進', '降低風險', '影響', '投資回報', '分類為', '延緩', '效果持續', '受規範', '吸收', '包裝', '抵抗']
    
    # 連接到 Pinecone
    pc = Pinecone(api_key=config['pinecone_api_key'])
    
    # 定義共用元數據
    metadata = {
        "dimensions": 1024,
        "model": "jina-embeddings-v3"
    }

    # 批次處理實體並上傳
    print("開始處理實體...")
    entity_index = pc.Index('entity')
    batch_size = 10  # 設定批次大小，依據系統性能調整
    
    for i in range(0, len(entity), batch_size):
        batch = entity[i:i + batch_size]
        vectors = []
        
        for text in batch:
            embeddings = jina_embedding(text, config)
            if embeddings:
                # 每個向量需要一個唯一ID
                vector_id = str(uuid.uuid4())
                # 創建包含原始文本的元數據字典
                vector_metadata = {"text": text, "dimensions": metadata["dimensions"], "model": metadata["model"]}
                vectors.append({
                    "id": vector_id,  # 添加唯一ID
                    "values": embeddings,
                    "metadata": vector_metadata  # 添加元數據
                })
        
        if vectors:
            entity_index.upsert(vectors=vectors)
            print(f'已上傳實體批次 {i//batch_size + 1}/{(len(entity) + batch_size - 1)//batch_size}, 包含 {len(vectors)} 個項目')
    
    # 批次處理關係並上傳
    print("\n開始處理關係...")
    relation_index = pc.Index('relation')
    
    for i in range(0, len(relation), batch_size):
        batch = relation[i:i + batch_size]
        vectors = []
        
        for text in batch:
            embeddings = jina_embedding(text, config)
            if embeddings:
                # 每個向量需要一個唯一ID
                vector_id = str(uuid.uuid4())
                # 創建包含原始文本的元數據字典
                vector_metadata = {"text": text, "dimensions": metadata["dimensions"], "model": metadata["model"]}
                vectors.append({
                    "id": vector_id,  # 添加唯一ID
                    "values": embeddings,
                    "metadata": vector_metadata  # 添加元數據
                })
        
        if vectors:
            relation_index.upsert(vectors=vectors)
            print(f'已上傳關係批次 {i//batch_size + 1}/{(len(relation) + batch_size - 1)//batch_size}, 包含 {len(vectors)} 個項目')
    
    print("所有數據上傳完成!")




if __name__ == '__main__':
    import json
    with open('env.json', 'r', encoding='utf-8') as file:
        config = json.load(file)

    embedding_to_pinecone(config)
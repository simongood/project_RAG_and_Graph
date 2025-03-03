import requests


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
        embeddings =  data['data'][0]['embedding']   # 向量資料 : 1024 維
        return embeddings
    else:
        print(f"jina 呼叫失敗")


def embeddings_2_vector_db(index, embeddings, id, dimensions, model):
    """
    將向量嵌入存儲到 Pinecone 向量數據庫
    
    args:
        index: Pinecone 索引實例
        embeddings: 從 Jina 獲取的向量嵌入
        id: 文檔/片段的唯一標識符
        dimensions: 嵌入向量的維度 (例如 1024)
        model: 用於嵌入的模型名稱 (例如 "jina-embeddings-v3")
    """
    # 準備 metadata
    metadata = {
        "dimensions": dimensions,
        "model": model
    }
    
    # 使用 Pinecone 的 upsert 方法添加向量
    index.upsert(
        vectors=[{
            "id": id,
            "values": embeddings,  
            "metadata": metadata
        }]
    )
    
    return True

    
        
if __name__ == "__main__" :
    # 載入 env 設定 qdrant 連線
    import json
    from pinecone import Pinecone, ServerlessSpec

    with open('env.json', 'r', encoding='utf-8') as file:
        config = json.load(file)

    # 初始化 Pinecone gRPC 客戶端
    pc = Pinecone(api_key=config['pinecone_api_key'])
    
    # 檢查索引是否存在，如果不存在則創建
    index_name = "rag-vector-db-test"
    # 檢查索引是否存在，如果不存在則創建
    try:
        # 嘗試獲取索引
        index = pc.Index(index_name)
        print(f"已連接到索引: {index_name}")
    except Exception as e:
        print(f"索引不存在，正在創建: {index_name}")
        # 創建新索引
        pc.create_index(
            name=index_name,
            dimension=1024,  # Jina 嵌入的維度
            metric="cosine",  # 相似度度量方法
            spec=ServerlessSpec(
                cloud="aws",
                region="us-east-1"  # 可根據需要更改區域
            )
        )
        # 獲取新創建的索引
        index = pc.Index(index_name)


    chunks = [
        {
            "id": "chunk1",
            "text": "你的長文本內容你的長"
        },
        {
            "id": "chunk2",
            "text": "的長文本內容你的長文"
        },
        {
            "id": "chunk3",
            "text": "長文本內容你的長文本"
        }
    ]
    
    # ======= 測試 ==============================================
    for chunk in chunks:
        embeddings = jina_embedding(chunk['text'], config)
        embeddings_2_vector_db(index, embeddings, chunk['id'], 1024, "jina-embeddings-v3")
    
    # ======= 印出內容物 =======================================
    query_embedding = jina_embedding("長文本", config)

    # 連接到索引
    results = index.query(
        vector=query_embedding,
        top_k=3,
        include_metadata=True
    )
    print(results)
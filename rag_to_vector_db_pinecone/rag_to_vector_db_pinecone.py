from rag_pipeline.file_2_text import file_2_text
from rag_pipeline.text_2_chunks import text_2_chunks
from rag_pipeline.chunks_embeding_2_vector_db import (
    jina_embedding,
    embeddings_2_vector_db
)


import json
from pinecone import Pinecone, ServerlessSpec

def main():
    # 載入 env 設定
    with open('env.json', 'r', encoding='utf-8') as file:
        config = json.load(file)

    # 1. 將文件轉為文字
    text = file_2_text('data/mock_file_data.txt')
    
    # 2. 將文字分割片段
    chunks = text_2_chunks(text, 300, 60)   # 要調整
    # 將資料寫入 JSON 檔案
    with open('data/chunks.json', 'w', encoding='utf-8') as f:
        json.dump(chunks, f, ensure_ascii=False, indent=4)

    # 3. 存入 pinecone 數據庫
    # 初始化 Pinecone gRPC 客戶端
    pc = Pinecone(api_key=config['pinecone_api_key'])
    index = pc.Index("rag-vector-db-test")

    for chunk in chunks:
        embeddings = jina_embedding(chunk['text'], config)
        embeddings_2_vector_db(index, embeddings, chunk['id'], 1024, "jina-embeddings-v3")
    
    
if __name__ == '__main__':
    main()

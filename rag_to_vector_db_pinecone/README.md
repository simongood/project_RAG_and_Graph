# RAG
- 實作一個簡單的 RAG 系統，能夠：
    - 接收並處理文本檔案（我們將提供一篇學術論文或技術文件）
    - 將文件切分為適當大小的片段
    - 使用向量嵌入模型（如 OpenAI Embeddings 或 Sentence Transformers）為片段建立索引
    - 根據使用者查詢，檢索相關文件片段
    - 將檢索結果與查詢一起提交給 LLM（可使用 OpenAI API 或開源模型），生成回答


# pipeline 設定 :
- 可以將一文本從文本存至資料庫 
1. file_2_text.py  
    file 轉成文字
2. text_2_chunks.py
    文字切割，並將每句話給上一個 id
3. chunks_embeding_2_vector_db.py
    向量化文字，並存入向量庫且建立相對 id 索引


# 使用者設定
jupytor_notebook :
4. 根據使用者查詢，檢索相關文件片段
5. 檢索結果與查詢一起提交給 LLM，生成回答
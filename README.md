# 七日專案 RAG 與 Graph - RAG 實作與評比
1. 實作基本的檢索增強生成（RAG）系統
2. 構建和應用知識圖譜
3. 系統評估與比較分析

## 成果展示
![螢幕擷取畫面 2025-03-03 180910](https://github.com/user-attachments/assets/0d8b5b58-0a34-48d2-bc1a-65a7ab749a33)
![螢幕擷取畫面 2025-03-04 202015](https://github.com/user-attachments/assets/e95fc546-88cc-4efa-83f0-3cc79df3b092)
![螢幕擷取畫面 2025-03-05 021741](https://github.com/user-attachments/assets/b4056019-9332-4ec6-98b8-b4aa0292014b)


### 任務
任務一：基於向量檢索的 RAG 系統

實作一個簡單的 RAG 系統，能夠：
- 接收並處理文本檔案
- 將文件切分為適當大小的片段
- 使用向量嵌入模型（如 OpenAI Embeddings 或 Sentence Transformers）為片段建立索引
- 根據使用者查詢，檢索相關文件片段
- 將檢索結果與查詢一起提交給 LLM（可使用 OpenAI API 或開源模型），生成回答

請提供完整的程式碼實現，並展示至少 5 個不同複雜度的查詢範例及系統回答。

任務二：基於知識圖譜的生成系統

構建一個知識圖譜作為 RAG 系統的替代方案：
- 從相同的文件中提取實體和關係
- 構建基本的知識圖譜（可使用 NetworkX、Neo4j 或其他工具）
- 實現基於圖譜的查詢機制
- 使用相同的 LLM，但基於圖譜查詢結果生成回答
- 展示圖譜結構的可視化

請提供完整的程式碼實現，並對與任務一相同的 5 個查詢進行回答。

任務三：系統評估與比較

設計評估方法比較兩個系統的效能：
- 定義至少三種評估指標（如準確性、相關性、回答完整性等）
- 對兩個系統的回答進行評分（可使用自動化或手動方法）
- 分析兩種方法的優缺點
- 討論在哪些情況下各自的方法更為適合
- 提出可能的改進建議

---
# 專案資訊
- 項目：傳統 RAG 與 知識圖譜增強 RAG 實作與比較 
- 環境：Python 3.12.7 
- 套件：requests (2.32.3) langchain (0.3.19) langchain-openai (0.3.7) pinecone (6.0.1)
        networkx(3.4.2) matplotlib (3.10.1) 
- 安裝方式 : Poetry , requirements.txt
- 執行檔 :  
   1. RAG : [rag_query.ipynb](https://github.com/simongood/project_RAG_and_Graph/blob/master/rag_query.ipynb)
   2. graph RAG : [graph_query.ipynb](https://github.com/simongood/project_RAG_and_Graph/blob/master/graph_query.ipynb)
---
# 實作說明
- 技術文件 : [shoe-mold-technical-document.txt](https://github.com/simongood/project_RAG_and_Graph/blob/master/file/shoe-mold-technical-document.txt)
- 知識圖譜資料 : [graph_data.json](https://github.com/simongood/project_RAG_and_Graph/blob/master/data/graph_data.json)
- 完整文件參考 : [RAG_and_Graph_SummaryReport_2025-03-05](https://github.com/simongood/project_RAG_and_Graph/blob/master/RAG_and_Graph_SummaryReport_2025-03-05.pdf)

---
# RAG 與 graph - RAG 回應評測
- 對 graph rag 傳統 rag 定義了三項最大的差異特性，由 prompt 給 claude 分別對其回答進行評測 
  1. 推理能力 : 辨別回答中所呈現的多樣性、複雜性 
  2. 背景訊息 : 是否提供理解答案所需的足够背景和上下文 
  3. 資訊量匹配度 : 綜合考量焦點、簡潔度、額外資訊的必要性
- 詳細內容 : [grade.md](https://github.com/simongood/project_RAG_and_Graph/blob/master/grade.md)

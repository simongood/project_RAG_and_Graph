# 🐾 七日專案 RAG 與 Graph - RAG 實作與評比 🐾
>*2025/2/26 ~ 2025/3/4*
## 📋 專案概要
本專案實作並比較兩種知識增強技術：
1. 🦴 實作基本的檢索增強生成（RAG）系統
2. 🪁 構建和應用知識圖譜
3. 🏆 系統評估與比較分析

## 🌟 成果展示

<div align="center">
  <img src="https://github.com/user-attachments/assets/0d8b5b58-0a34-48d2-bc1a-65a7ab749a33" width="70%" style="margin: 10px 0; border-radius: 8px;" />
</div>
<div align="center">
  <img src="https://github.com/user-attachments/assets/e95fc546-88cc-4efa-83f0-3cc79df3b092" width="100%" style="margin: 10px 0; border-radius: 8px;" />
</div>
<div align="center">
  <img src="https://github.com/user-attachments/assets/b4056019-9332-4ec6-98b8-b4aa0292014b" width="60%" style="margin: 10px 0; border-radius: 8px;" />
</div>

## 📝 專案任務

### 🦴 任務一：基於向量檢索的 RAG 系統
實作一個簡單的 RAG 系統，能夠：
- ✅ 接收並處理文本檔案
- ✅ 將文件切分為適當大小的片段
- ✅ 使用向量嵌入模型為片段建立索引
- ✅ 根據使用者查詢，檢索相關文件片段
- ✅ 將檢索結果與查詢一起提交給 LLM，生成回答

### 🪁 任務二：基於知識圖譜的生成系統
構建知識圖譜作為 RAG 系統的替代方案：
- ✅ 從相同的文件中提取實體和關係
- ✅ 構建基本的知識圖譜
- ✅ 實現基於圖譜的查詢機制
- ✅ 使用相同的 LLM，但基於圖譜查詢結果生成回答
- ✅ 展示圖譜結構的可視化

### 🏠 任務三：系統評估與比較
- ✅ 定義評估指標（準確性、相關性、回答完整性等）
- ✅ 對兩個系統的回答進行評分
- ✅ 分析兩種方法的優缺點
- ✅ 討論適用場景
- ✅ 提出改進建議

## 🧠 專案資訊

### 技術堆疊
| 項目 | 規格 |
|------|------|
| **🐶 環境** | Python 3.12.7 |
| **✈️ 核心套件** | langchain (0.3.19), langchain-openai (0.3.7), pinecone (6.0.1) |
| **🐦 圖譜與視覺化** | networkx (3.4.2), matplotlib (3.10.1) |
| **📱 其他依賴** | requests (2.32.3) |
| **🛠️ 安裝方式** | Poetry, requirements.txt |

### 關鍵檔案
- **🦴 RAG 實作**: [rag_query.ipynb](https://github.com/simongood/project_RAG_and_Graph/blob/master/rag_query.ipynb)
- **🪁 圖譜 RAG 實作**: [graph_query.ipynb](https://github.com/simongood/project_RAG_and_Graph/blob/master/graph_query.ipynb)
- **📄 技術文件**: [shoe-mold-technical-document.txt](https://github.com/simongood/project_RAG_and_Graph/blob/master/file/shoe-mold-technical-document.txt)
- **🧩 知識圖譜資料**: [graph_data.json](https://github.com/simongood/project_RAG_and_Graph/blob/master/data/graph_data.json)
- **📊 完整報告**: [RAG_and_Graph_SummaryReport_2025-03-05](https://github.com/simongood/project_RAG_and_Graph/blob/master/RAG_and_Graph_SummaryReport_2025-03-05.pdf)

## 🏆 RAG 與 graph - RAG 回應評測

對 graph rag 與傳統 rag 定義了三項最大的差異特性：

| 評測指標 | 說明 |
|---------|------|
| **🔍 推理能力** | 回答中所呈現的多樣性與複雜性 |
| **🌐 背景訊息** | 是否提供理解答案所需的足够背景和上下文 |
| **⚖️ 資訊量匹配度** | 綜合考量焦點、簡潔度、額外資訊的必要性 |

**詳細評測結果請參考** : [grade.md](https://github.com/simongood/project_RAG_and_Graph/blob/master/grade.md)

> *"Sometimes I lie on my doghouse roof and think about graph. Other times, I just lie there."* 🐾

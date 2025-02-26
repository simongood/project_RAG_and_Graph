import json
import math
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

def text_2_chunks(text, chunk_size=500, chunk_overlap=100):
    """
    将文档切割成更小的文本块
    
    参数:
    - documents: 原始文档列表
    - chunk_size: 文本分块大小
    - chunk_overlap: 文本块之间的重叠大小
    
    返回:
    - 切割后的文本块列表
    """
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    # 创建 Document 对象
    document = Document(page_content=text)
    chunks = text_splitter.split_documents([document])

    # 转换为指定格式
    formatted_chunks = [
        {
            "id": f"chunk{i+1}", 
            "text": chunk.page_content
        } 
        for i, chunk in enumerate(chunks)
    ]
    
    return formatted_chunks

# 示例使用
if __name__ == "__main__":
    sample_text = "你的長文本內容" * 10
    result = text_2_chunks(sample_text, 10, 2)
    
    # 打印JSON
    print(json.dumps(result, ensure_ascii=False, indent=4))
    
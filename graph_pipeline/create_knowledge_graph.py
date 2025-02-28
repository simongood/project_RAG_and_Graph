import networkx as nx
import matplotlib.pyplot as plt
import json
import pickle

def create_knowledge_graph(data, save_file):
    """
    創建知識圖譜並選擇性地儲存到檔案
    
    Args:
        data (dict): 包含人物和關係的字典
        save_file (str, optional): 如果提供，將知識圖譜保存到這個檔案路徑
        
    Returns:
        nx.DiGraph: 創建好的知識圖譜
    """
    # 建立知識圖譜
    G = nx.DiGraph()

    # 添加節點（人物）
    for person in data["people"]:
        G.add_node(person["name"], age=person["age"])

    # 添加邊（關係）
    for rel in data["relationships"]:
        G.add_edge(
            rel["source"],
            rel["target"],
            type=rel["type"],
            since=rel["properties"]["since"]
        )
    

    with open(save_file, 'wb') as f:
        pickle.dump(G, f)
    print(f"知識圖譜已儲存到: {save_file}")


if __name__ == '__main__':
    # 載入 env 設定
    with open('env.json', 'r', encoding='utf-8') as file:
        config = json.load(file)

    with open("data/graph_data.json", "r", encoding="utf-8") as f:
        data =  json.load(f)

    # 創建知識圖譜並直接儲存
    graph_file = "data/knowledge_graph.pkl"
    create_knowledge_graph(data, save_file=graph_file)
    
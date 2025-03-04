import networkx as nx
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
    
    # 添加節點和關係
    for rel in data["relationships"]:
        source = rel["source"]
        target = rel["target"]
        relation = rel["relation"]
        description = rel["description"]
        
        # 添加節點（如果不存在）
        if not G.has_node(source):
            G.add_node(source)
        if not G.has_node(target):
            G.add_node(target)
        
        # 添加邊和邊的屬性
        G.add_edge(source, target, relation=relation, description=description)
    
    # 如果提供了保存路徑，則保存圖譜
    if save_file:
        with open(save_file, 'wb') as f:
            pickle.dump(G, f)
            
    return G


if __name__ == '__main__':
    # 載入 env 設定
    with open('env.json', 'r', encoding='utf-8') as file:
        config = json.load(file)

    with open("data/graph_data.json", "r", encoding="utf-8") as f:
        data =  json.load(f)

    # 創建知識圖譜並直接儲存
    graph_file = "data/knowledge_graph.pkl"
    create_knowledge_graph(data, save_file=graph_file)
    
import matplotlib.pyplot as plt
import networkx as nx

def visualize_knowledge_graph(G, output_file=None):
    """
    可視化知識圖譜
    
    Args:
        G (nx.DiGraph): 要可視化的知識圖譜
        output_file (str, optional): 輸出圖片的文件路徑，如果為None則僅顯示不保存
    
    Returns:
        None
    """
    # 設置中文字體支援
    try:
        # 嘗試設置全局字體
        plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'SimHei', 'Microsoft YaHei', 'DejaVu Sans', 'sans-serif']
        plt.rcParams['axes.unicode_minus'] = False  # 解決負號顯示問題
        # 如果使用MacOS，可以嘗試
        # plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'Heiti TC', 'sans-serif']
        # 如果使用Windows，可以嘗試
        # plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei', 'sans-serif']
    except:
        print("無法設置中文字體，將使用默認字體")
    
    plt.figure(figsize=(10, 8))

    # 使用spring_layout來確定節點位置
    pos = nx.spring_layout(G, seed=42)

    # 繪製節點
    nx.draw_networkx_nodes(G, pos, node_size=700, node_color='lightblue')

    # 繪製邊
    nx.draw_networkx_edges(G, pos, width=1.5, alpha=0.7, edge_color='gray', 
                          connectionstyle='arc3,rad=0.1', arrowsize=15)

    # 為節點添加標籤 - 使用適合中文的字體
    nx.draw_networkx_labels(G, pos, font_size=12)

    # 為邊添加標籤（關係成立年份）
    edge_labels = {(u, v): f"認識自: {d['since']}" for u, v, d in G.edges(data=True)}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10)

    # 添加標題
    plt.title("人物關係知識圖譜", fontsize=16)
    plt.axis('off')  # 隱藏座標軸
    plt.tight_layout()
    # 儲存圖片或顯示
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    
    plt.show()



if __name__ == "__main__":
    import pickle

    with open('data/knowledge_graph.pkl', 'rb') as f:
        G = pickle.load(f)

    output_filepath = 'knowledge_graph.png'
    visualize_knowledge_graph(G, output_filepath)
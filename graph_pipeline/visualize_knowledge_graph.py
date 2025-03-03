import matplotlib.pyplot as plt
import networkx as nx

def visualize_knowledge_graph(G, output_file=None):
    """
    可視化知識圖譜
    
    Args:
        G (nx.DiGraph): 要可視化的知識圖譜
        output_file (str): 輸出圖片的文件路徑
    
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
    
    # 創建圖形
    plt.figure(figsize=(16, 12))
    
    # 使用spring佈局
    pos = nx.spring_layout(G, k=0.3, seed=42)
    
    # 繪製節點
    nx.draw_networkx_nodes(G, pos, node_color='skyblue', node_size=800, alpha=0.8)
    
    # 繪製節點標籤
    nx.draw_networkx_labels(G, pos, font_size=6, font_family='sans-serif')
    
    # 繪製邊
    nx.draw_networkx_edges(G, pos, width=1.5, alpha=0.7, arrowsize=20)
    
    # 繪製邊標籤
    edge_labels = {(u, v): d['relation'] for u, v, d in G.edges(data=True)}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=6)
    
    # 設置標題和關閉坐標軸
    plt.title("鞋類發霉問題知識圖譜", fontsize=16)
    plt.axis('off')
    
    # 保存圖片
    if output_file:
        plt.savefig(output_file, dpi=300, bbox_inches='tight')
        print(f"圖譜已保存至: {output_file}")
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    import pickle

    with open('data/knowledge_graph.pkl', 'rb') as f:
        G = pickle.load(f)

    output_filepath = 'knowledge_graph.png'
    visualize_knowledge_graph(G, output_filepath)
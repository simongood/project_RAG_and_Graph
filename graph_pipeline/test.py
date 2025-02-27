import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import pandas as pd

# 設定中文字體
try:
    # 嘗試使用系統中文字體
    font = FontProperties(fname=r'C:\Windows\Fonts\msjh.ttc')  # Windows 微軟正黑體
except:
    # 無法使用指定字體時的備用方案
    font = FontProperties()

# 創建一個有向圖作為知識圖譜
G = nx.MultiDiGraph()

# 添加實體節點
# 黴菌類型
fungi_species = [
    "黴菌", "真菌", "毛黴", "根黴", "青黴", "曲黴", "黑曲黴", "鏈格孢", "白腐菌",
    "Mucor", "Rhizopus", "Penicillium", "Aspergillus", "Alternaria", "Fusarium", 
    "Trichoderma", "Beauveria bassiana", "Acremonium", "Penicillium roqueforti",
    "Aspergillus niger", "Aspergillus oryzae", "Penicillium chrysogenum", 
    "Acremonium chrysogenum", "Aspergillus terreus", "Aspergillus flavus",
    "Aspergillus ochraceus", "Penicillium verrucosum", "Fusarium graminearum"
]

# 黴菌結構
fungi_structures = ["菌絲體", "菌絲", "孢子", "孢子囊", "有隔菌絲", "無隔菌絲", "無性孢子", "有性孢子"]

# 黴菌分類
classification_categories = ["接合菌門", "子囊菌門", "半知菌門", "接合菌亞門", "擔子菌門"]

# 生長條件
growth_conditions = ["溫度", "pH值", "水分活度", "氧氣"]

# 代謝特點
metabolic_features = ["胞外酶", "澱粉酶", "蛋白酶", "纖維素酶", "降解複雜有機物", "次級代謝產物", "抗生素", "黴菌毒素"]

# 應用領域
application_areas = ["工業應用", "農業應用", "環境應用", "發酵工業", "酶製劑生產", "抗生素生產", 
                     "生物防治", "植物生長促進", "生物修復", "廢棄物處理"]

# 黴菌毒素
mycotoxins = ["黃曲霉毒素", "赭曲霉毒素", "鐮刀菌毒素", "單端孢霉烯族毒素", "玉米赤霉烯酮", 
              "Aflatoxins", "Ochratoxins", "Fumonisins", "Trichothecenes", "Zearalenone"]

# 產品
products = ["青黴素", "頭孢菌素", "他汀類", "洛伐他汀", "檸檬酸", "葡萄糖酸", "藍紋奶酪", 
           "豆豉", "醬油", "生物乙醇", "生物柴油"]

# 添加節點
for item in fungi_species:
    G.add_node(item, type="fungi_species")

for item in fungi_structures:
    G.add_node(item, type="structure")

for item in classification_categories:
    G.add_node(item, type="classification")

for item in growth_conditions:
    G.add_node(item, type="growth_condition")

for item in metabolic_features:
    G.add_node(item, type="metabolic_feature")

for item in application_areas:
    G.add_node(item, type="application_area")

for item in mycotoxins:
    G.add_node(item, type="mycotoxin")

for item in products:
    G.add_node(item, type="product")

# 添加關係
# 黴菌和結構
for structure in fungi_structures:
    G.add_edge("黴菌", structure, type="has_structure")

# 黴菌分類關係
for category in ["接合菌門", "子囊菌門", "半知菌門"]:
    G.add_edge("黴菌", category, type="classified_as")

# 種類和分類關係
G.add_edge("毛黴", "接合菌門", type="belongs_to")
G.add_edge("根黴", "接合菌門", type="belongs_to")
G.add_edge("青黴", "子囊菌門", type="belongs_to")
G.add_edge("曲黴", "子囊菌門", type="belongs_to")
G.add_edge("黑曲黴", "半知菌門", type="belongs_to")
G.add_edge("鏈格孢", "半知菌門", type="belongs_to")

# 屬和種的關係
G.add_edge("Mucor", "毛黴", type="latin_name_of")
G.add_edge("Rhizopus", "根黴", type="latin_name_of")
G.add_edge("Penicillium", "青黴", type="latin_name_of")
G.add_edge("Aspergillus", "曲黴", type="latin_name_of")
G.add_edge("Alternaria", "黑曲黴", type="latin_name_of")
G.add_edge("Fusarium", "鏈格孢", type="latin_name_of")

# 黴菌和生長條件
for condition in growth_conditions:
    G.add_edge("黴菌", condition, type="requires")

# 黴菌和代謝特點
for feature in metabolic_features:
    G.add_edge("黴菌", feature, type="has_feature")

# 黴菌產品關係
G.add_edge("Penicillium chrysogenum", "青黴素", type="produces")
G.add_edge("Acremonium chrysogenum", "頭孢菌素", type="produces")
G.add_edge("Aspergillus terreus", "洛伐他汀", type="produces")
G.add_edge("Aspergillus niger", "檸檬酸", type="produces")
G.add_edge("Penicillium roqueforti", "藍紋奶酪", type="used_in")
G.add_edge("Aspergillus oryzae", "澱粉酶", type="produces")

# 黴菌毒素關係
G.add_edge("Aspergillus flavus", "黃曲霉毒素", type="produces")
G.add_edge("Aspergillus ochraceus", "赭曲霉毒素", type="produces")
G.add_edge("Penicillium verrucosum", "赭曲霉毒素", type="produces")
G.add_edge("Fusarium", "鐮刀菌毒素", type="produces")
G.add_edge("Fusarium", "單端孢霉烯族毒素", type="produces")
G.add_edge("Fusarium graminearum", "玉米赤霉烯酮", type="produces")

# 應用領域關係
G.add_edge("黴菌", "工業應用", type="has_application")
G.add_edge("黴菌", "農業應用", type="has_application")
G.add_edge("黴菌", "環境應用", type="has_application")
G.add_edge("工業應用", "發酵工業", type="includes")
G.add_edge("工業應用", "酶製劑生產", type="includes")
G.add_edge("工業應用", "抗生素生產", type="includes")
G.add_edge("農業應用", "生物防治", type="includes")
G.add_edge("農業應用", "植物生長促進", type="includes")
G.add_edge("環境應用", "生物修復", type="includes")
G.add_edge("環境應用", "廢棄物處理", type="includes")

# 特殊應用關係
G.add_edge("Trichoderma", "生物防治", type="used_for")
G.add_edge("Beauveria bassiana", "害蟲防治", type="used_for")
G.add_edge("白腐菌", "有機污染物降解", type="used_for")

# 知識圖譜基本信息
print(f"知識圖譜總節點數: {G.number_of_nodes()}")
print(f"知識圖譜總邊數: {G.number_of_edges()}")

# 統計各類型節點數量
node_types = {}
for node, attrs in G.nodes(data=True):
    node_type = attrs.get('type', 'unknown')
    node_types[node_type] = node_types.get(node_type, 0) + 1

print("\n節點類型分佈:")
for node_type, count in node_types.items():
    print(f"{node_type}: {count}")

# 統計各類型關係數量
edge_types = {}
for _, _, attrs in G.edges(data=True):
    edge_type = attrs.get('type', 'unknown')
    edge_types[edge_type] = edge_types.get(edge_type, 0) + 1

print("\n關係類型分佈:")
for edge_type, count in edge_types.items():
    print(f"{edge_type}: {count}")

# ===== 查詢示例 =====

def query_toxin_producers():
    """查詢1: 找出所有產生黴菌毒素的菌種"""
    print("\n查詢1: 產生黴菌毒素的菌種")
    results = []
    for u, v, data in G.edges(data=True):
        if data.get('type') == 'produces' and G.nodes[v].get('type') == 'mycotoxin':
            results.append((u, v))
    
    # 將結果轉為DataFrame以便更好地展示
    df = pd.DataFrame(results, columns=['菌種', '毒素'])
    return df

def query_penicillium_applications():
    """查詢2: 找出青黴屬的所有應用和產品"""
    print("\n查詢2: 青黴屬的應用和產品")
    results = []
    for u, v, data in G.edges(data=True):
        if u.startswith("Penicillium") and data.get('type') in ['produces', 'used_in']:
            results.append((u, data.get('type'), v))
    
    df = pd.DataFrame(results, columns=['青黴種類', '關係', '產品'])
    return df

def query_biocontrol_fungi():
    """查詢3: 用於生物防治的黴菌"""
    print("\n查詢3: 用於生物防治的黴菌")
    results = []
    for u, v, data in G.edges(data=True):
        if v == "生物防治" or v == "害蟲防治":
            results.append((u, v))
    
    df = pd.DataFrame(results, columns=['菌種', '應用'])
    return df

def query_fungi_structures():
    """查詢4: 黴菌的所有結構"""
    print("\n查詢4: 黴菌的結構")
    results = []
    for u, v, data in G.edges(data=True):
        if u == "黴菌" and data.get('type') == 'has_structure':
            results.append(v)
    
    return results

def query_industrial_paths():
    """查詢5: 黴菌在工業中的應用路徑"""
    print("\n查詢5: 黴菌在工業中的應用路徑")
    # 找出黴菌到工業應用的直接路徑
    direct_paths = list(nx.all_simple_paths(G, source="黴菌", target="工業應用", cutoff=1))
    
    # 找出工業應用的細分領域
    industrial_subareas = []
    for u, v, data in G.edges(data=True):
        if u == "工業應用" and data.get('type') == 'includes':
            industrial_subareas.append(v)
    
    return {
        "direct_paths": direct_paths,
        "industrial_subareas": industrial_subareas
    }

def visualize_toxin_subgraph():
    """可視化以黴菌毒素為中心的子圖"""
    # 找出所有產生毒素的菌種
    toxin_producers = set()
    for u, v, data in G.edges(data=True):
        if data.get('type') == 'produces' and G.nodes[v].get('type') == 'mycotoxin':
            toxin_producers.add(u)
    
    # 創建子圖節點集合
    mycotoxin_subgraph_nodes = list(toxin_producers) + mycotoxins
    mycotoxin_subgraph = G.subgraph(mycotoxin_subgraph_nodes)
    
    # 繪製子圖
    plt.figure(figsize=(12, 8))
    pos = nx.spring_layout(mycotoxin_subgraph, seed=42)
    
    # 根據節點類型著色
    node_colors = []
    for n in mycotoxin_subgraph.nodes():
        if G.nodes[n].get('type') == 'fungi_species':
            node_colors.append('lightblue')
        else:
            node_colors.append('lightgreen')
    
    nx.draw_networkx_nodes(mycotoxin_subgraph, pos, node_color=node_colors, node_size=1500, alpha=0.8)
    nx.draw_networkx_edges(mycotoxin_subgraph, pos, width=1.5, alpha=0.7)
    nx.draw_networkx_labels(mycotoxin_subgraph, pos, font_size=10)
    
    # 添加邊標籤
    edge_labels = {}
    for u, v, data in mycotoxin_subgraph.edges(data=True):
        edge_labels[(u, v)] = data.get('type', '')
    
    nx.draw_networkx_edge_labels(mycotoxin_subgraph, pos, edge_labels=edge_labels, font_size=8)
    
    plt.title("黴菌毒素及其產生菌種", fontsize=15)
    plt.axis('off')
    plt.tight_layout()
    
    return plt

# 執行查詢
toxin_producers_df = query_toxin_producers()
print(toxin_producers_df)

penicillium_applications_df = query_penicillium_applications()
print(penicillium_applications_df)

biocontrol_fungi_df = query_biocontrol_fungi()
print(biocontrol_fungi_df)

fungi_structures = query_fungi_structures()
print("黴菌結構:", fungi_structures)

industrial_paths = query_industrial_paths()
print("黴菌到工業應用的路徑:", industrial_paths["direct_paths"])
print("工業應用的細分領域:", industrial_paths["industrial_subareas"])

# 路徑查詢示例 - 從Aspergillus niger到其產品的路徑
paths = list(nx.all_simple_paths(G, source="Aspergillus niger", target="檸檬酸", cutoff=1))
print("\n從Aspergillus niger到檸檬酸的路徑:")
for path in paths:
    print(" -> ".join(path))

# 示範如何使用NetworkX的算法分析知識圖譜
# 計算中心度
print("\n節點中心度(按中心度排序的前10個節點):")
degree_centrality = nx.degree_centrality(G)
sorted_centrality = sorted(degree_centrality.items(), key=lambda x: x[1], reverse=True)[:10]
for node, centrality in sorted_centrality:
    print(f"{node}: {centrality:.4f}")

# 找出最大連通子圖
largest_cc = max(nx.weakly_connected_components(G), key=len)
print(f"\n最大連通子圖大小: {len(largest_cc)} 節點")

# 使用NetworkX來視覺化產品子圖
product_related = set()
for u, v, data in G.edges(data=True):
    if data.get('type') in ['produces', 'used_in'] and G.nodes[v].get('type') == 'product':
        product_related.add(u)
        product_related.add(v)

product_subgraph = G.subgraph(product_related)

plt.figure(figsize=(10, 6))
pos = nx.spring_layout(product_subgraph, seed=123)
nx.draw(product_subgraph, pos, with_labels=True, 
        node_color='lightblue', node_size=700, font_size=8, 
        font_weight='bold', edge_color='gray')
plt.title("黴菌產品關係圖")
plt.show()

# 展示如何構建複雜查詢
print("\n複雜查詢示例: 找出既能產生有用產品又能產生毒素的菌種")
useful_producers = set()
toxin_producers = set()

for u, v, data in G.edges(data=True):
    if data.get('type') == 'produces':
        if G.nodes[v].get('type') == 'product':
            useful_producers.add(u)
        elif G.nodes[v].get('type') == 'mycotoxin':
            toxin_producers.add(u)

dual_nature_fungi = useful_producers.intersection(toxin_producers)
print("既有益又有害的菌種:", dual_nature_fungi)
import json
from neo4j import GraphDatabase
import matplotlib.pyplot as plt
import networkx as nx




# 從JSON文件讀取數據
def load_from_json(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)
    
# 上傳數據
def create_graph_database(data, config):
    # 創建Neo4j連接
    # Neo4j連接資訊
    URI = config['neo4j_uri'] 
    USERNAME = "neo4j"  # 預設用戶名
    PASSWORD = config['neo4j_password']
    driver = GraphDatabase.driver(URI, auth=(USERNAME, PASSWORD))

    driver.verify_connectivity()

    # with driver.session(database="neo4j") as session:
    #     result = session.run("RETURN 'Connection successful' AS message")
    #     message = result.single()["message"]
    #     print(f"測試結果: {message}")
    #     return True

    # with driver.session() as session:
    #     # 清空資料庫（謹慎使用！）
    #     session.run("MATCH (n) DETACH DELETE n")
        
    #     # 創建節點
    #     for person in data["people"]:
    #         session.run(
    #             "CREATE (:Person {name: $name, age: $age})",
    #             name=person["name"], age=person["age"]
    #         )
    #         print(f"已創建節點: {person['name']}, {person['age']}歲")
        
    #     # 創建關係
    #     for rel in data["relationships"]:
    #         cypher_query = (
    #             f"MATCH (a:Person), (b:Person) "
    #             f"WHERE a.name = $source AND b.name = $target "
    #             f"CREATE (a)-[r:{rel['type']} $props]->(b)"
    #         )
    #         session.run(
    #             cypher_query, 
    #             source=rel["source"], 
    #             target=rel["target"], 
    #             props=rel["properties"]
    #         )
    #         print(f"已創建關係: {rel['source']} -{rel['type']}-> {rel['target']}")
            
    #     print("\n圖資料庫建置完成！")
    driver.close()


if __name__ == '__main__':
    # 載入 env 設定
    with open('env.json', 'r', encoding='utf-8') as file:
        config = json.load(file)
    data = load_from_json("data/graph_data.json")

    create_graph_database(data, config)
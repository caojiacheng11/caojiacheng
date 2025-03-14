pip install streamlit
pip install pandas
pip install networkx

import streamlit as st
import pandas as pd
import networkx as nx
from pyvis.network import Network
from streamlit.components.v1 import html

def create_sample_data():
    nodes = [
        {"id": 1, "label": "characteristics", "group": "characteristics"},  

        {"id": 2, "label": "demographic characteristics", "group": "characteristics"},
        {"id": 3, "label": "disease characteristics", "group": "characteristics"},
        {"id": 4, "label": "individual characteristics", "group": "characteristics"},

        
        {"id": 5, "label": "tumor-related factors", "group": "disease characteristics"},
        {"id": 6, "label": "physical condition related score", "group": "disease characteristics"},
        {"id": 7, "label": "laboratory indices", "group": "disease characteristics"},
        {"id": 8, "label": "administration processes", "group": "disease characteristics"},
        {"id": 9, "label": "surgery processes", "group": "disease characteristics"},
        {"id": 10, "label": "past histories", "group": "disease characteristics"},
        {"id": 11, "label": "complications", "group": "disease characteristics"},

        
        {"id": 12, "label": "age", "group": "demographic characteristics"},
        {"id": 13, "label": "sex", "group": "demographic characteristics"},
        {"id": 14, "label": "BMI", "group": "demographic characteristics"},
        {"id": 15, "label": "tumor blood supply", "group": "tumor-related factors"},
        {"id": 16, "label": "number of tumors in the liver", "group": "tumor-related factors"},
        {"id": 17, "label": "tumor diameter", "group": "tumor-related factors"},
        {"id": 18, "label": "tumor volume", "group": "tumor-related factors"},
        {"id": 19, "label": "tumor capsule", "group": "tumor-related factors"},
        {"id": 20, "label": "distance from tumor to hepatic capsule", "group": "tumor-related factors"},
        {"id": 21, "label": "vascular invasion", "group": "tumor-related factors"},
        {"id": 22, "label": "PVTT", "group": "tumor-related factors"},
        {"id": 23, "label": "stage of liver cancer", "group": "tumor-related factors"},
        {"id": 24, "label": "hepatic artery diameter", "group": "tumor-related factors"},
        {"id": 25, "label": "Child-Pugh", "group": "tumor-related factors"},
        {"id": 26, "label": "ECOG performance status", "group": "physical condition related score"},
        {"id": 27, "label": "prothrombin activity", "group": "laboratory indices"},
        {"id": 28, "label": "AFP", "group": "laboratory indices"},
        {"id": 29, "label": "C-reactive protein", "group": "laboratory indices"},
        {"id": 30, "label": "hemoglobin", "group": "laboratory indices"},
        {"id": 31, "label": "IL-6", "group": "laboratory indices"},
        {"id": 32, "label": "IL-10", "group": "laboratory indices"},
        {"id": 33, "label": "TNF-α", "group": "laboratory indices"},
        {"id": 34, "label": "MTT", "group": "laboratory indices"},
        {"id": 35, "label": "NLR", "group": "laboratory indices"},
        {"id": 36, "label": "PLR", "group": "laboratory indices"},
        {"id": 37, "label": "Adriamycin dose", "group": "administration processes"},
        {"id": 38, "label": "Pirarubicin mixed with iodized oil for embolization", "group": "administration processes"},
        {"id": 39, "label": "Adriamycin mixed with iodized oil for embolization", "group": "administration processes"},
        {"id": 40, "label": "iodized oil dose", "group": "administration processes"},
        {"id": 41, "label": "DEB-TACE", "group": "administration processes"},
        {"id": 42, "label": "particle size of Drug-eluting Beads", "group": "administration processes"},
        {"id": 43, "label": "anhydrous alcohol embolism", "group": "administration processes"},
        {"id": 44, "label": "dose of oxaliplatin", "group": "administration processes"},
        {"id": 45, "label": "preparation time of oxaliplatin", "group": "administration processes"},
        {"id": 46, "label": "manufacturer of oxaliplatin", "group": "administration processes"},
        {"id": 47, "label": "iodide sedimentation type", "group": "surgery processes"},
        {"id": 48, "label": "range of embolization", "group": "surgery processes"},
        {"id": 49, "label": "superselective chemoembolization", "group": "surgery processes"},
        {"id": 50, "label": "extrahepatic perfusion", "group": "surgery processes"},
        {"id": 51, "label": "number of TACE", "group": "past histories"},
        {"id": 52, "label": "liver cancer surgery history", "group": "past histories"},
        {"id": 53, "label": "liver cancer transplantation history", "group": "past histories"},
        {"id": 54, "label": "drinking history", "group": "past histories"},
        {"id": 55, "label": "number of HAIC", "group": "past histories"},
        {"id": 56, "label": "chronic cancer pain", "group": "past histories"},
        {"id": 57, "label": "ascites", "group": "complications"},
        {"id": 58, "label": "diabetes history", "group": "complications"},
        {"id": 59, "label": "chronic liver disease history", "group": "complications"},
        {"id": 60, "label": "gastroduodenal ulcer", "group": "complications"},
        {"id": 61, "label": "anxiety", "group": "individual characteristics"},
        {"id": 62, "label": "depression", "group": "individual characteristics"},
        {"id": 63, "label": "abdominal pain history after TACE", "group": "individual characteristics"},
        {"id": 64, "label": "preoperative analgesic administration", "group": "individual characteristics"},
        {"id": 65, "label": "intraoperative analgesic administration", "group": "individual characteristics"},
        {"id": 66, "label": "pain before surgery", "group": "individual characteristics"},
    ]


    edges = [
    {"from": 1, "to": 2, "label": "include"},
    {"from": 1, "to": 3, "label": "include"},
    {"from": 1, "to": 4, "label": "include"},
    
    {"from": 3, "to": 5, "label": "include"},
    {"from": 3, "to": 6, "label": "include"},
    {"from": 3, "to": 7, "label": "include"},
    {"from": 3, "to": 8, "label": "include"},
    {"from": 3, "to": 9, "label": "include"},
    {"from": 3, "to": 10, "label": "include"},
    {"from": 3, "to": 11, "label": "include"},

    {"from": 2, "to": 12, "label": "include"},
    {"from": 2, "to": 13, "label": "include"},
    {"from": 2, "to": 14, "label": "include"},

    {"from": 5, "to": 15, "label": "include"},
    {"from": 5, "to": 16, "label": "include"},
    {"from": 5, "to": 17, "label": "include"},
    {"from": 5, "to": 18, "label": "include"},
    {"from": 5, "to": 19, "label": "include"},
    {"from": 5, "to": 20, "label": "include"},
    {"from": 5, "to": 21, "label": "include"},
    {"from": 5, "to": 22, "label": "include"},
    {"from": 5, "to": 23, "label": "include"},
    {"from": 5, "to": 24, "label": "include"},
    {"from": 5, "to": 25, "label": "include"},

    {"from": 6, "to": 26, "label": "include"},

    {"from": 7, "to": 27, "label": "include"},
    {"from": 7, "to": 28, "label": "include"},
    {"from": 7, "to": 29, "label": "include"},
    {"from": 7, "to": 30, "label": "include"},
    {"from": 7, "to": 31, "label": "include"},
    {"from": 7, "to": 32, "label": "include"},
    {"from": 7, "to": 33, "label": "include"},
    {"from": 7, "to": 34, "label": "include"},
    {"from": 7, "to": 35, "label": "include"},
    {"from": 7, "to": 36, "label": "include"},

    {"from": 8, "to": 37, "label": "include"},
    {"from": 8, "to": 38, "label": "include"},
    {"from": 8, "to": 39, "label": "include"},
    {"from": 8, "to": 40, "label": "include"},
    {"from": 8, "to": 41, "label": "include"},
    {"from": 8, "to": 42, "label": "include"},
    {"from": 8, "to": 43, "label": "include"},
    {"from": 8, "to": 44, "label": "include"},
    {"from": 8, "to": 45, "label": "include"},
    {"from": 8, "to": 46, "label": "include"},

    {"from": 9, "to": 47, "label": "include"},
    {"from": 9, "to": 48, "label": "include"},
    {"from": 9, "to": 49, "label": "include"},
    {"from": 9, "to": 50, "label": "include"},

    {"from": 10, "to": 51, "label": "include"},
    {"from": 10, "to": 52, "label": "include"},
    {"from": 10, "to": 53, "label": "include"},
    {"from": 10, "to": 54, "label": "include"},
    {"from": 10, "to": 55, "label": "include"},
    {"from": 10, "to": 56, "label": "include"},

    {"from": 11, "to": 57, "label": "include"},
    {"from": 11, "to": 58, "label": "include"},
    {"from": 11, "to": 59, "label": "include"},
    {"from": 11, "to": 60, "label": "include"},

    {"from": 4, "to": 61, "label": "include"},
    {"from": 4, "to": 62, "label": "include"},
    {"from": 4, "to": 63, "label": "include"},
    {"from": 4, "to": 64, "label": "include"},
    {"from": 4, "to": 65, "label": "include"},
    {"from": 4, "to": 66, "label": "include"},
  ]
    return pd.DataFrame(nodes), pd.DataFrame(edges)



# 构建知识图谱
def build_knowledge_graph(nodes_df, edges_df):
    G = nx.Graph()
    
    # 添加节点
    for _, row in nodes_df.iterrows():
        G.add_node(row['id'], 
                  label=row['label'],
                  group=row['group'])
    
    # 添加边
    for _, row in edges_df.iterrows():
        G.add_edge(row['from'], row['to'], 
                  title=row.get('label', ''))
    
    return G

# 使用PyVis生成可视化
def visualize_with_pyvis(graph):
    net = Network(height="600px", 
                 width="100%",
                 bgcolor="#ffffff",
                 font_color="black",
                 directed=True)
    
    # 从NetworkX导入图
    net.from_nx(graph)
    
    # 配置可视化参数
    net.set_options("""
    {
      "physics": {
        "barnesHut": {
          "gravitationalConstant": -80000,
          "springLength": 250
        },
        "minVelocity": 0.75
      },
      "nodes": {
        "font": {
          "size": 40
        }
      }
    }
    """)
    
    # 保存为HTML文件
    net.save_graph("knowledge_graph.html")
    return open("knowledge_graph.html", "r").read()

# 创建Streamlit网页应用
def main():
    st.set_page_config(page_title="Knowledge Graph", layout="wide")
    
    st.title("Knowledge Graph")
    st.markdown("---")
    
    # 创建数据
    nodes_df, edges_df = create_sample_data()
    
    
    # 构建知识图谱
    G = build_knowledge_graph(nodes_df, edges_df)
    
    # 生成可视化
    html_content = visualize_with_pyvis(G)
    
    # 显示可视化结果
    html(html_content, height=620)


if __name__ == "__main__":
    main()

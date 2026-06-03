import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="AI分析报告", page_icon="🤖", layout="wide")
st.title("🤖 AI 智能分析报告（DeepSeek）")

try:
    banks = pd.read_csv("data/bank_scores.csv", encoding="utf-8-sig")["银行"].tolist()
except:
    banks = ["招商银行", "工商银行", "建设银行"]

selected = st.selectbox("选择分析银行", banks)
api_key = os.getenv("DEEPSEEK_API_KEY")

if st.button("✅ 生成专业分析报告"):
    if not api_key:
        st.error("请配置API Key")
    else:
        with st.spinner("AI正在生成双评价综合报告..."):
            prompt = f"""
            你是专业银行财务分析师，请基于CAMEL评级与双评价机制，对{selected}进行分析：
            1. 盈利能力
            2. 资产质量
            3. 资本充足性
            4. 流动性
            5. 结合机器学习权重与专家观点给出综合结论
            语言专业、结构清晰、结论明确。
            """
            try:
                resp = requests.post("https://api.deepseek.com/chat/completions",
                    headers={"Authorization": f"Bearer {api_key}"},
                    json={
                        "model": "deepseek-chat",
                        "messages": [{"role": "user", "content": prompt}],
                        "temperature": 0.7,
                        "max_tokens": 2000
                    })
                if resp.status_code == 200:
                    report = resp.json()["choices"][0]["message"]["content"]
                    st.success("报告生成完成")
                    st.write("---")
                    st.markdown(report)
                else:
                    st.error(f"API错误：{resp.status_code}")
            except Exception as e:
                st.error(f"失败：{e}")
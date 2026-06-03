import streamlit as st
import pandas as pd

st.set_page_config(page_title="骆驼模型排行", page_icon="🐫", layout="wide")
st.title("🐫 银行综合排名（机器学习 + 专家）")

df = pd.read_csv("data/bank_scores.csv", encoding="utf-8-sig")
df["机器学习评分"] = pd.to_numeric(df["机器学习评分"], errors='coerce')
df["专家评分"] = pd.to_numeric(df["专家评分"], errors='coerce')
df["机器学习排名"] = df["机器学习评分"].rank(ascending=False, na_option='bottom')
df["专家排名"] = df["专家评分"].rank(ascending=False, na_option='bottom')

# TOP3
ml_col, ex_col = st.columns(2)
with ml_col:
    st.subheader("🏆 机器学习 TOP3")
    top3 = df.nlargest(3, "机器学习评分")
    c1, c2, c3 = st.columns(3)
    for i, (_, row) in enumerate(top3.iterrows()):
        with [c1, c2, c3][i]:
            st.metric(row.银行, f"{row.机器学习评分:.2f}", f"第{int(row.机器学习排名)}名")

with ex_col:
    st.subheader("🏆 专家评分 TOP3")
    top3 = df.nlargest(3, "专家评分")
    c1, c2, c3 = st.columns(3)
    for i, (_, row) in enumerate(top3.iterrows()):
        with [c1, c2, c3][i]:
            st.metric(row.银行, f"{row.专家评分:.2f}", f"第{int(row.专家排名)}名")

st.divider()
st.subheader("📋 完整排名表")
st.dataframe(
    df.sort_values("机器学习评分", ascending=False)
      .style.format({"机器学习评分": "{:.2f}", "专家评分": "{:.2f}"})
      .background_gradient(subset=["机器学习评分"], cmap="Blues")
      .background_gradient(subset=["专家评分"], cmap="Greens"),
    use_container_width=True
)

# 参考案例折叠
with st.expander("📘 参考：经典CAMEL评价示例"):
    example = pd.read_csv("data/camel_example.csv", encoding="utf-8-sig")
    st.dataframe(example.style.highlight_max(color="#c7f7c7"), use_container_width=True)
import streamlit as st
import pandas as pd
import re

st.set_page_config(page_title="银行基本信息", page_icon="🏢", layout="wide")

# 全局CSS优化页面间距、卡片样式
st.markdown("""
<style>
.block-container{padding:20px 40px !important;}
.income-card{
    background:#f0f7ff;
    padding:18px;
    border-radius:10px;
}
.profit-card{
    background:#f0fff7;
    padding:18px;
    border-radius:10px;
}
.risk-card{
    background:#fcf8ff;
    padding:18px;
    border-radius:10px;
}
th{
    background:#195cad !important;
    color:#fff !important;
    text-align:center !important;
}
td{text-align:center !important;}
</style>
""",unsafe_allow_html=True)

st.title("🏢 上市银行基础档案信息")

# 读取数据
df = pd.read_csv("data/bank_info.csv", encoding="utf-8-sig")
bank_list = df["银行"].tolist()
selected = st.selectbox("🔎 选择需要查看的上市银行", bank_list)

row = df[df["银行"]==selected].iloc[0]

# ==========1、基础信息：删掉card-box卡片，无背景无边框==========
st.subheader("📋 基础工商信息")
base_df = pd.DataFrame({
    "项目":["上市时间","所属行业","主营业务","实际控制人"],
    "内容":[row["上市时间"],row["行业"],row["主营业务"],row["实际控制人"]]
})
st.dataframe(base_df,use_container_width=True,hide_index=True)

# 2.五年财务拆分
def parse_year_data(s):
    res = re.findall(r"(\d{4}):(\d+)",s)
    return pd.DataFrame(res,columns=["年份","金额(亿元)"])

inc_df = parse_year_data(row["五年收入(亿)"])
pro_df = parse_year_data(row["五年毛利(亿)"])

st.subheader("💰 近五年经营财务数据")
c1,c2 = st.columns(2)
with c1:
    st.markdown('<div class="income-card">',unsafe_allow_html=True)
    st.markdown("#### 📈 营业收入明细")
    st.dataframe(inc_df,use_container_width=True,hide_index=True)
    st.markdown('</div>',unsafe_allow_html=True)
with c2:
    st.markdown('<div class="profit-card">',unsafe_allow_html=True)
    st.markdown("#### 🧾 毛利润明细")
    st.dataframe(pro_df,use_container_width=True,hide_index=True)
    st.markdown('</div>',unsafe_allow_html=True)

st.divider()

# 3.经营风险与优势
st.markdown('<div class="risk-card">',unsafe_allow_html=True)
st.subheader("📌 经营现状｜优势与潜在风险")
biz_df = pd.DataFrame({
    "分类":["现存经营问题","核心竞争优势","潜在经营危机"],
    "详情":[row["面临问题"],row["成就"],row["危机"]]
})
st.dataframe(biz_df,use_container_width=True,hide_index=True)
st.markdown('</div>',unsafe_allow_html=True)
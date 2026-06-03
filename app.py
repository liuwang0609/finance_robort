import streamlit as st

st.set_page_config(
    page_title="智能财务机器人｜上市银行双评价分析系统",
    page_icon="🏦",
    layout="wide"
)

# ---------- 全局美化CSS ----------
st.markdown("""
<style>
    .title {
        font-size: 2.6rem;
        font-weight: 700;
        color: #003366;
        text-align: center;
        margin-bottom: 0.3rem;
    }
    .subtitle {
        font-size: 1.1rem;
        color: #555;
        text-align: center;
        margin-bottom: 2rem;
    }
    .box {
        background: #f9f9fb;
        border-radius: 12px;
        padding: 1.5rem;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        margin-bottom: 1rem;
    }
    .card {
        background: linear-gradient(135deg, #eef2f9 0%, #f8f9fc 100%);
        border-radius: 12px;
        padding: 1.2rem;
        text-align: center;
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
    .footer {
        text-align: center;
        color: #888;
        margin-top: 3rem;
        padding-top: 1rem;
        border-top: 1px solid #eee;
    }
</style>
""", unsafe_allow_html=True)

# ---------- 首页 ----------
st.markdown('<div class="title">🏦 智能财务机器人</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">上市银行 CAMELS 双评价分析系统（期末版）</div>', unsafe_allow_html=True)

st.markdown('<div class="box">', unsafe_allow_html=True)
st.markdown("### 📌 项目核心逻辑")
st.markdown("""
- **X变量**：银行CAMELS骆驼评级指标（资本充足、资产质量、管理、盈利、流动性）
- **Y变量**：托宾Q / 股价
- **双评价机制**：
  1. **机器学习**：随机森林特征重要性排序（R²验证）
  2. **专家评判**：财报/研报指标词频统计排序
- **输出**：AI自动生成银行综合分析报告
""")
st.markdown('</div>', unsafe_allow_html=True)

st.write("---")

# 功能卡片
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown('<div class="card"><h3>📊 指标重要性排行</h3><p>机器学习特征权重</p></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="card"><h3>🐫 骆驼模型排行</h3><p>双评分综合排名</p></div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="card"><h3>📈 股价走势</h3><p>近一年股价可视化</p></div>', unsafe_allow_html=True)

col4, col5 = st.columns(2)
with col4:
    st.markdown('<div class="card"><h3>🤖 AI分析报告</h3><p>DeepSeek自动生成</p></div>', unsafe_allow_html=True)
with col5:
    st.markdown('<div class="card"><h3>🏢 银行基本信息</h3><p>概况与经营要点</p></div>', unsafe_allow_html=True)

st.markdown('<div class="footer">请在左侧边栏切换功能模块</div>', unsafe_allow_html=True)
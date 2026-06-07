import streamlit as st
import pandas as pd

st.set_page_config(page_title="指标重要性排行", page_icon="📊", layout="wide")
st.title("📊 指标重要性排行（双评价）")

# --------------------------
# 1. 专家视角数据（组长更新版）
# --------------------------
expert_data = [
    {"指标": "不良贷款率", "专家权重": 0.1919},
    {"指标": "净利差", "专家权重": 0.1296},
    {"指标": "成本收入比", "专家权重": 0.1260},
    {"指标": "流动性比例", "专家权重": 0.0929},
    {"指标": "拨备覆盖率", "专家权重": 0.0652},
    {"指标": "净息差", "专家权重": 0.0651},
    {"指标": "十大客户贷款占比", "专家权重": 0.0589},
    {"指标": "存贷比", "专家权重": 0.0472},
    {"指标": "资产收益率", "专家权重": 0.0460},
    {"指标": "权益资本比", "专家权重": 0.0458},
    {"指标": "网均利润（百万元）", "专家权重": 0.0388},
    {"指标": "人均利润（百万元）", "专家权重": 0.0375},
    {"指标": "核心一级资本充足率", "专家权重": 0.0344},
    {"指标": "资本充足率", "专家权重": 0.0207}
]
df_expert = pd.DataFrame(expert_data).sort_values("专家权重", ascending=False)

# --------------------------
# 2. 机器学习视角（保留原有数据）
# --------------------------
df_ml = pd.read_csv("data/feature_importance.csv", encoding="utf-8-sig")
df_ml = df_ml.sort_values("随机森林重要性", ascending=False)

# --------------------------
# 3. 分栏展示
# --------------------------
left, right = st.columns(2)
with left:
    st.subheader("🖥️ 机器学习视角")
    st.dataframe(
        df_ml.style.bar(subset=["随机森林重要性"], color='#4285F4', vmin=0),
        use_container_width=True, height=500
    )

with right:
    st.subheader("👨‍🏫 专家视角")
    st.dataframe(
        df_expert.style.bar(subset=["专家权重"], color='#e67e22', vmin=0),
        use_container_width=True, height=500
    )

st.divider()
st.caption("📌 机器学习：随机森林特征重要性 | 专家视角：财报指标词频统计；  说明:机器学习权重和专家权重各自独立输出，放在同一份报告中分析。二者方法论不同、不可直接对比，仅供读者从市场逻辑（机器学习）与监管逻辑（专家）两个角度分别参考。两套权重独立计算、并列呈现，差异之处（如机器学习更看重资本充足率，专家更看重资产质量）反映了客观分野。最终结论建议结合两方视角，而非简单平均。）")
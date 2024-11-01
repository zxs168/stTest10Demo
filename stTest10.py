import streamlit as st
import pandas as pd
import numpy as np

# 应用标题
st.title("多列布局和侧边栏筛选应用示例")

# 创建示例数据
np.random.seed(42)
data = pd.DataFrame({
    "类别": np.random.choice(["A", "B", "C"], 100),
    "数值1": np.random.randn(100) * 100,
    "数值2": np.random.randn(100) * 50,
    "数值3": np.random.randn(100) * 30 + 50
})

# 侧边栏筛选选项
st.sidebar.title("筛选选项")

# 类别筛选
category = st.sidebar.multiselect(
    "选择类别",
    options=data["类别"].unique(),
    default=data["类别"].unique()
)

# 数值1的范围筛选
value_range = st.sidebar.slider(
    "数值1的范围",
    min_value=int(data["数值1"].min()),
    max_value=int(data["数值1"].max()),
    value=(int(data["数值1"].min()), int(data["数值1"].max()))
)

# 数据筛选
filtered_data = data[
    (data["类别"].isin(category)) &
    (data["数值1"] >= value_range[0]) &
    (data["数值1"] <= value_range[1])
]

# 显示筛选后的数据和分析
st.header("筛选后的数据展示")

# 多列布局
col1, col2 = st.columns(2)

# 第一列：显示表格
with col1:
    st.subheader("筛选后的数据表")
    st.write(filtered_data)

# 第二列：显示图表
with col2:
    st.subheader("数据统计图")
    st.bar_chart(filtered_data[["数值1", "数值2", "数值3"]])

# 数据描述
st.header("数据描述统计")
st.write(filtered_data.describe())

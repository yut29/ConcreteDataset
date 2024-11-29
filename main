import streamlit as st
import joblib
import numpy as np

# 加载保存的模型
model = joblib.load("random_forest_model.pkl")

# Streamlit 用户输入
st.title("混凝土强度预测")
st.write("输入混凝土的参数进行预测")

# 创建输入框用于输入混凝土参数
cement = st.number_input("水泥含量 (kg)", min_value=0.0, step=1.0)
slag = st.number_input("矿渣含量 (kg)", min_value=0.0, step=1.0)
flyash = st.number_input("粉煤灰含量 (kg)", min_value=0.0, step=1.0)
water = st.number_input("水含量 (kg)", min_value=0.0, step=0.1)
superplasticizer = st.number_input("高效减水剂含量 (kg)", min_value=0.0, step=0.1)
coarseaggregate = st.number_input("粗骨料含量 (kg)", min_value=0.0, step=1.0)
fineaggregate = st.number_input("细骨料含量 (kg)", min_value=0.0, step=1.0)
age = st.number_input("混凝土龄期 (天)", min_value=0.0, step=1.0)

# 创建预测按钮
if st.button("预测"):
    input_data = np.array([[cement, slag, flyash, water, superplasticizer, coarseaggregate, fineaggregate, age]])
    prediction = model.predict(input_data)
    st.write(f"预测的混凝土强度是: {prediction[0]:.2f} MPa")

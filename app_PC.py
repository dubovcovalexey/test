import streamlit as st
import pickle
import numpy as np

model=pickle.load(open("model_saved","rb"))

CreditScore = st.slider('Скоринговый балл', 0, 400)
Geography = st.selectbox('География/регион', ['Минск', 'Брест', 'Могилев'])

Gender = st.selectbox('Пол', ['1', '0'])

Age = st.slider("Возраст", 10, 100)

Tenure = st.selectbox("Стаж", ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15'])

Balance = st.slider("Баланс", 0.00, 10000.00)

NumOfProducts = st.selectbox('Количество продуктов', ['1', '2'])

HasCrCard = st.selectbox("Есть кредитная БПК ?", ['0', '1'])

IsActiveMember = st.selectbox("Активный клиент ?", ['0', '1'])

EstimatedSalary = st.slider("Зарплата", 0.00, 200000.00)


if st.button('Сделать прогноз'):
    output = predict_churn(CreditScore, Geo, Gen, Age, Tenure, Balance, NumOfProducts, HasCrCard, IsActiveMember,
                           EstimatedSalary)
    st.success('Вероятность оттока составляет {}'.format(output))
    st.balloons()

if output >= 0.5:
        print('Клиент уйдет')

else:
        print('Клиент останется')

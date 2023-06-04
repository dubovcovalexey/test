import streamlit as st
import pickle
import numpy as np

model=pickle.load(open("model_saved","rb"))

def predict_churn(CreditScore, Geography, Gender, Age, Tenure, Balance, NumOfProducts, HasCrCard, IsActiveMember, EstimatedSalary):
    input = np.array([[CreditScore, Geography, Gender, Age, Tenure, Balance, NumOfProducts, HasCrCard, IsActiveMember, EstimatedSalary]])
    prediction = model.predict_proba(input)[:, 1] * 100
    return float(prediction)


CreditScore = st.slider('Скоринговый балл', 0, 400)
Geography = st.selectbox('География/регион', ['Минск', 'Брест', 'Могилев'])

Gender = st.selectbox('Пол', ['1', '0'])

Age = st.slider("Возраст", 18, 100)

Tenure = st.slider("Количество лет клиент банка:", 0, 20)

Balance = st.slider("Баланс", 0.00, 10000.00)

NumOfProducts = st.selectbox('Количество продуктов', ['1', '2'])

HasCrCard = st.selectbox("Есть кредитная БПК ?", ['0', '1'])

IsActiveMember = st.selectbox("Активный клиент ?", ['0', '1'])

EstimatedSalary = st.slider("Зарплата", 0.00, 10000.00)


churn_html = """  
              <div style="background-color:#f44336;padding:20px >
               <h2 style="color:red;text-align:center;"> Жаль, но теряем клиента.</h2>
               </div>
            """
no_churn_html = """  
              <div style="background-color:#94be8d;padding:20px >
               <h2 style="color:green ;text-align:center;"> Ура, клиент остаётся в банке !!!</h2>
               </div>
            """

if st.button('Сделать прогноз'):
        output = predict_churn(CreditScore, Geography, Gender, Age, Tenure, Balance, NumOfProducts, HasCrCard, IsActiveMember, EstimatedSalary)
        st.success('Вероятность оттока составляет {}'.format(output))
        st.balloons()

        if output >= 50:
            st.markdown(churn_html, unsafe_allow_html= True)

        else:
            st.markdown(no_churn_html, unsafe_allow_html= True)

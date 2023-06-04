import streamlit as st
import pickle
import numpy as np

def predict_churn(CreditScore, Geography, Gender, Age, Tenure, Balance, NumOfProducts, HasCrCard, IsActiveMember, EstimatedSalary):
    input = np.array([[CreditScore, Geography, Gender, Age, Tenure, Balance, NumOfProducts, HasCrCard, IsActiveMember, EstimatedSalary]])
    prediction = model.predict_proba(input)
    pred = '{0:.{1}f}'.format(prediction[0][0], 2)
    return float(pred)

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
        output = predict_churn(CreditScore, Geo, Geography, Age, Tenure, Balance, NumOfProducts, HasCrCard, IsActiveMember, EstimatedSalary)
        st.success('Вероятность оттока составляет {}'.format(output))
        st.balloons()

        if output >= 0.5:
            st.markdown(churn_html, unsafe_allow_html= True)

        else:
            st.markdown(no_churn_html, unsafe_allow_html= True)

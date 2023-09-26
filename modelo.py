import streamlit as st
import numpy as np 
import pandas as pd 
import pickle
from catboost import CatBoostRegressor 
import sklearn 



st.title("modelo - actividad 26 de septiembre")
st.divider()
st.write("ingrese los datos")

assess=st.slider("assess", 0,20)
bedrooms=st.slider("bdrms", 0,30)
lotsize=st.slider("lotsize", 0,35)
square_fit=st.slider("sqrft", 0,20)
colonial=st.slider("colonial", 0,1)

with open ("model.pickle","rb") as doc:
    model=pickle.load(doc)

prediction=model.predict(np.array([[assess,bedrooms,lotsize,square_fit,colonial]]))
if st.button("predecir"):
    st.write(f"El precio del inmueble es {prediccion[0]}")

    
                                               
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 08:17:17 2022

@author: vishn
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 19:32:28 2022

@author: vishn
"""

import pickle
import streamlit as st
import numpy as np
import pandas as pd
#from flask import jsonify
import json




#loding the saved model
house_price=pickle.load(open('banglr_model.pkl','rb'))



#silde bar for navigation


page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://i.pinimg.com/originals/7b/01/e6/7b01e6ddedddc9d10b24e7b73a06fd1a.gif");
background-size: 180%;
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
}}
[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}
[data-testid="stToolbar"] {{
right: 2rem;
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

__locations=None
__data_columns=None
__model=None 
with open("columns.json") as f:
        __data_columns=json.load(f)['data_columns']
        __location=__data_columns[3:]
                 
 
data=pd.read_csv('Bengaluru_House_Data.csv') 
loc=data['location'].unique()
    
  
  
def house_prices(location,sqt,bhk,bath):
      try:
          loc_index=__data_columns.index(location.lower())
      except:
          loc_index = -1
          
          
      
     # loc_index = np.where(X.columns==location)[0][0]
      x = np.zeros(243)
      x[0] = sqt
      x[1] = bath
      x[2] = bhk
  
      if loc_index >=0:
        x[loc_index] = 1
        
      return round(house_price.predict([x])[0],3)
   
  
  

    
'''-------------------------------------------------------------------''' 
def main():
    st.title('Hi Welcome to Bangalore')
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Banglore House Price Prediction </h2>
    </div>
   
     """
    st.markdown(html_temp,unsafe_allow_html=True)
   
    location=st.selectbox('Enter the location',loc)    
    sqt=st.text_input("Enter the squrefeet")
    bath=st.text_input("Enter the number of Bathroom")
    bhk=st.text_input("Enter the number of BHK")
    result=''
   
    if st.button('House Price in laks'):
       
       result= house_prices(location,sqt,bhk,bath)
    st.success("The Final Price in INR {} \-".format(result))
    
    
if __name__=='__main__':
    main()    
    
    
   
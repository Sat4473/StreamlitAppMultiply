# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 20:02:32 2022

@author: 
"""

import streamlit as st

st.write( ''' Multiplication of two numbers ''')

st.header('User inputs')

def user_inputs():
    num1 = st.number_input("Number")
    num2 = st.number_input("multiplier")
    
    return (num1*num2)

num = user_inputs()
    
st.write(num)    

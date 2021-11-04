import streamlit as st


import pandas as pd
import numpy as np

import os
import joblib
import hashlib

import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("Agg")


#import database py file for db functions
from manage_db import *


#function to hash password
def hash_password(password):
    return hashlib.sha256(str.encode(password)).hexdigest()

#function to verify hashed password
def verify_hashPass(password,hashed_text):
    if hash_password(password) == hashed_text:
        return hashed_text
    else:
        return False


feature_names = ['age', 'sex', 'steroid', 'antivirals', 
'fatigue', 'spiders', 'ascites','varices', 'bilirubin',
'alk_phosphate', 'sgot', 'albumin', 'protime','histology']


gender_dict = {"Male":1,"Female":2}
feature_dict = {"No":1,"Yes":2}

def get_value(val,my_dict):
    for key,value in my_dict.items():
        if val == key:
            return value

def get_key(val,my_dict):
    for key,value in my_dict.items():
        if val == key:
            return key


def get_feat_value(val):
    feat_dict = {"No":1,"Yes":2}
    for key,value in feat_dict.items():
        if val == key:
            return value


def load_model(model_file):
    loaded_model = joblib.load(open(os.path.join(model_file),"rb"))
    return loaded_model

'''
Main mortality prediction app
'''

def main():
    st.title("Disease Mortality prediction app")

    menu = ["Home","Login","Signup"]
    subMenu = ["Plot","Prediction","Metrics"]

    choice = st.sidebar.selectbox("Menu",menu)

    if choice == "Home":
        st.subheader("Home")
        st.text("What is Hepatitis?")

    elif choice == "Login":
        username = st.sidebar.text_input("username")
        password = st.sidebar.text_input("Password",type="password")

        if st.sidebar.checkbox("Login"):


            create_usertable()
            hashed_passwd = hash_password(password)

            #login_user from manage_db
            #verifying new password
            result = login_user(username,verify_hashPass(password,hashed_passwd))


            if result:
                st.success(f"Welcome {username}")
                activity = st.selectbox("Activity",subMenu)

                if activity == "Plot":
                    st.subheader("Data vs Plot")
                    df = pd.read_csv("data/clean_hepatitis_dataset.csv")

                    st.dataframe(df)

                    #frequency distribution plot

                    freq_df = pd.read_csv("data/freq_df_hepatitis_dataset.csv")
                    st.bar_chart(freq_df["count"])



                    if st.checkbox("Area Chart"):
                        all_columns = df.columns.to_list()

                        feat_choices = st.multiselect("Choose Another Feature",all_columns)

                        new_df = df[feat_choices]
                        st.area_chart(new_df)


                    #plot differnt number of objects in each class
                    df["class"].value_counts().plot(kind="bar")
                    st.pyplot()





                elif activity == "Prediction":
                    st.subheader("predictive analysis")

                    age =st.number_input("Age",10,80)

                    gender = st.radio("Sex",tuple(gender_dict.keys()))
                    
                    fatigue = st.radio("Do You Have Fatigue",tuple(feature_dict.keys()))

                    steroid = st.radio("Do you take Steriods?",tuple(feature_dict.keys()))

                    anitvirals = st.radio("Do you take Antivirals?",tuple(feature_dict.keys()))

                    spiders = st.radio("Presence of Spider Naevi??",tuple(feature_dict.keys()))
                    ascites = st.radio("Do you have Ascites",tuple(feature_dict.keys()))

                    varices = st.radio("Presence of Varices",tuple(feature_dict.keys()))
                    bilirubin = st.number_input("bilirubin Content",0.0,8.0)
                    

                    alk_phosphate = st.number_input("Alkaline Phosphate Content",0.0,296.0)

                    sgot = st.number_input("Sgot",0.0,648.0)

                    albumin = st.number_input("Albumin",0.0,6.4)

                    protime = st.number_input("Prothrombin Time",0.0,100.0)

                    histology = st.radio("Histology",tuple(feature_dict.keys()))

                    feature_list = [age,get_value(gender,gender_dict),get_feat_value(steroid),get_feat_value(anitvirals),get_feat_value(fatigue),get_feat_value(spiders),get_feat_value(ascites),get_feat_value(varices),bilirubin,alk_phosphate,sgot,albumin,int(protime),get_feat_value(histology)]


                    #st.write(feature_list)
                    st.write("Final Results from User: ")
                    result_new = {"Age":age,"Gender":gender,"Steroid":steroid,"Antivirals":anitvirals,"Fatigue":fatigue,"Spiders Naevi":spiders,"Ascites":ascites,"Varices":varices,"Bilirubin":bilirubin,"Alk_phosphate":alk_phosphate,"Sgot":sgot,"Albumin":albumin,"Protime":protime,"Histolog":histology}
                    st.json(result_new)


                    single_sample = np.array(feature_list).reshape(1,-1)


                    model_choice = st.selectbox("Select Model",["LR","KNN","DecisionTree"])

                    if st.button("Prediction"):
                        if model_choice == "KNN":
                            loaded_model = load_model("models/knn_hepB_model.pkl")

                            prediction = loaded_model.predict(single_sample)

                            st.write(prediction)


            
            else:
                st.warning("Incorrect password/username")

    elif choice == "Signup":
        new_username = st.text_input("Username")
        new_password = st.text_input("Password",type='password')

        confirm_password = st.text_input("Confirm Password",type="password")
        if confirm_password == new_password:
            st.success("Password confirmed")
        else:
            st.warning("Password is incorrect")
        
        if st.button("Submit"):
            create_usertable()
            hashed_new_password = hash_password(new_password)
            add_userdata(new_username,hashed_new_password)

            st.success("You have created an account")

            st.info("Login to get started")





if __name__ == "__main__":
    main()

print("\nWorking...\n")
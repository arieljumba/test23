
import streamlit as st
import streamlit_authenticator as stauth
from deta import Deta

st.title('connect db')

deta = st.secrets["DETA_KEY"]

#create a database
db = deta.Base("users_db")

def insert_user(username,name, role, password):
    #returns user on a succesful creation otherwise raises an error
    return db.put({"key":username,"name": name, "role": role,"password":password})



#import database as db

usernames = st.text_input('username')
names = st.text_input('name')
roles = st.selectbox('roles', options = ("admin","inputter"))
passwords = st.text_input('password')
hashed_passwords = stauth.Hasher(passwords).generate()

if st.button(label='add'):
    for (username,name, role, hashed_password) in zip(usernames, names, roles, hashed_passwords):
        insert_user(username,name,role,hashed_password)

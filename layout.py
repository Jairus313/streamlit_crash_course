# importing library.
import streamlit as st


fname, mname, lname = st.columns(3)

with fname:
    st.text_input("Enter First Name")

with mname:
    st.text_input("Enter Middle Name")

with lname:
    st.text_input("Enter Last Name")

st.text_input("Enter Email")

psswd, repsswd = st.columns(2)

with psswd:
    st.text_input("Enter Password", type="password")

with repsswd:
    st.text_input("Re-Enter Password", type="password")

dob, gender = st.columns(2)

with dob:
    st.date_input("Enter Date of birth")

with gender:
    st.selectbox(
     'Select the Gender',
     ['Select', 'Male', 'Female', 'Rather not to select'], index=0)


st.text_area("Enter the Address 1")

st.text_input("Enter the Address 2")

st.text_input("Enter the Landmark")

state, pin_code = st.columns(2)

with state:
    st.text_input("Enter State name")

with pin_code:
    st.text_input("Enter Pin code")

st.checkbox("I agree with all terms and conditions*")

_, _, button, _, _ = st.columns(5)


with button:
    st.button('sign in')

st.markdown("***")


_, msg, _ = st.columns(3)

with msg:
    st.markdown("### Already an user?")

_, login, glogin,  _ = st.columns(4)

with login:
    st.button("Login with Credentials")

with glogin:
    st.button("Login with Google Account")
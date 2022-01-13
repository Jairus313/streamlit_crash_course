# importing library.
import streamlit as st


# button.
if st.button("Demo Button"):
    st.write("# Hola HUGE TTEEXXTTSSS :joy:.")

# text input. 
name = st.text_input("what's your made name?")

if name:
    st.write("Oh, I see! That's your made up name **{0}**".format(name))

# text area.
text_area = st.text_area("How you felt? When you got Spiderman:No way home's spoilers:smirk:")

if text_area:
    st.write(text_area)


# check box.
if st.checkbox("Do you agree with this without reading it?"):
    st.write("son of gun, I'm in.!!")

# with defualt value.
if st.checkbox("Uncheck this one, If you think HTML is not programming language?", value=True):
    st.write("Really Bro.!?")
else:
    st.write("Now We cool")

# radio button
radio = st.radio("Choose one", ["Tobey Maguire", "Andrew Garfield", "Tom Holland", "Dialemma!?"], index=3)

if radio and radio == "Tobey Maguire":
    st.write("The OG Fan ah!")
elif radio and radio == "Andrew Garfield":
    st.write("ngl he is amazing too!")
elif radio and radio == "Tom Holland":
    st.write("This kid got a heart!")
else:
    st.write("Select one bro, quick..!!")


# selectbox
option = st.selectbox(
     'Most popular programming language for 2022?',
     ['Python', 'JavaScript', 'GO', 'C++'], index=0)

st.write('You selected:', option)


# multiselect
st.multiselect('select anything', ['a', 'b', 'c'])


# slider
slider = st.slider('sliders', min_value=-10, max_value=10, value=0, step=2)

if slider > 0:
    st.write("#### %d"%slider)


# file upload.
file_name = st.file_uploader("upload here")

if file_name:
    if file_name.type == "image/jpeg" or file_name.type == "image/png" or file_name.type == "image/jpg":
        st.image(file_name)

    elif file_name.type == "audio/mpeg":
        st.audio(file_name)

    elif file_name.type == "video/mp4":
        st.video(file_name)

    else:
        st.write(file_name)
# importing library.
import streamlit as st


# sidebar.
side_bar = st.sidebar.button("Demo Button")

if side_bar:
    st.write("# You just clicked the button on side bar.")


name = st.sidebar.text_input("what's your made name?")

if name:
    st.write("# you entered _%s_."%name)

text_area = st.sidebar.text_area("How you felt? When you got Spiderman:No way home's spoilers:smirk:")

if text_area:
    st.write(text_area)

if st.sidebar.checkbox("Do you agree with this without reading it?"):
    st.write("son of gun, I'm in.!!")

if st.sidebar.checkbox("Uncheck this one, If you think HTML is not programming language?", value=True):
    st.write("Really Bro.!?")
else:
    st.write("Now We cool")

radio = st.sidebar.radio("Choose one", ["Tobey Maguire", "Andrew Garfield", "Tom Holland", "Dialemma!?"], index=3)

if radio and radio == "Tobey Maguire":
    st.write("The OG Fan ah!")
elif radio and radio == "Andrew Garfield":
    st.write("ngl he is amazing too!")
elif radio and radio == "Tom Holland":
    st.write("This kid got a heart!")
else:
    st.write("Select one bro, quick..!!")

option = st.sidebar.selectbox(
     'Most popular programming language for 2022?',
     ['Python', 'JavaScript', 'GO', 'C++'], index=0)

st.write('You selected:', option)

st.sidebar.multiselect('select anything', ['a', 'b', 'c'])

slider = st.sidebar.slider('sliders', min_value=-10, max_value=10, value=0, step=2)

if slider > 0:
    st.write("#### %d"%slider)


file_name = st.sidebar.file_uploader("upload here")

if file_name:
    if file_name.type == "image/jpeg" or file_name.type == "image/png" or file_name.type == "image/jpg":
        st.image(file_name)

    elif file_name.type == "audio/mpeg":
        st.audio(file_name)

    elif file_name.type == "video/mp4":
        st.video(file_name)

    else:
        st.write(file_name)
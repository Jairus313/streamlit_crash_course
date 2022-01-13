# importing library.
import streamlit as st
import time


# success message.
st.success("Success in Green")

# info message.
st.info("Info in Blue")

# warning message.
st.warning("Warning in Yellow")

# error message.
st.error("Error in Red")

# exception message is interesting one.
try:
    print(some_undefined_variable)
except Exception as e:
    st.exception(e)

# progress bar.
progress_bar = st.progress(0)

for i in range(100):
    time.sleep(0.25)
    progress_bar.progress(i+1)

# this one is really bonus.
st.write("### Balloonssss")
st.balloons()

# spinner.
with st.spinner('spinner for 5 secs..'):
    time.sleep(5)

st.success('### Done!')
st.write("### Again Balloonssss :joy:")
st.balloons()
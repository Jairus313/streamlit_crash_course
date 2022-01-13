# importing library.
import streamlit as st
import pandas as pd
import numpy as np

# to print anything using write.
st.write(1234)

st.write("# Can be used as markdown too.")

st.write("sum of two values", 2+2)

# can display the arrays too.
data = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                   columns=['a', 'b', 'c'])

st.write("before the dataframe", data, "after the dataframe")
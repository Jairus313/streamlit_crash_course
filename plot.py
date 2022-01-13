# importing library.
import streamlit as st
import pandas as pd
import numpy as np


# line chart
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)


# area chart
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.area_chart(chart_data)

# bar chart
chart_data = pd.DataFrame(
     np.random.randn(50, 3),
     columns=["a", "b", "c"])

st.bar_chart(chart_data)

# flow chart
st.graphviz_chart('''
    digraph {
        start_new_project -> plan_to_learn_new_skills
        plan_to_learn_new_skills -> too_many_skills_to_learn
        too_many_skills_to_learn -> abandon_the_project 
        abandon_the_project -> start_another_new_project
        start_another_new_project -> plan_to_learn_new_skills
        plan_to_learn_new_skills -> accidently_learn_all_those_new_skills
        accidently_learn_all_those_new_skills -> complete_the_project
        complete_the_project -> open_source_the_project
    }
''')
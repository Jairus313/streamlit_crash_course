# importing library.
import streamlit as st
import pandas as pd
import numpy as np



# dataframe.
# values in 2D array with column name.
df = pd.DataFrame(
        np.array([["Sudeep Nellur", "Machine Learning Engineer", "https://sudeepnellur.tech/"]]),
        columns=("Name", "Desgination", "Portfolio"))

st.dataframe(df)

df = pd.DataFrame(
    np.random.randn(10, 10),
    columns=('col %d' % i for i in range(10)))

st.dataframe(df)

# tables.
# in table everything will be displayed
st.table(df)

# some cool metric.
st.metric(label="Petrol", value="100 ₹", delta="+10%")

# some json too.
st.json({
	"id": "0001",
	"type": "donut",
	"name": "Cake",
	"ppu": 0.55,
	"batters":
		{
			"batter":
				[
					{ "id": "1001", "type": "Regular" },
					{ "id": "1002", "type": "Chocolate" },
					{ "id": "1003", "type": "Blueberry" },
					{ "id": "1004", "type": "Devil's Food" }
				]
		},
	"topping":
		[
			{ "id": "5001", "type": "None" },
			{ "id": "5002", "type": "Glazed" },
			{ "id": "5005", "type": "Sugar" },
			{ "id": "5007", "type": "Powdered Sugar" },
			{ "id": "5006", "type": "Chocolate with Sprinkles" },
			{ "id": "5003", "type": "Chocolate" },
			{ "id": "5004", "type": "Maple" }
		]
})
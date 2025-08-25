import openpyxl
import json
import pandas as pd
from datetime import datetime
import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials


scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]


creds_dict = dict(st.secrets['gsread'])
creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)

print(creds_dict)


# client = gspread.authorize(creds)
# sheet = client.open('Choco_primo_database').sheet1


# st.title('Choco Primo Activation')

# st.markdown("🧠 Behavioral Prompt")

# # Load Data
# outlets = pd.read_excel('data.xlsx', sheet_name='outlets')
# products = pd.read_excel('data.xlsx', sheet_name='products')

# # Chain selection
# selected_chain = st.selectbox('Select Chain', outlets['Chain'].unique())
# filtered_outlets = outlets[outlets['Chain']==selected_chain]
# selected_outlet = st.selectbox('Select Outlet', sorted(filtered_outlets['Outlets'].unique()))


# # Category Selection
# selected_category = st.selectbox("Select Category", products['Category'].unique())
# filtered_products = products[products['Category']== selected_category]
# selected_product = st.selectbox('Select Product', filtered_products['Product'].unique())

# activation_date = st.date_input('Select Activation Date')


# # Sales

# sales = st.number_input("Enter Sales (in Pieces)", min_value=0, step=1, format="%d")
# timestamp = activation_date
# row = []

# if sales <= 0:
#     st.warning("Sales can't be zero")
# else:
#     row.extend([
#         timestamp,
#         selected_chain,
#         selected_outlet,
#         selected_product,
#         selected_category,
#         sales
#     ])

# # buttons
#     if st.button("Submit Activation"):
#         sheet.append_row(row)
#         st.success(f"Recorded {sales} pieces of {selected_product} at {selected_outlet} on {timestamp}")


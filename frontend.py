import streamlit as st
import pandas as pd
import sqlite3
from streamlit_dynamic_filters import DynamicFilters


st.title("OCR Project")
st.title("The Expense Tracker Through Bills")

DB_NAME = "ocr_master_table.db"
TABLE_NAME = "ocr_line_items"

def load_data():
    try:
        con = sqlite3.connect(DB_NAME)
        df = pd.read_sql_query(f"Select * from {TABLE_NAME}", con)
        con.close()
        return df
    
    except sqlite3.Error as e:
        st.error(f"Error Loading data from database: {e}")
        return pd.DataFrame()
    
    except Exception as e:
        st.error(f"An unexpected error occured: {e}")
        return pd.DataFrame()


data_df = load_data()


filters_obj =DynamicFilters(
    data_df,
    filters = ["Category", "Invoice_No"]
)

with st.sidebar:
    st.header("filter Expenses")
    filters_obj.display_filters()



st.dataframe(filters_obj.filter_df(),use_container_width=True)

    


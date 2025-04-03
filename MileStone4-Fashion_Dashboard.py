import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Load data with caching to improve performance
@st.cache_data
def load_data():
    file_path = "C:/Users/sriya/OneDrive/Desktop/Fashion_Sales_Cleaned.xlsx"
    df = pd.read_excel(file_path)
    
    # Clean column names
    df.columns = df.columns.str.strip()

    # Convert Date column to datetime
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

    # Remove negative values in Amount column
    df = df[df['Amount'] > 0]

    # Define mappings
    mappings = {
        'Gender': {0: "Male", 1: "Female"},
        'Channel': {0: "Myntra", 1: "Ajio", 2: "Amazon", 3: "Flipkart", 4: "Meesho", 5: "Nalli", 6: "Others"},
        'Category': {0: "Kurta", 1: "Top", 2: "Set", 3: "Dress", 4: "Shirt", 5: "Trousers", 6: "Jeans", 7: "Jacket"},
    }

    # Apply mappings
    for col, mapping in mappings.items():
        df[col] = df[col].map(mapping)

    # Define realistic price ranges for each category
    category_price_mapping = {
        "Kurta": (500, 800),
        "Top": (300, 600),
        "Set": (700, 1200),
        "Dress": (800, 1500),
        "Shirt": (400, 800),
        "Trousers": (600, 1200),
        "Jeans": (1000, 2000),
        "Jacket": (1200, 2500),
    }

    # Replace abnormal values using vectorized operations
    df['Amount'] = np.where(
        df['Amount'] < 50,
        df['Category'].map(lambda x: np.random.randint(*category_price_mapping.get(x, (300, 1000)))),
        df['Amount']
    )

    return df

df = load_data()

# Sidebar Filters with Cached Unique Values
st.sidebar.header("Filters")

gender_options = df['Gender'].dropna().unique()
channel_options = df['Channel'].dropna().unique()
category_options = df['Category'].dropna().unique()

gender_filter = st.sidebar.multiselect("Select Gender:", gender_options, default=gender_options, key="gender_filter")
channel_filter = st.sidebar.multiselect("Select Channel:", channel_options, default=channel_options, key="channel_filter")
category_filter = st.sidebar.multiselect("Select Category:", category_options, default=category_options, key="category_filter")

# Apply filters using query (faster than multiple conditions)
df_filtered = df.query("Gender in @gender_filter and Channel in @channel_filter and Category in @category_filter")

# Dashboard Title
st.title("📊 Fashion Sales Dashboard")

# Total Sales Overview
total_revenue = df_filtered['Amount'].sum()
total_orders = len(df_filtered)  # More efficient than shape[0]
avg_order_value = total_revenue / total_orders if total_orders else 0

st.metric("Total Revenue (INR)", f"{total_revenue:,.0f}")
st.metric("Total Orders", f"{total_orders}")
st.metric("Average Order Value", f"{avg_order_value:,.0f}")

# Orders by Month
monthly_sales = df_filtered.resample('M', on='Date').agg({'Amount': 'sum'}).reset_index()
monthly_sales['Date'] = monthly_sales['Date'].dt.strftime('%Y-%m')

fig1 = px.line(monthly_sales, x='Date', y='Amount', title="Monthly Sales Trend")
st.plotly_chart(fig1)

# Top Categories
category_sales = df_filtered.groupby('Category', as_index=False)['Amount'].sum()
fig2 = px.bar(category_sales, x='Category', y='Amount', title="Top Selling Categories", color='Category')
st.plotly_chart(fig2)

# Revenue Distribution
fig3 = px.histogram(df_filtered, x='Amount', nbins=50, title="Revenue Distribution")
st.plotly_chart(fig3)

# Sales by Gender
gender_sales = df_filtered.groupby('Gender', as_index=False)['Amount'].sum()
fig4 = px.pie(gender_sales, names='Gender', values='Amount', title="Sales by Gender")
st.plotly_chart(fig4)

# Sales by Channel
channel_sales = df_filtered.groupby('Channel', as_index=False)['Amount'].sum()
fig5 = px.bar(channel_sales, x='Channel', y='Amount', title="Sales by Channel", color='Channel')
st.plotly_chart(fig5)

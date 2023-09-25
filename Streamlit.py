import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px




def space(n,element): # n: number of lines
    for i in range(n):
        element.write("")

# html command for a red line
red_line="""<hr style="height:4px;border:none;color:#DC143C;background-color:#DC143C;"/>"""

# html commnad for a grey line
grey_line="""<hr style="height:1px;border:none;no shade;"/>"""

# Setting page layout
st.set_page_config(layout='wide')

# Loading Dataset
df = pd.read_csv("https://raw.githubusercontent.com/Mohammad-Ayoub/Streamlit/main/Largest_Companies.csv")

# MSBA Logo
html_string = '''<!DOCTYPE html>
<html>
<body>
 <a href="https://www.aub.edu.lb/osb/MSBA/Pages/default.aspx">
  <img src="https://www.aub.edu.lb/osb/research/Darwazah/PublishingImages/OSB%20Stamp%20color-MSBA.png" width=300" height="80" />
 </a>
</body>
</html>'''
st.sidebar.markdown(html_string, unsafe_allow_html=True)
space(4,st.sidebar)

# My name and professor's name
st.sidebar.subheader("Done by Mohammad Hussein Ayoub")
st.sidebar.subheader("Professor [Fouad Zablith](https://www.aub.edu.lb/pages/profile.aspx?memberId=fz13)")




# Create a Streamlit app
st.title('Top Companies by Revenue')

# Interactive Dropdown for Industry Selection
selected_industry = st.selectbox('Select an Industry:', df['Industry'].unique())

# Interactive Slider for Number of Companies
num_companies = st.slider('Select the Number of Companies to Display:', 1, 10, 5)

# Filter the DataFrame based on the selected industry
filtered_df = df[df['Industry'] == selected_industry]

# Sort the filtered DataFrame by Revenue in descending order to get the top companies
df_sorted = filtered_df.sort_values(by='Revenue (USD millions)', ascending=False)

# Select the top N companies based on the user's choice
top_companies = df_sorted.head(num_companies)

# Reverse the order to show the top company at the top of the chart
top_companies = top_companies.iloc[::-1]

# Create a bar chart using Plotly Express
fig = px.bar(top_companies, x='Name', y='Revenue (USD millions)', color='Industry',
             title=f'Top {num_companies} {selected_industry} Companies by Revenue',
             labels={'Name': 'Company Name', 'Revenue (USD millions)': 'Revenue (Millions USD)'})

# Display the chart in the Streamlit app
st.plotly_chart(fig)

# Create a Streamlit app
st.title("Top Companies Analysis")

# Interactive Dropdown for Color Scale
color_scale_options = ['viridis', 'plasma', 'inferno', 'magma', 'cividis']
selected_color_scale = st.selectbox("Select Color Scale:", color_scale_options)

# Interactive Checkbox for Data Filtering (e.g., by Industry)
selected_industries = st.multiselect("Select Industries to Filter:", df['Industry'].unique())

# Filter the DataFrame based on selected industries
filtered_df = df[df['Industry'].isin(selected_industries)] if selected_industries else df

# Create the bar chart using Plotly Express with the selected color scale
fig = px.bar(filtered_df, x="Name", y='Rank', color='Industry', color_continuous_scale=selected_color_scale,
             title="Examining the ranking and industry of top companies")

# Display the chart in the Streamlit app
st.plotly_chart(fig)

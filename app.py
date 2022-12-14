import streamlit as st
import numpy as np
import pandas as pd
import time  # to simulate a real time data,time loop
import plotly.express as px  # interactive charts

## reading csv from url

df = pd.read_csv("https://raw.githubusercontent.com/Lexie88rus/bank-marketing-analysis/master/bank.csv")

## Setup configurations

st.set_page_config(
    page_title="Real-Time Data Science Dashboard",  # used for seo purpose
    layout='wide'  # full screen and other option can be narrow
)

# dashboard title
st.title("Real-Time / Live Data Science Dashboard")

# top-level filters
job_filter = st.sidebar.selectbox("Select the Job", pd.unique(df['job']))

# creating a single-element container.
placeholder = st.empty()
# inserts a container for single element.Replacing the components but user will be seeing as a real time change
## location will not be changed but the changes the element within the location. Need to be careful.

# dataframe filter
df = df[df['job'] == job_filter]  ## filtering the table frame

## As this is static data and need to tell users that this is dynamic, we are muliplying age with random
## number and adding it to new column and adding for loop to iterate for 200 times.
# near real-time / live feed simulation
for seconds in range(200):
    # while True:
    df['age_new'] = df['age'] * np.random.choice(range(1, 5))
    df['balance_new'] = df['balance'] * np.random.choice(range(1, 5))

     # creating KPIs
    avg_age = np.mean(df['age_new'])

    count_married = int(df[(df["marital"] == 'married')]['marital'].count() + np.random.choice(range(1, 30)))

    balance = np.mean(df['balance_new'])

    # create three columns
    with placeholder.container():
        kpi1, kpi2, kpi3 = st.columns(3)

    # fill in those three columns with respective metrics or KPIs
    kpi1.metric(label="Age ⏳", value=round(avg_age), delta=round(avg_age) - 10)
    ##delta is difference, +ve and -ve with color
    kpi2.metric(label="Married Count 💍", value=int(count_married), delta=- 10 + count_married)
    kpi3.metric(label="A/C Balance ＄", value=f"$ {round(balance, 2)} ", delta=- round(balance / count_married) * 100)

    # create two columns for charts

    fig_col1, fig_col2 = st.columns(2)
    with fig_col1:
        st.markdown("### First Chart")
        fig = px.density_heatmap(data_frame=df, y='age_new', x='marital')
        st.write(fig)
    with fig_col2:
        st.markdown("### Second Chart")
        fig2 = px.histogram(data_frame=df, x='age_new')
        st.write(fig2)
        st.markdown("### Detailed Data View")
        st.dataframe(df)
        time.sleep(1)
    # placeholder.empty()

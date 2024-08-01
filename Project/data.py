import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

@st.cache_data
def load_data():
    df=pd.read_csv("Placement_Data_Full_Class.csv")
    df.head()
    df.info()
    df.describe()
    df['status']
    p=df[['degree_p','etest_p']].describe()
    p
    plt.title("Average Academic Point vs Employbility Test Point")
    plt.plot(p.degree_p.iloc[1:8],label='Average Academic Point')
    plt.ylabel("Points")
    plt.plot(p.etest_p.iloc[1:8],label='Employbility Test Point')
    plt.legend()
    df = df.set_index('status')
    df.head()
    d=df['specialisation']
    d
    df.columns
    placed=df.loc['Placed']
    placed
    print(f'Number of students placed: {placed}')
    plt.figure(figsize=(100,60))
    placed.plot(kind='line')
    plt.title('Number of Students Placed')
    plt.xlabel('Placed')
    plt.ylabel('Package')
    plt.show()
    gen=df.groupby('gender').value_counts()
    print(f'No of students placed and not placed in each gender:\n{gen}\n')
    gen=df.gender.value_counts(normalize=True)*100
    plt.title('Gender Distribution in Campus')
    lb=['Male','Female']
    print(plt.pie(gen,labels=lb,autopct='%.0f%%'))
    plt.title("Statistics of Various Academic Points")
    plt.ylabel("Points")
    plt.plot(df[['ssc_p','hsc_p','degree_p','mba_p','etest_p']].iloc[0],label='Female')
    plt.plot(df[['ssc_p','hsc_p','degree_p','mba_p','etest_p']].iloc[1],label='Male')
    plt.legend()
    special=df.groupby('specialisation').value_counts(normalize=True)*100
    print(f'Placement Stats Of Different Specialisations:\n{special}\n')
    p_s=df.loc['Placed']['specialisation']
    p_s
    spc=df.specialisation.value_counts(normalize=True)*100
    spc.plot(kind='pie')
    work_experience=df.groupby('workex').value_counts(normalize=True)*100
    print(f'Percentage students placed and not placed based their work experience:\n{work_experience}')
    work=df.workex.value_counts(normalize=True)*100
    work.plot(kind='bar',xlabel=['work experience'])
    df.sl_no=df.sl_no.astype(str)
    mfe=df[df.specialisation=='Mkt&Fin'].nlargest(10,'etest_p')
    plt.plot(mfe.sl_no,mfe.etest_p,"o-c")
    plt.title('Top Scores of Employbility test for Marketing & Finance');
    plt.xlabel('Id of student');
    plt.ylabel('Score');
    plt.figure(figsize=(8, 6))
    plt.plot(df.ssc_p)
    plt.title('SSC Percentage by Placement Status')
    plt.xlabel('Placement Status')
    plt.ylabel('SSC Percentage')
    plt.show()
    plt.figure(figsize=(7,6))
    plt.pie(df['workex'].value_counts(),labels=['yes','no'],startangle=90,autopct='%.1f%%')
    plt.title("Pie Chart of Work experience")
    plt.show()
    plt.figure(figsize=(10, 6))
    plt.hist(data=df, x='salary', bins=20, color='green')
    plt.title('Distribution of Salary for Placed Students')
    plt.show()
    plt.figure(figsize=(12,6))
    df.plot(kind='line',color='blue')
    plt.title("Status - Count", fontsize=16)
    return df

st.set_page_config(
layout='wide',
page_title='Immigration Data Analysis',
page_icon='@',
)

with st.spinner('Loading data...'):
    df=load_data()
    st.sidebar.success('Data Loaded Successfully!!!')

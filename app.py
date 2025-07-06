import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

st.set_page_config(page_title="Marketing Data Dashboard", layout="wide")

st.title("Marketing Data Analysis Dashboard")

uploaded_file = st.file_uploader("Upload marketing_data.csv", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    
    df.columns = df.columns.str.strip()
    df['Income'] = df['Income'].str.replace(r'[\$,]', '', regex=True).astype(float)
    df['Dt_Customer'] = pd.to_datetime(df['Dt_Customer'], format='%m/%d/%y')
    df['Income'] = df.groupby(['Education', 'Marital_Status'])['Income'].transform(lambda x: x.fillna(x.mean()))

    df['Education'] = df['Education'].replace({
        '2n Cycle': 'Master',
        'Basic': 'High School',
        'Graduation': 'Graduate',
        'PhD': 'PhD',
        'Master': 'Master'
    })
    df['Marital_Status'] = df['Marital_Status'].replace({
        'Together': 'Married',
        'Alone': 'Single',
        'Absurd': 'Other',
        'YOLO': 'Other',
        'Divorced': 'Divorced',
        'Widow': 'Widow',
        'Single': 'Single',
        'Married': 'Married'
    })

    df['Age'] = 2025 - df['Year_Birth']
    df['Customer_Since'] = (pd.Timestamp.now() - df['Dt_Customer']).dt.days
    df['Total_Children'] = df['Kidhome'] + df['Teenhome']
    df['Total_Spending'] = df[['MntWines', 'MntFruits', 'MntMeatProducts','MntFishProducts', 'MntSweetProducts', 'MntGoldProds']].sum(axis=1)
    df['Total_Purchases'] = df[['NumWebPurchases', 'NumCatalogPurchases', 'NumStorePurchases']].sum(axis=1)

    st.subheader("Basic Info")
    st.write(df.head())

    with st.expander("Column Info"):
        st.write(df.describe(include='all'))

    # Visualizations
    st.subheader("Marital Status Distribution")
    fig1, ax1 = plt.subplots()
    ax1.pie(df['Marital_Status'].value_counts(), labels=df['Marital_Status'].value_counts().index,
            autopct='%1.1f%%', startangle=140)
    ax1.axis('equal')
    st.pyplot(fig1)

    st.subheader("Average Income by Education")
    fig2, ax2 = plt.subplots(figsize=(8,6))
    sns.barplot(x='Education', y='Income', data=df, estimator=pd.Series.mean, errorbar=None, ax=ax2)
    ax2.set_title("Average Income by Education")
    ax2.set_xticklabels(ax2.get_xticklabels(), rotation=45)
    st.pyplot(fig2)

    st.subheader("Univariate Analysis")
    st.subheader("Age Distribution")
    fig_u1, ax_u1 = plt.subplots()
    sns.histplot(df['Age'], kde=True, bins=30, color='skyblue', ax=ax_u1)
    ax_u1.set_title("Age Distribution")
    st.pyplot(fig_u1)

    st.subheader("Income Distribution")
    fig_u2, ax_u2 = plt.subplots()
    sns.histplot(df['Income'], kde=True, bins=30, color='orange', ax=ax_u2)
    ax_u2.set_title("Income Distribution")
    st.pyplot(fig_u2)

    st.subheader("Total Spending Distribution")
    fig_u3, ax_u3 = plt.subplots()
    sns.histplot(df['Total_Spending'], kde=True, bins=30, color='green', ax=ax_u3)
    ax_u3.set_title("Total Spending Distribution")
    st.pyplot(fig_u3)

    st.subheader("Bivariate Analysis")
    st.subheader("Spending vs Marital Status")
    fig_b1, ax_b1 = plt.subplots()
    sns.boxplot(x='Marital_Status', y='Total_Spending', data=df, ax=ax_b1)
    ax_b1.set_title("Total Spending by Marital Status")
    ax_b1.set_xticklabels(ax_b1.get_xticklabels(), rotation=45)
    st.pyplot(fig_b1)

    st.subheader("Spending vs Education")
    fig_b2, ax_b2 = plt.subplots()
    sns.boxplot(x='Education', y='Total_Spending', data=df, ax=ax_b2)
    ax_b2.set_title("Total Spending by Education Level")
    ax_b2.set_xticklabels(ax_b2.get_xticklabels(), rotation=45)
    st.pyplot(fig_b2)

    st.subheader("Correlation Heatmap")
    fig3, ax3 = plt.subplots(figsize=(15, 8))
    sns.heatmap(df.select_dtypes(include='number').corr(), annot=True, cmap='coolwarm', fmt=".2f", ax=ax3)
    st.pyplot(fig3)
    

    st.subheader("Clustering (KMeans + PCA)")
    features = df[['Age', 'Income', 'Total_Spending', 'Total_Children']].dropna()
    scaler = StandardScaler()
    scaled = scaler.fit_transform(features)

    kmeans = KMeans(n_clusters=4, random_state=42, n_init='auto')
    cluster_labels = kmeans.fit_predict(scaled)
    features['Cluster'] = cluster_labels

    pca = PCA(n_components=2)
    pca_components = pca.fit_transform(scaled)

    fig4, ax4 = plt.subplots()
    sns.scatterplot(x=pca_components[:, 0], y=pca_components[:, 1], hue=cluster_labels, palette='Set2', s=60, ax=ax4)
    ax4.set_title("Customer Clusters (PCA View)")
    st.pyplot(fig4)

    st.subheader("High Spenders (Top 25%)")
    threshold = df['Total_Spending'].quantile(0.75)
    high_spenders = df[df['Total_Spending'] > threshold]
    st.write(high_spenders[['ID', 'Income', 'Total_Spending', 'Education', 'Marital_Status']].head())

    fig5, ax5 = plt.subplots()
    sns.histplot(df['Total_Spending'], bins=30, kde=True, ax=ax5)
    ax5.axvline(threshold, color='red', linestyle='--', label='75th Percentile')
    ax5.set_title("Spending Distribution with High Spenders Marked")
    ax5.legend()
    st.pyplot(fig5)

else:
    st.info("Please upload the `marketing_data.csv` file to proceed.")

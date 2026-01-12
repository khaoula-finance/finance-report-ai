import streamlit as st
import pandas as pd

st.set_page_config(page_title="Finance Report AI", layout="centered")

st.title("📊 Finance Report AI")
st.write("Application de génération automatique de rapports financiers")

# Chargement des données
df = pd.read_csv("indicateurs_financiers.csv")

st.subheader("📈 Indicateurs financiers")
st.dataframe(df)

st.subheader("🧠 Analyse automatique")
st.write("""
Les indicateurs ci-dessus montrent l'évolution de la performance financière 
entre 2019 et 2022. L'application permet de transformer ces résultats 
en un rapport financier interprétable à l'aide de l'IA générative.
""")

st.success("Application déployée avec succès 🚀")

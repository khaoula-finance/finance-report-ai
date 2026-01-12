import pandas as pd

# Chargement des données
df = pd.read_csv("Profit and loss.csv", encoding="latin1")
df.columns = df.columns.str.strip()

# Colonnes temporelles
years = [
    "JAN - DEC 2019",
    "JAN - DEC 2020",
    "JAN - DEC 2021",
    "JAN - DEC 2022"
]

# Nettoyage et conversion des valeurs numériques
for col in years:
    df[col] = (
        df[col]
        .astype(str)
        .str.replace(",", "", regex=False)
        .str.strip()
    )
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Traitement des valeurs manquantes
df[years] = df[years].fillna(0)

# Sauvegarde des données nettoyées
df.to_csv("data_nettoyee.csv", index=False)

# Calcul des indicateurs
df_clean = pd.read_csv("data_nettoyee.csv")

df_clean["Evolution_2020_2019"] = df_clean["JAN - DEC 2020"] - df_clean["JAN - DEC 2019"]
df_clean["Evolution_2021_2020"] = df_clean["JAN - DEC 2021"] - df_clean["JAN - DEC 2020"]
df_clean["Evolution_2022_2021"] = df_clean["JAN - DEC 2022"] - df_clean["JAN - DEC 2021"]

df_clean["Croissance_2020_2019"] = df_clean["Evolution_2020_2019"] / df_clean["JAN - DEC 2019"]
df_clean["Croissance_2021_2020"] = df_clean["Evolution_2021_2020"] / df_clean["JAN - DEC 2020"]
df_clean["Croissance_2022_2021"] = df_clean["Evolution_2022_2021"] / df_clean["JAN - DEC 2021"]

df_clean.to_csv("indicateurs_financiers.csv", index=False)



import pandas as pd
import numpy as np

np.random.seed(42)

# creo df con id univoci incrementali
n = 0
id_dfs = [] # lista dei singoli df
for i in range(200):
    n+= 1
    df = pd.DataFrame({"customerID": n}, index=range(12))
    id_dfs.append(df)

id_df = pd.concat(id_dfs) #unisco i df in unico df con solo gli id.
# CORREZIONE: reset_index(inplace=True) è deprecato in pandas, riassegno il risultato
id_df = id_df.reset_index(drop=True)

#------------ dfs con dati utenti ------------------

#dataframe list
df_list = []

##15 churned users con calo accessi
for a in range(15):
    #valore base
    first = np.random.randint(10,201)

    #valori attorno al valore base per i primi 6 mesi
    rumore = np.random.normal(0, first * .1, 6)
    first_6_values = np.round(first + rumore).astype(int)

    #valori calanti ultimi 6 mesi
    # CORREZIONE rumore: separo la tendenza (valore) dal valore osservato.
    # - il rumore NON entra in valore, quindi non si accumula mese dopo mese
    #   (come nei primi 6 mesi, dove oscilla attorno a una base fissa)
    # - il rumore è il 7% del valore ATTUALE, non della base iniziale,
    #   così resta proporzionato mentre i login calano
    # - max(..., 0) evita login negativi
    valore = first_6_values[-1]
    risultati = []
    for i in range(6):
        sottrazione = np.random.uniform(.85, .95)   # perde tra 5% e 15% al mese
        valore = valore * sottrazione               # tendenza: calo proporzionale, senza rumore
        osservato = valore + np.random.normal(0, valore * .07)
        risultati.append(max(round(osservato), 0))  # arrotondo solo il valore salvato

    #unisco array + lista 
    logins = np.append(first_6_values, risultati)

    churned_user = pd.DataFrame({
        "month": np.arange(-12,0)
        , "logins": logins
        , "churned": True
    })
    #store new df in list
    df_list.append(churned_user)

##15 churned users senza calo accessi
for b in range(15):

    base = np.random.randint(10,201)                #intero tra 10 e 200
    rumore = np.random.normal(0, base * .1, 12)     #12 numeri, con centro zero, al max 10% della base.
    valori = np.round(base + rumore).astype(int)    # integra il rumore alla base e ne tiene il numero intero.

    churned_user = pd.DataFrame({
        "month": np.arange(-12,0)
        , "logins": valori
        , "churned": True
    })
    #store new df in list
    df_list.append(churned_user)

##20 nochurned users con calo accessi
for c in range(20):
    #valore base
    first = np.random.randint(10,201)

    #valori attorno al valore base per i primi 6 mesi
    rumore = np.random.normal(0, first * .1, 6)
    first_6_values = np.round(first + rumore).astype(int)

    #valori calanti ultimi 6 mesi
    # CORREZIONE rumore: separo la tendenza (valore) dal valore osservato.
    # - il rumore NON entra in valore, quindi non si accumula mese dopo mese
    #   (come nei primi 6 mesi, dove oscilla attorno a una base fissa)
    # - il rumore è il 7% del valore ATTUALE, non della base iniziale,
    #   così resta proporzionato mentre i login calano
    # - max(..., 0) evita login negativi
    valore = first_6_values[-1]
    risultati = []
    for i in range(6):
        sottrazione = np.random.uniform(.85, .95)   # perde tra 5% e 15% al mese
        valore = valore * sottrazione               # tendenza: calo proporzionale, senza rumore
        osservato = valore + np.random.normal(0, valore * .07)
        risultati.append(max(round(osservato), 0))  # arrotondo solo il valore salvato

    #unisco array + lista 
    logins = np.append(first_6_values, risultati)

    churned_user = pd.DataFrame({
        "month": np.arange(-12,0)
        , "logins": logins
        , "churned": False
    })
    #store new df in list
    df_list.append(churned_user)

##150 sani: nochurn users senza calo accessi
for d in range(150):

    base = np.random.randint(10,201)                #intero tra 10 e 200
    rumore = np.random.normal(0, base * .1, 12)     #12 numeri, con centro zero, al max 10% della base.
    valori = np.round(base + rumore).astype(int)    # integra il rumore alla base e ne tiene il numero intero.

    churned_user = pd.DataFrame({
        "month": np.arange(-12,0)
        , "logins": valori
        , "churned": False
    })
    #store new df in list
    df_list.append(churned_user)

b2busers = pd.concat(df_list)
# CORREZIONE: reset_index(inplace=True) è deprecato in pandas, riassegno il risultato
b2busers = b2busers.reset_index(drop=True)

# unisco il df con gli id al df con dati utenti
b2busers = pd.merge(id_df, b2busers, left_index=True, right_index=True)
# CORREZIONE: index=False evita la colonna inutile "Unnamed: 0" quando si rilegge il csv
b2busers.to_csv('Data/b2busers.csv', index=False)
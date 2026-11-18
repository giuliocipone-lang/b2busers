import pandas as pd
import numpy as np

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
    limit = max(round(first * .1), 6)
    valore = first
    risultati = []
    for i in range(6):
        sottrazione = np.random.randint(5,limit + 1)
        valore = max(valore - sottrazione, 0)   # mai sotto zero
        risultati.append(valore)

    #unisco array + lista 
    logins = np.append(first_6_values, risultati)

    churned_user = pd.DataFrame({
        "customerID": [np.random.randint(100000, 1000000)] * 12
        , "month": np.arange(-12,0)
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
        "customerID": [np.random.randint(100000, 1000000)] * 12
        , "month": np.arange(-12,0)
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
    limit = max(round(first * .1), 6)
    valore = first
    risultati = []
    for i in range(6):
        sottrazione = np.random.randint(5,limit + 1)
        valore = max(valore - sottrazione, 0)   # mai sotto zero
        risultati.append(valore)

    #unisco array + lista 
    logins = np.append(first_6_values, risultati)

    churned_user = pd.DataFrame({
        "customerID": [np.random.randint(100000, 1000000)] * 12
        , "month": np.arange(-12,0)
        , "logins": logins
        , "churned": False
    })
    #store new df in list
    df_list.append(churned_user)

##150 sani: nochurn users senza calo accessi
for c in range(150):

    base = np.random.randint(10,201)                #intero tra 10 e 200
    rumore = np.random.normal(0, base * .1, 12)     #12 numeri, con centro zero, al max 10% della base.
    valori = np.round(base + rumore).astype(int)    # integra il rumore alla base e ne tiene il numero intero.

    churned_user = pd.DataFrame({
        "customerID": [np.random.randint(100000, 1000000)] * 12
        , "month": np.arange(-12,0)
        , "logins": valori
        , "churned": False
    })
    #store new df in list
    df_list.append(churned_user)

b2busers = pd.concat(df_list)
b2busers.reset_index(drop=True, inplace=True)
b2busers.to_csv('Data/b2busers.csv')
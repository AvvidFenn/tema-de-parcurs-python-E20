import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

print(df.to_string())

X=5
Y=6

# Graficul 1 (toate valorile pentru coloanele Durata, Puls, MaxPuls, Calorii)
plt.figure(figsize=(10,5))
for col in ['Durata','Puls','MaxPuls','Calorii']:
    if col in df.columns:
        plt.plot(df.index, df[col], label=col)

plt.title("Graficul 1 Toate Valorile")
plt.xlabel("Index")
plt.ylabel("Valoare")
plt.legend()
plt.grid(True)
plt.show()

# Graficul 2 (primele X=5 valori pentru coloanele Durata, Puls, Calorii)
plt.figure(figsize=(10,5))
df_primele5=df[['Durata','Puls','Calorii']].head(X)
for col in df_primele5.columns:
    plt.plot(df_primele5.index,df_primele5[col],label=col)

plt.title("Graficul 2 Primele 5 Valori")
plt.xlabel("Index")
plt.ylabel("Valoare")
plt.legend()
plt.grid(True)
plt.show()
        
# Graficul 3 (ultimele Y=6 valori, iar culorile/merkeri pentru X%6==5 sunt verde,albastru, diamant)
plt.figure(figsize=(10,5))
df_ultimele6=df[['Durata','Puls']].tail(Y)
plt.plot(
    df_ultimele6.index,
    df_ultimele6['Durata'],
    color='green',
    marker='D',
    label='Durata'
)
plt.plot(
    df_ultimele6.index,
    df_ultimele6['Puls'],
    color='blue',
    marker='D',
    label='Puls'
)

plt.title("Graficul 3 Ultimele 6 Valori")
plt.xlabel("Index")
plt.ylabel("Valoare")
plt.legend()
plt.grid(True)
plt.show()

    

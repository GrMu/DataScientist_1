from draaitabel import *
import matplotlib.pyplot as plt

# Grafiek maken
df_pivot.plot(kind='bar', figsize=(12, 6))

# Labels en titel
plt.xlabel("Jaar")
plt.ylabel("Aantal transacties")
plt.title("Aantal transacties per gemeente per jaar")
plt.legend(title="Gemeente")

# Grafiek tonen
plt.show()

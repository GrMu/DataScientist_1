import matplotlib.pyplot as plt
import numpy as np

# Sterktes
categorieën = ['Logisch denken', 'Soft skills', 'Python', 'Databases', 'Statistiek', 'Business']
N = len(categorieën)

# Dummy data voor Alice (scores op 5)
alice_scores = [4, 3, 5, 4, 4, 3]

# Hoeken voor elke categorie in de radar chart
hoeken = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
hoeken += hoeken[:1]  # Sluit de cirkel

# Radar chart setup
fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

# Waarden voor Alice
waarden = alice_scores + alice_scores[:1]  # Sluit de cirkel

# Plot de radialen voor Alice
for i in range(N):
    ax.plot([hoeken[i], hoeken[i]], [0, waarden[i]], color='skyblue', alpha=0.5)

# Plot de punten op de radialen
ax.scatter(hoeken[:-1], alice_scores, color='skyblue', s=100)

# Instellingen
ax.set_title('Sterkteanalyse van Alice', size=14)
ax.set_xticks(hoeken[:-1])
ax.set_xticklabels(categorieën)
ax.set_yticks(range(1, 6))
ax.set_yticklabels(map(str, range(1, 6)))
ax.set_ylim(0, 5)
ax.legend(['Alice'], loc='upper right', bbox_to_anchor=(1.1, 1.1))

# Tonen
plt.tight_layout()
plt.show()

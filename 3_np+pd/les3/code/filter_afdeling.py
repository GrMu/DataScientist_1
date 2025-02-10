import pandas as pd

# Dummy data
data = {
    "id": range(1, 13),
    "naam": ["Jan", "Sara", "Ali", "Emma", "Tom", "Lisa", "Mark", "Eva", "Noah", "Sophie", "Lars", "Mila"],
    "functie": ["Manager", "HR Medewerker", "IT Support", "Marketing Specialist", "Developer", "HR Manager", "Accountant", "Verkoper", "Engineer", "Designer", "Logistiek", "CEO"],
    "afdeling": ["Management", "HR", "IT", "Marketing", "IT", "HR", "Finance", "Sales", "Engineering", "Design", "Logistiek", "Management"],
    "loon": [5000, 3200, 3500, 3700, 4000, 4500, 3800, 3400, 4200, 3600, 3300, 8000]
}

# DataFrame maken
personeel = pd.DataFrame(data)

# Functie om te filteren op afdeling
def filter_op_afdeling(df, afdeling):
    return df[df["afdeling"] == afdeling]

# Voorbeeld: filteren op HR
hr_personeel = filter_op_afdeling(personeel, "HR")
print(hr_personeel)

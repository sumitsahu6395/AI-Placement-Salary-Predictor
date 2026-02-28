import pandas as pd
import random

data = []

for _ in range(600):

    cgpa = round(random.uniform(5, 9.8), 2)
    iq = random.randint(80, 140)
    communication = random.randint(3, 10)
    internship = random.randint(0, 1)
    coding = random.randint(40, 100)
    aptitude = random.randint(40, 100)
    projects = random.randint(0, 1)
    certifications = random.randint(0, 1)

    # Balanced scoring system
    score = (
        cgpa * 1.5 +
        iq * 0.05 +
        communication * 1.2 +
        internship * 2 +
        coding * 0.08 +
        aptitude * 0.07 +
        projects * 2 +
        certifications * 1.5
    )

    placed = 1 if score > 30 else 0   # balanced threshold

    # Salary calculation
    if placed == 1:
        salary = int(
            250000 +
            cgpa * 25000 +
            iq * 800 +
            communication * 12000 +
            coding * 2000 +
            aptitude * 1500 +
            internship * 50000 +
            projects * 60000 +
            certifications * 30000 +
            random.randint(-30000, 30000)
        )
    else:
        salary = 0

    data.append([
        cgpa, iq, communication, internship,
        coding, aptitude, projects, certifications,
        placed, salary
    ])

columns = [
    "CGPA","IQ","Communication","Internship",
    "Coding","Aptitude","Projects","Certifications",
    "Placed","Salary"
]

df = pd.DataFrame(data, columns=columns)

df.to_csv("placement_pro_600.csv", index=False)

print("✅ Dataset created successfully!")
print("Total rows:", len(df))
print(df.head())
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression, LinearRegression
import pickle

# Load dataset
data = pd.read_csv("placement_pro_600.csv")

# ---------- Placement Model ----------
X = data[['CGPA','IQ','Communication','Internship',
          'Coding','Aptitude','Projects','Certifications']]
y = data['Placed']

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)

placement_model = LogisticRegression(max_iter=1000)
placement_model.fit(X_train,y_train)

print("Placement Accuracy:", placement_model.score(X_test,y_test))

pickle.dump(placement_model, open("placement_model.pkl","wb"))

# ---------- Salary Model ----------
placed_data = data[data['Placed']==1]

X_sal = placed_data[['CGPA','IQ','Communication','Internship',
                     'Coding','Aptitude','Projects','Certifications']]
y_sal = placed_data['Salary']

salary_model = LinearRegression()
salary_model.fit(X_sal,y_sal)

pickle.dump(salary_model, open("salary_model.pkl","wb"))

print(" Models saved!")
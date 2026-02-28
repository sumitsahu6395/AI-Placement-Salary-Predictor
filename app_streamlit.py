import streamlit as st
import pickle

# Load models
placement_model = pickle.load(open("placement_model.pkl","rb"))
salary_model = pickle.load(open("salary_model.pkl","rb"))

st.title("🎓 AI Placement & Salary Predictor")

st.write("Enter student details:")

cgpa = st.slider("CGPA", 5.0, 10.0, 7.0)
iq = st.slider("IQ Score", 80, 140, 100)
communication = st.slider("Communication Skills", 1, 10, 6)
internship = st.selectbox("Internship", [0,1])
coding = st.slider("Coding Score", 0, 100, 60)
aptitude = st.slider("Aptitude Score", 0, 100, 60)
projects = st.selectbox("Projects Completed", [0,1])
certifications = st.selectbox("Certifications", [0,1])

if st.button("Predict"):

    features = [[cgpa, iq, communication, internship,
                 coding, aptitude, projects, certifications]]

    placed = placement_model.predict(features)[0]

    if placed == 1:
        salary = int(salary_model.predict(features)[0])
        st.success(" High Chances of Placement!")
        st.info(f" Expected Salary: ₹ {salary:,}")
    else:
        st.error(" Low Placement Chances")
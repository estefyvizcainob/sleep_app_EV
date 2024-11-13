import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load('sleep_model.pkl')

# Set up the app title and header image
st.set_page_config(page_title="Sleep Quality Predictor", layout="wide")
st.title("Sleep Quality Predictor")

# App description
st.write("""
### Enter your data below to see if you're getting a good night's sleep.
Adjust the sliders and input your information to predict your sleep quality based on your habits.
""")

# Layout for user input using columns
col1, col2 = st.columns(2)

with col1:
    age = st.slider("Age", 18, 60, 25)
    university_year = st.slider("University Year (1 to 5)", 1, 5, 2)
    #sleep_duration = st.slider("Sleep Duration (hours)", 3.0, 12.0, 7.0)
    study_hours = st.slider("Study Hours", 0.0, 15.0, 5.0)
    screen_time = st.slider("Screen Time (hours)", 0.0, 10.0, 2.0)

with col2:
    caffeine_intake = st.slider("Caffeine Intake (cups)", 0, 10, 1)
    physical_activity = st.slider("Physical Activity (minutes)", 0, 300, 60)
    sleep_quality = st.slider("Sleep Quality Score (1 to 10)", 1, 10, 5)
    weekday_sleep_start = st.slider("Weekday Sleep Start Time (24-hr format)", 0.0, 24.0, 22.0)
    weekend_sleep_start = st.slider("Weekend Sleep Start Time (24-hr format)", 0.0, 24.0, 23.0)

weekday_sleep_end = st.slider("Weekday Sleep End Time (24-hr format)", 0.0, 24.0, 7.0)
weekend_sleep_end = st.slider("Weekend Sleep End Time (24-hr format)", 0.0, 24.0, 8.0)
gender_male = st.radio("Gender", ('Male', 'Female')) == 'Male'

# Prepare the feature array
features = np.array([[age, university_year, study_hours, screen_time,
                      caffeine_intake, physical_activity, sleep_quality, weekday_sleep_start,
                      weekend_sleep_start, weekday_sleep_end, weekend_sleep_end, int(gender_male)]])

# Predict sleep quality
if st.button("Predict Sleep Quality"):
    prediction = model.predict(features)
    if prediction[0] == 1:
        st.success("You are likely having a good night's sleep!")
        st.balloons()
    else:
        st.error("You might not be getting a good night's sleep. Consider reviewing your sleep habits.")

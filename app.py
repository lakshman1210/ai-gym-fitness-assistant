
import streamlit as st
import math

st.set_page_config(page_title="AI Gym & Fitness Assistant", layout="wide")

st.title("🏋️ AI Gym & Fitness Assistant (MVP)")

menu = st.sidebar.selectbox(
    "Choose Module",
    [
        "AI Gym Trainer (Basics)",
        "AI Dietician & Calorie Coach",
        "Fitness Habit Tracker",
        "Virtual Gym Buddy"
    ]
)

if menu == "AI Gym Trainer (Basics)":
    st.header("AI Gym Trainer (Demo Version)")
    st.info("This MVP simulates workout tracking logic (no camera required).")
    reps = st.number_input("Enter reps completed", 0, 500, 10)
    sets = st.number_input("Enter sets completed", 0, 50, 3)
    if st.button("Analyze Workout"):
        score = reps * sets
        st.success(f"Workout Performance Score: {score}")
        if score < 50:
            st.warning("Try increasing reps or sets for better results.")
        else:
            st.success("Great workout! Keep going 💪")

elif menu == "AI Dietician & Calorie Coach":
    st.header("AI Dietician & Calorie Coach")
    weight = st.number_input("Weight (kg)", 30.0, 200.0, 70.0)
    height = st.number_input("Height (cm)", 120.0, 220.0, 170.0)
    goal = st.selectbox("Fitness Goal", ["Weight Loss", "Muscle Gain", "Maintenance"])
    if st.button("Generate Diet Plan"):
        bmi = weight / ((height/100) ** 2)
        st.write(f"**Your BMI:** {round(bmi,2)}")
        if goal == "Weight Loss":
            st.success("Recommended: High-protein, low-carb meals.")
        elif goal == "Muscle Gain":
            st.success("Recommended: High-protein, calorie-surplus meals.")
        else:
            st.success("Recommended: Balanced diet with maintenance calories.")

elif menu == "Fitness Habit Tracker":
    st.header("AI Fitness Habit Tracker")
    days = st.slider("Workouts per week", 0, 7, 3)
    if days < 2:
        st.warning("You're at risk of skipping workouts. Try setting reminders!")
    else:
        st.success("Good consistency! Keep it up 🔥")

elif menu == "Virtual Gym Buddy":
    st.header("Virtual Gym Buddy 🤖")
    mood = st.selectbox("How are you feeling today?", ["Motivated", "Tired", "Lazy", "Stressed"])
    if st.button("Get Motivation"):
        responses = {
            "Motivated": "Awesome! Let's crush today's workout 💥",
            "Tired": "Rest if needed, but even a light workout helps 💙",
            "Lazy": "Start small. 5 minutes can turn into 30!",
            "Stressed": "Exercise is the best stress relief. You've got this 🌟"
        }
        st.success(responses[mood])

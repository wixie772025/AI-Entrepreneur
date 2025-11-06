import streamlit as st
import random

# Display logo and header
st.image("logo.png", width=120)
st.markdown("""
    <h1 style='color:#4A90E2;'>AI Entrepreneur Prompt Generator</h1>
    <p style='font-size:18px;'>Empower your business with weekly AI-driven content ideas for social media growth.</p>
""", unsafe_allow_html=True)

# Define categorized prompts for each day of the week
weekly_prompts = {
    "Monday": [
        "Show your workspace or behind-the-scenes setup.",
        "Share your weekly goals and intentions."
    ],
    "Tuesday": [
        "Post a client testimonial or review.",
        "Share a tip or trick related to your niche."
    ],
    "Wednesday": [
        "Ask your audience a question to boost engagement.",
        "Share a myth vs. fact post about your industry."
    ],
    "Thursday": [
        "Tell a personal story about your business journey.",
        "Share a challenge you overcame recently."
    ],
    "Friday": [
        "Promote a product or service with urgency.",
        "Offer a limited-time discount or bonus."
    ],
    "Saturday": [
        "Feature a community member or collaborator.",
        "Share a fun fact or behind-the-scenes moment."
    ],
    "Sunday": [
        "Reflect on the week and share a win.",
        "Express gratitude or share a motivational quote."
    ]
}

# Function to generate a weekly schedule
def generate_schedule():
    return {day: random.choice(prompts) for day, prompts in weekly_prompts.items()}

# Button to generate new schedule
if st.button("🔄 Generate New Schedule"):
    schedule = generate_schedule()
    st.session_state.schedule = schedule

# Initialize schedule if not already present
if "schedule" not in st.session_state:
    st.session_state.schedule = generate_schedule()

# Display the schedule
st.markdown("<h2 style='color:#4A90E2;'>🗓️ Your Weekly Prompt Schedule</h2>", unsafe_allow_html=True)
for day, prompt in st.session_state.schedule.items():
    st.markdown(f"<p style='font-size:16px;'><strong>{day}:</strong> {prompt}</p>", unsafe_allow_html=True)

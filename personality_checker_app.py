import streamlit as st

# Page setup
st.set_page_config(page_title="PERSONALITY CHECKER APP", layout="centered")

# Custom CSS styling
st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #198754;
    color: white;
    font-size: 16px;
    height: 3em;
    border-radius: 10px;
    width: 100%;
}
.main {
    background-color: #f5f7fa;
    padding: 20px;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

# App header
st.markdown("<h1 style='text-align: center; color: #2E86C1;'>🧠 PERSONALITY CHECKER APP</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Welcome! Answer honestly to discover your personality type</h4>", unsafe_allow_html=True)

# User info
st.markdown("### 👤 User Information")
name = st.text_input("Full Name")
roll_no = st.text_input("Roll Number")

# Questions
questions = [
    "Do you enjoy trying new things?", "Do you like to plan things in advance?", "Do you enjoy being the center of attention?",
    "Do you easily trust others?", "Do you often feel anxious without reason?", "Do you like to solve complex problems?",
    "Do you follow a strict routine?", "Do you prefer group activities over solo ones?", "Do you find it easy to forgive others?",
    "Do you worry about the future often?", "Do you enjoy artistic experiences?", "Do you pay attention to details?",
    "Do you enjoy meeting new people?", "Do you sympathize with others’ feelings?", "Do you get upset easily?",
    "Do you enjoy learning about different cultures?", "Do you make to-do lists regularly?", "Do you find it easy to make small talk?",
    "Do you care deeply about others’ well-being?", "Do your moods change frequently?", "Do you enjoy experimenting with new ideas?",
    "Do you like to keep your space tidy?", "Do you enjoy parties and gatherings?", "Do you go out of your way to help others?",
    "Do you feel nervous in new situations?", "Do you enjoy working on creative projects?", "Do you double-check your work often?",
    "Do you talk to strangers easily?", "Do you believe in giving second chances?", "Do you get frustrated quickly?",
    "Do you think outside the box?", "Do you stick to deadlines strictly?", "Do you gain energy from social interaction?",
    "Do you show empathy to others?", "Do you feel down without reason?", "Do you enjoy writing or reading fiction?",
    "Do you manage your time efficiently?", "Do you find crowds exciting?", "Do you often put others' needs before your own?",
    "Do you feel overwhelmed by small issues?", "Do you think deeply about abstract topics?", "Do you organize tasks by priority?",
    "Do you find it fun to lead group discussions?", "Do you comfort friends when they’re upset?",
    "Do you often feel insecure about yourself?"
]

# Form to collect answers
answers = []
with st.form("personality_form"):
    for i, question in enumerate(questions):
        # Grouping and progress tracking
        if i == 0:
            st.markdown("### 🧠 Cognitive & Curiosity Traits")
        elif i == 10:
            st.markdown("### 📋 Planning & Organization")
        elif i == 20:
            st.markdown("### 🤝 Social & Interpersonal Traits")
        elif i == 30:
            st.markdown("### 💬 Communication & Energy")
        elif i == 40:
            st.markdown("### ❤️ Emotional Stability")
        
        st.caption(f"Question {i+1} of {len(questions)}")
        answer = st.radio(f"{i+1}. {question}", ["Yes", "No"], key=f"q{i}", horizontal=True)
        answers.append(answer)

    submitted = st.form_submit_button("📤 Submit")

# Result logic
if submitted:
    if not name or not roll_no or len(answers) != 45:
        st.warning("Please fill in your name, roll number, and answer all questions.")
    else:
        yes_count = answers.count("Yes")

        # Personality evaluation
        if yes_count >= 35:
            result = "Highly Expressive Personality"
            tip = "You are open, social, and emotionally expressive."
        elif yes_count >= 25:
            result = "Balanced Personality"
            tip = "You show a good balance of traits. Keep growing."
        elif yes_count >= 15:
            result = "Reserved Personality"
            tip = "You prefer a calm, organized life and reflect deeply."
        else:
            result = "Introverted or Passive Personality"
            tip = "You tend to be quiet and introspective. Embrace your strengths."

        # Display result
        st.success("🎉 Thank you for completing the assessment!")
        st.markdown(f"**👤 Name:** {name}")
        st.markdown(f"**🆔 Roll Number:** {roll_no}")
        st.markdown(f"**🔍 Personality Type:** *{result}*")
        st.info(f"💬 {tip}")

        # Download result
        output = f"""PERSONALITY CHECKER APP - Result

Name: {name}
Roll Number: {roll_no}

Personality Type: {result}
Interpretation: {tip}
Score (Yes Answers): {yes_count}/45
"""
        st.download_button("📥 Download Your Result", output, file_name="personality_result.txt")

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center;'>© 2025 | Developed by <strong>Zubair</strong> | Petroleum & Natural Gas Engineering Department</p>", unsafe_allow_html=True)

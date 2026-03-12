import streamlit as st
import plotly.graph_objects as go

# Setting up the Page
st.set_page_config(page_title="The Predictor", page_icon="")

# Adding a Custom Header
st.markdown("<h1 style='text-align: center;'> The Tech Path Predictor</h1>", unsafe_allow_html=True)
st.write("Determine your success probability in different Tech domains based on your current logic and skills.")

# Input Section
st.subheader("Enter Your Stats")
name = st.text_input("What is your name?")
math_skill = st.slider("Maths & Statistics (0-100)", 0, 100, 50)
logic_skill = st.slider("Logic & Problem Solving (0-100)", 0, 100, 50)
creative_skill = st.slider("Design & Aesthetics (0-100)", 0, 100, 50)
coding_hours = st.number_input("Daily Coding Hours", 0, 15, 2)

# The Prediction Logic
if st.button("Predict My Future "):
    # Calculating Scores
    ds_score = (math_skill * 0.45) + (logic_skill * 0.45) + (coding_hours * 1)
    web_score = (creative_skill * 0.50) + (logic_skill * 0.30) + (coding_hours * 2)

    # Creating a Visual Radar Chart
    categories = ['Data Science', 'Web Development', 'Logic', 'Mathematics', 'Creativity']
    values = [ds_score, web_score, logic_skill, math_skill, creative_skill]

    fig = go.Figure(data=go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        line_color='#00d2ff'
    ))

    fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 100])), showlegend=False)

    # Displaying the Results
    st.plotly_chart(fig)
    
    if ds_score > web_score:
        st.success(f"Hey {name}! Your data-driven logic makes you a perfect fit for **Data Science & AI**.")
    else:
        st.info(f"Hey {name}! Your creative flair suggests you'll excel in **Web & App Development**.")
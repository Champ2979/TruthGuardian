import streamlit as st
import joblib
import pandas as pd

# Load CSS styles
with open('assets/style.css', 'r') as f:
    css = f.read()
st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

# Load the trained model
trained_model = joblib.load('trained_model.pkl')

# Define the class labels
labels = ['Commenting', 'Ogling/Facial Expressions/Staring', 'Touching /Groping']

# Prediction function
def predict_probabilities(text, model):
    return model.predict_proba([text])[0]

# App layout
st.markdown('<h1 class="title">Truth Guardian</h1>', unsafe_allow_html=True)

# Text input
text_input = st.text_input('Enter the text:', '')

# Prediction section
if st.button('Predict'):
    if text_input:
        probabilities = predict_probabilities(text_input, trained_model)
        
        # Display results with enhanced visualization
        st.markdown('<div class="predicted-probabilities">', unsafe_allow_html=True)
        st.markdown('**Predicted Probabilities:**')
        
        for label, prob in zip(labels, probabilities):
            # Probability item with bar
            st.markdown(f'''
            <div class="probability-item">
                <span>{label}</span>
                <span>{prob:.2%}</span>
            </div>
            <div class="probability-bar">
                <div class="bar-fill" style="width: {prob*100}%"></div>
            </div>
            ''', unsafe_allow_html=True)
        
        # Highlight highest probability
        max_idx = probabilities.argmax()
        st.markdown(f'''
        <div style="margin-top: 1.5rem; padding: 1rem; background: #e3f2fd; border-radius: 8px;">
            🚩 Predicted Category: <strong>{labels[max_idx]}</strong> ({probabilities[max_idx]:.2%})
        </div>
        ''', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.warning('Please enter some text.')

# About section
st.markdown('<div class="about-section">', unsafe_allow_html=True)
st.markdown('#### About')
st.markdown('''
This Streamlit app is made with love by the team Deception Detectors of VIT Bhopal.
- Powered by machine learning
- Explainable AI approach
- Real-time classification
''')
st.markdown('</div>', unsafe_allow_html=True)
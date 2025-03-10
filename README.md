# Truth Guardian - Harassment Classifier 🛡️

[![Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-app-url.herokuapp.com)

A machine learning-powered web application for classifying harassment-related text into categories: Commenting, Ogling/Facial Expressions/Staring, and Touching/Groping.

![App Demo](https://via.placeholder.com/800x400.png?text=Truth+Guardian+Interface+Preview)

## Features ✨
- Real-time text classification
- Probability visualization with progress bars
- Explainable AI results
- Responsive web interface
- Category highlighting for maximum probability

## Installation 💻

1. **Clone the repository**
```bash
git clone https://github.com/your-username/truth-guardian.git
cd truth-guardian
```
2. **Install dependencies**
   ```
   pip install -r requirements.txt
   ```
## Usage 🚀
1. **Run the Streamlit app**
    ```
    streamlit run app.py
    ```
   2. **In the browser:**
      - Enter text in the input box
      - Click "Predict" to see classification results
      - View probabilities and highlighted dominant category
  ## Project Structure 📁
     
├── app.py              # Main application logic
├── trained_model.pkl   # Trained ML model (REPLACE WITH YOUR ACTUAL MODEL)
├── assets/
│   └── style.css       # Custom styling
├── requirements.txt    # Dependencies list
└── README.md           # Documentation

## Dependencies 📦
  - Python 3.7+
  - Streamlit
  - scikit-learn
  - pandas
  - joblib

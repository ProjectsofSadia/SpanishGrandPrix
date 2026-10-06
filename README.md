# SpanishPrix: Real-Time F1 Winner Prediction Dashboard

Welcome to SpanishPrix - an app that predicts Formula 1 race outcomes using real telemetry data from the Spanish Grand Prix.  
Built with FastF1, scikit-learn, and Streamlit, this app forecasts winners, visualizes confidence levels, and even predicts the full podium!

### 🚗 Features
- ✅ **Live Driver Selection** by name
- 🧠 **ML Model Trained** on real 2023 Spanish GP lap data
- 📊 **Confidence Bar Charts** for predicted winner
- 🖼️ **Driver Image Display** on selection
- 🏆 **Top 3 Podium Predictions** based on lap performance

---

### 📊 Technologies Used

| Tool         | Purpose                          |
|--------------|----------------------------------|
| Python       | Core development                 |
| FastF1       | Pulls real F1 telemetry/lap data |
| Scikit-learn | Builds ML prediction models      |
| Streamlit    | Frontend UI for real-time input  |
| Plotly       | Beautiful live charts            |
| PIL          | Displays driver headshots        |

---

### 🔧 How to Run Locally

```bash
git clone https://github.com/ProjectsofSadia/SpanishGrandPrix.git
cd SpanishGrandPrix
pip install -r requirements.txt
streamlit run app.py

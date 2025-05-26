import streamlit as st
import pandas as pd
import plotly.express as px
from model import train_with_fastf1
from datetime import datetime

st.set_page_config(page_title="SpanishGrandPrix 🏎️", layout="wide")
st.title("🏁 Real-Time F1 Winner Prediction Dashboard")
model, features, driver_map = train_with_fastf1("data/spanish_fastf1_real.csv")
st.markdown("### 🔧 Input Your Real-Time Race Stats Below")

lap_time = st.slider("Average Lap Time (seconds)", 60.0, 100.0, 75.0, step=0.1)
compound = st.selectbox("Tire Compound", ["Soft", "Medium", "Hard"])
team_code = st.slider("Team Code", 0, 9, 3)
driver_dict = dict(zip(driver_map["DriverFullName"], driver_map["DriverCode"]))
driver_name = st.selectbox("👤 Select Driver", list(driver_dict.keys()))
driver_code = driver_dict[driver_name]
compound_map = {"Soft": 2, "Medium": 1, "Hard": 0}
compound_encoded = compound_map[compound]
input_data = [[lap_time, compound_encoded, team_code, driver_code]]
prediction = model.predict(input_data)
prediction_proba = model.predict_proba(input_data)[0]

if st.button("🚨 Predict Now"):
    st.subheader("📢 Prediction Outcome")
    if prediction[0] == 1:
        st.success("🏆 This driver is predicted to WIN!")
    else:
        st.error("❌ This driver is NOT predicted to win.")

    st.markdown("### 🔮 Prediction Confidence Chart")
    chart_data = pd.DataFrame({
        "Outcome": ["Not Winner", "Winner"],
        "Probability": [prediction_proba[0], prediction_proba[1]]
    })

    fig = px.bar(chart_data, x="Outcome", y="Probability", color="Outcome",
                 title="Prediction Probability", text_auto='.2f')
    st.plotly_chart(fig, use_container_width=True)

    st.markdown(f"🕒 Prediction made at: `{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}`")
    st.markdown("## 🏆 Predicted Podium (Top 3 Drivers)")
try:
    podium = pd.read_csv("data/predicted_podium.csv")
    st.table(podium.rename(columns={"DriverFullName": "Driver", "LapTimeSeconds": "Fastest Lap (s)"}))
except:
    st.warning("No podium prediction available. Run `scrape_fastf1.py` to generate it.")


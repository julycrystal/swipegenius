import streamlit as st
import pandas as pd
import plotly.express as px
import random
from utils import calculate_engagement_metrics

st.title("📊 Dating Analytics")

# Get metrics
metrics = calculate_engagement_metrics()

# Display metrics
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Messages Sent", metrics["messages_sent"])
with col2:
    st.metric("Response Rate", f"{metrics['response_rate']}%")
with col3:
    st.metric("Matches", metrics["matches"])
with col4:
    st.metric("Quality Conversations", metrics["successful_conversations"])

# Create sample data for charts
dates = pd.date_range(start="2024-01-01", periods=30, freq="D")
data = pd.DataFrame({
    "Date": dates,
    "Messages": [random.randint(0, 10) for _ in range(30)],
    "Matches": [random.randint(0, 3) for _ in range(30)]
})

# Activity timeline
st.subheader("Activity Timeline")
fig = px.line(data, x="Date", y=["Messages", "Matches"])
st.plotly_chart(fig, use_container_width=True)

# Success metrics
st.subheader("Success Metrics")
success_data = pd.DataFrame({
    "Metric": ["First Responses", "Extended Conversations", "Date Proposals", "Accepted Dates"],
    "Count": [random.randint(10, 50) for _ in range(4)]
})
fig2 = px.bar(success_data, x="Metric", y="Count")
st.plotly_chart(fig2, use_container_width=True)

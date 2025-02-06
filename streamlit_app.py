import streamlit as st

st.set_page_config(
    page_title="SwipeGenius",
    page_icon="💘",
    layout="wide"
)

st.title("🚀 SwipeGenius")

if "messages" not in st.session_state:
    st.session_state.messages = []

st.markdown("""
## Welcome to SwipeGenius!
Your personal AI dating coach that helps you:
- 💬 Get smart conversation suggestions
- 👤 Optimize your dating profile
- 📊 Track your dating success metrics
""")

st.sidebar.success("Select a feature above")

# Quick Start Section
st.header("🎯 Quick Start")
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Create New Profile", use_container_width=True):
        st.switch_page("pages/1_💬_Chat_Assistant.py")
with col2:
    st.button("Start Chat Assistant", use_container_width=True)
with col3:
    st.button("View Analytics", use_container_width=True)

import streamlit as st
from utils import generate_message_suggestion

st.title("💬 Chat Assistant")

# Message context input
context = st.text_area("Paste the conversation context here:", height=150)

# Tone selection
tone = st.select_slider(
    "Select conversation tone:",
    options=["casual", "friendly", "romantic", "professional"]
)

if st.button("Generate Response"):
    if context:
        suggestion = generate_message_suggestion(context, tone)
        st.success("Suggested Response:")
        st.write(suggestion)
        
        # Save to history
        if "message_history" not in st.session_state:
            st.session_state.message_history = []
        st.session_state.message_history.append({
            "context": context,
            "suggestion": suggestion
        })
    else:
        st.warning("Please provide conversation context")

# History section
if st.session_state.get("message_history"):
    st.header("Recent Suggestions")
    for item in st.session_state.message_history[-5:]:
        with st.expander(f"Context: {item['context'][:50]}..."):
            st.write(item['suggestion'])

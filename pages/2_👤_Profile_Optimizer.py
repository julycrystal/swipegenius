import streamlit as st
from utils import analyze_profile

st.title("👤 Profile Optimizer")

# Profile input section
st.header("Current Profile")
profile_text = st.text_area(
    "Paste your dating profile text:",
    height=200,
    help="Include your bio, prompts, and any other text from your profile"
)

profile_photos = st.file_uploader(
    "Upload profile photos (optional)",
    type=["jpg", "jpeg", "png"],
    accept_multiple_files=True
)

if st.button("Analyze Profile"):
    if profile_text:
        analysis = analyze_profile(profile_text)
        
        # Display results
        col1, col2 = st.columns(2)
        
        with col1:
            st.success("✨ Strengths")
            for strength in analysis["strengths"]:
                st.write(f"✓ {strength}")
                
        with col2:
            st.info("🎯 Suggested Improvements")
            for improvement in analysis["improvements"]:
                st.write(f"• {improvement}")
    else:
        st.warning("Please enter your profile text")

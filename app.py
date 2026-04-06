import streamlit as st
from main import analyze_resume_logic

st.set_page_config(page_title="HROne AI-Scout", page_icon="🎯")

st.title("🎯 HROne AI-Scout")
st.markdown("### Smart Talent Acquisition Tool")

# Inputs
jd = st.text_area("📋 Paste Job Description (JD) here...", height=150)
uploaded_file = st.file_uploader("📄 Upload Candidate Resume (PDF)", type="pdf")

if st.button("🚀 Analyze Candidate"):
    if uploaded_file and jd:
        with st.spinner("AI is evaluating the profile..."):
            result = analyze_resume_logic(uploaded_file, jd)
            
            if "error" in result:
                st.error(f"Something went wrong: {result['error']}")
            else:
                st.success(f"Candidate Match Score: {result['match_score']}%")
                st.write(f"**Matching Skills:** {', '.join(result['matching_skills'])}")
                st.write(f"**Missing Skills:** {', '.join(result['missing_skills'])}")
                st.subheader("🎙️ Suggested Interview Questions")
                for q in result['interview_questions']:
                    st.info(q)
    else:
        st.warning("Please upload a resume and paste the JD first!")
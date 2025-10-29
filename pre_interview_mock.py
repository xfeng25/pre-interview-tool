import streamlit as st

st.set_page_config(
    page_title="Stakeholder Interview Tool – Pre-Interview Generation",
    layout="centered"
)

st.title("Pre-Interview Generation (Prototype Mock)")
st.markdown("""
This mock demonstrates how a single uploaded brief generates two outputs:
1) an Interview Guide for planning,
2) and, if requested, an Interview Slide Guide for use during the actual stakeholder interview.
""")

# Step 1: Upload or paste context
st.header("Step 1 – Upload Context / Project Brief")
uploaded_file = st.file_uploader("Upload a PDF or DOCX file", type=["pdf", "docx"])
manual_text = st.text_area(
    "Or paste context here:",
    height=150,
    placeholder="Paste project background, goals, timeline, and stakeholder context..."
)

# Session state
if "guide_generated" not in st.session_state:
    st.session_state.guide_generated = False
if "slide_prompt_shown" not in st.session_state:
    st.session_state.slide_prompt_shown = False

# Continue only if input provided
if uploaded_file or manual_text:
    st.success("Context uploaded successfully.")
    st.divider()

    # Step 2: Generate Interview Guide
    st.header("Step 2 – Generate Interview Guide")
    if st.button("Generate Interview Guide"):
        st.session_state.guide_generated = True
        st.session_state.slide_prompt_shown = True

    # Show sample Interview Guide once generated
    if st.session_state.guide_generated:
        st.subheader("Interview Guide (Example)")
        st.markdown("""
        **Interview Objectives**  
        - Clarify strategic priorities around robotics and automation  
        - Identify decision-makers and success metrics  
        - Surface pain points, blockers, and urgency  

        **Target Stakeholders**  
        - Business lead (growth / revenue owner)  
        - Technical lead (product / engineering)  
        - Operations owner (process / execution)  

        **Key Themes to Cover**  
        - Where current process breaks today  
        - Where differentiation is most defensible  
        - What “success” looks like in the next 1–2 quarters  

        **Suggested Flow (30–40 min)**  
        - Opening / context alignment (5 min)  
        - Core challenges & impact (20–25 min)  
        - Success definition / next steps (5–10 min)
        """)
        st.info("This is a planning document for the interviewer, not the final question script.")

    st.divider()

    # Step 3: Ask if user wants Slide Guide
    if st.session_state.slide_prompt_shown:
        st.header("Step 3 – Prepare Interview Slide Guide?")
        st.markdown("Would you like to turn this plan into a slide-style question set for the live interview?")
        generate_slide = st.button("Yes, generate Slide Guide")

        # Step 4: Show slide-style question set
        if generate_slide:
            st.subheader("Interview Slide Guide (Example)")
            st.markdown("""
            **Slide 1 – Opening Script**  
            - Thank you for taking the time today.  
            - We’d like to understand your current challenges and opportunities.  
            - This discussion will take about 30–40 minutes and is for internal use only.  

            **Slide 2 – Agenda & Goals**  
            - Business goals and success definition  
            - Current barriers or pain points  
            - Impact if no changes occur  

            **Slide 3 – Business Lead Questions**  
            - What are your top priorities this quarter?  
            - Where does the current process break down?  
            - If this succeeds, what will change for you?  

            **Slide 4 – Technical / Product Lead Questions**  
            - What are the hardest technical constraints right now?  
            - Which challenges are now solvable with current tools?  
            - What approaches have already been tried?  

            **Slide 5 – Wrap Up / Next Steps**  
            - Is there anything else we should understand?  
            - Who else should we be speaking with?
            """)
            st.success("This version is designed for use during the live interview.")
else:
    st.warning("Please upload a document or paste context to continue.")

st.divider()
st.caption("Static prototype – no API calls yet. This layout is for structure and workflow review.")

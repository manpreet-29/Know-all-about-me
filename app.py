### Main page for streamlit resume
import streamlit as st
import pages.about
import pages.project
import pages.kaggle
import pages.work
import pages.intro
import pages.pie
import pages.intern
import pages.skills
import pages.nlp
import pages.thoughts
import resources.ast as ast

PAGES = {
    "Know me" : pages.intro,
    "Profile": pages.about,
    "Experience": pages.project,
    "Projects &  Internships": pages.intern,
    "Skills" : pages.skills,
    "NLP & Data Science Learnings" : pages.nlp,
    "Work Learnings" : pages.work,
    "Thoughts & Soft Skills" : pages.thoughts,
    "Pie and AI Meetups": pages.pie,
    "Kaggle Days Meetup": pages.kaggle
    
}

def main():
    """Main function of App"""
    st.set_page_config(layout="wide")
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))

    page = PAGES[selection]
    
    with st.spinner(f"Loading {selection} ..."):
        ast.write_page(page)

    st.sidebar.title("Collaborations")
    st.sidebar.info(
        """
        If you are looking to collaborate for Projects or Trainings,
        or If you like to get mentored or invite me as a speaker, 
        Please email me -  
        [email me](mailto:budhraja.manpreet@gmail.com) or reach out 
        to me on [LinkedIn](https://www.linkedin.com/in/manpreet-budhraja/)
""")
    

if __name__ == "__main__":
    main()

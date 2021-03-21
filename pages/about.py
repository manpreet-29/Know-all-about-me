"""About page shown when the user enters the application"""
import streamlit as st

def write():
    """Used to write the about page in the app.py file"""
    
    st.title("All about me..!!")
    st.markdown(
                """

:large_blue_diamond: **Data Engineer**\n
The current role revolves around working with database management(AWS Redshift), automation of tasks (using Python), and helping out other teams at work with required data for BI reports. This involves me working with various ETL tools like Matillion. Apart from this, I have started some creative learning initiatives at work to develop and grow skills.

:large_blue_diamond: **Speaker | Blogger | Community- Builder**\n
I have speaker at various meetups and workshops. Apart from this, I am a Lead organizer at **Kaggle Days Meetups - Surat** and **Pie and AI: Gujarat**. You will often find me on Saturdays at Integrated Mentoring Session - where we as a community believe in More Together Learning. I like to write blogs on data science, NLP, work learnings, and some general topics.

:large_blue_diamond: **NLP- Practitioner**\n
Sharing the learnings and practices of NLP with the community through various workshops and classes or through LinkedIn posts and videos. I have completed her thesis titled "Neural Machine Translation on Indian Languages". Currently, working on a research project. 

:large_blue_diamond: **Collaborations**\n
If you are looking to collaborate on Research opportunities in NLP, 
Corporate training in NLP, 
teaching and mentoring students & professionals in NLP.
Please
[email me](mailto:budhraja.manpreet@gmail.com) or reach out 
to me on [LinkedIn](https://www.linkedin.com/in/manpreet-budhraja/) 



""",
            unsafe_allow_html=True,
        )




if __name__ == "__main__":
    main()


import streamlit as st
import streamlit.components.v1 as components
def write():
    """Used to write the page in the app.py file"""
    
    st.title("Pie and AI - Gujarat Meetups :slightly_smiling_face: ")
    st.markdown(
            """
            ### Pie and AI is a community in partnership with **deeplearning.ai**
            ### Here are some of the talks and discussions hosted by Pie and AI Gujarat. The sessions held are from various domains of Data Science..!!\n""",
            unsafe_allow_html=True
        )
    c1, c2, c3 = st.beta_columns((3,3,3))
    
    with c1:
        components.iframe(src="https://www.youtube.com/embed/CmjY1ATKNH0",  height=315 )
        st.markdown("** True/False Question Generation using NLP - Ramsri Goutham Golla**", unsafe_allow_html=True)

        

        components.iframe(src="https://www.youtube.com/embed/C2wEuFDdQpY",  height=315 )
        st.markdown("**Grasp The Basics To Become an Expert - Danny Ma**", unsafe_allow_html=True)
        
        components.iframe(src="https://www.youtube.com/embed/G2XJnfc3XJU",  height=315 )
        st.markdown("**The Dangers of Dirty Data - Susan Walsh**", unsafe_allow_html=True)

        
        
        
            
    with c2:
        components.iframe(src="https://www.youtube.com/embed/gIfN-N6OkLA",  height=315 ) 
        st.markdown("**Brain vs AI - Giuseppe & Ghaith**", unsafe_allow_html=True)
       
        components.iframe(src="https://www.youtube.com/embed/TVef8B8ekq4", height=315)
        st.markdown("**Data Visualisation is all about Data Storytelling - Vijay Pravin**", unsafe_allow_html=True)

        
        components.iframe(src="https://www.youtube.com/embed/8oJJNDtazkY",  height=315 ) 
        st.markdown("**Artificial Intelligence - 4th Industrial Revolution - Hari Kantipudi**", unsafe_allow_html=True)


        
        
        
    with c3:  
         
        components.iframe(src="https://www.youtube.com/embed/rxkOeYwnvv4", height=315)
        st.markdown("**Being a Data Scientist - Thom Ives & Abdul Najeeb**", unsafe_allow_html=True)


        components.iframe(src="https://www.youtube.com/embed/0bC2hk2OB-U",  height=315 )
        st.markdown("**Algorithmic Decision Making: Why accuracy isn't enough ? - Ansgar **", unsafe_allow_html=True)

        
            
        
if __name__ == "__main__":
    main()

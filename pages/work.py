"""All about Work learnings ..!!"""
import streamlit as st
import streamlit.components.v1 as components
def write():
    """Used to write the page in the app.py file"""
    
    st.title("All about Work Learnings :speech_balloon: ")
    st.markdown(
            """
            Sharing what I have learned at work, which has immensely helped me to grow and interact with my Linkedin Family..!!""",
            unsafe_allow_html=True,
        )
    c1, c2 = st.beta_columns((3,3))
    
    with c1:
        components.iframe(src="https://www.linkedin.com/embed/feed/update/urn:li:share:6777589026737205248", height=400)
        components.iframe(src="https://www.linkedin.com/embed/feed/update/urn:li:share:6770780292924928000", height=296) 
        components.iframe(src = "https://www.linkedin.com/embed/feed/update/urn:li:share:6771043712911884288" , height=500 )
        components.iframe(src = "https://www.linkedin.com/embed/feed/update/urn:li:share:6729753913366515712" , height=400)
            
    with c2:
        components.iframe(src = "https://www.linkedin.com/embed/feed/update/urn:li:share:6775398788417826816", height=500 )
        components.iframe(src = "https://www.linkedin.com/embed/feed/update/urn:li:share:6767781819942285312", height=500 ) 
        components.iframe(src = "https://www.linkedin.com/embed/feed/update/urn:li:ugcPost:6732275725614813186", height=400)
            
        
if __name__ == "__main__":
    main()

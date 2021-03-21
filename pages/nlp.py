
import streamlit as st
import streamlit.components.v1 as components
def write():
    """Used to write the page in the app.py file"""
    
    st.title("NLP & Data Science Learnings..!!" )
  

    c1, c2 = st.beta_columns((3,3))
    
    with c1:
        components.iframe(src="https://www.linkedin.com/embed/feed/update/urn:li:share:6773646149204131841", height=520)
        components.iframe(src="https://www.linkedin.com/embed/feed/update/urn:li:share:6769956489504333824", height=430)
        components.iframe(src="https://www.youtube.com/embed/YLj52vt-wQ4",  height=315 ) 
        
 
    with c2:
        components.iframe(src="https://www.linkedin.com/embed/feed/update/urn:li:ugcPost:6772128459939467264", height=450)
        components.iframe(src="https://www.linkedin.com/embed/feed/update/urn:li:share:6730097521634418688", height=520)
        components.iframe(src="https://www.youtube.com/embed/f2m6Mon0VE8",  height=315 )         

        

        
if __name__ == "__main__":
    main()
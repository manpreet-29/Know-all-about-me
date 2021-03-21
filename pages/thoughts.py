"""All about Work learnings ..!!"""
import streamlit as st
import streamlit.components.v1 as components
def write():
    """Used to write the page in the app.py file"""
    
    st.title("Thoughts :thought_balloon: ")
    st.markdown(
            """
            Sharing some postitvity and soft skills that help us everyday..!!""",
            unsafe_allow_html=True,
        )
    c1, c2 = st.beta_columns((3,3))
    
    with c1:
        components.iframe(src="https://www.linkedin.com/embed/feed/update/urn:li:share:6778895371167961088", height=300)
        components.iframe(src="https://www.linkedin.com/embed/feed/update/urn:li:share:6778510384224636928", height=296)
        components.iframe(src = "https://www.linkedin.com/embed/feed/update/urn:li:share:6777228909109932032", height=500) 
        components.iframe(src="https://www.linkedin.com/embed/feed/update/urn:li:share:6772864413667004416", height=400)
        components.iframe(src="https://www.linkedin.com/embed/feed/update/urn:li:share:6777787626494705664", height=250)
        components.iframe(src="https://www.linkedin.com/embed/feed/update/urn:li:share:6729008253046439936", height=360)

            
    with c2:
        components.iframe(src = "https://www.linkedin.com/embed/feed/update/urn:li:share:6778654002344202240", height=300)
        components.iframe(src = "https://www.linkedin.com/embed/feed/update/urn:li:share:6772503725744410625", height=400)
        components.iframe(src="https://www.linkedin.com/embed/feed/update/urn:li:share:6778179581686935552", height=250) 
        components.iframe(src = "https://www.linkedin.com/embed/feed/update/urn:li:share:6778293153016401920", height=480) 
        components.iframe(src = "https://www.linkedin.com/embed/feed/update/urn:li:share:6773968490819833856", height=500) 
        components.iframe(src = "https://www.linkedin.com/embed/feed/update/urn:li:share:6731546780737028096", height=500)
  

        
if __name__ == "__main__":
    main()
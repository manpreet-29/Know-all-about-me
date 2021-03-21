"""About page shown when the user enters the application"""
import streamlit as st
from PIL import Image
def write():
    """Used to write the about page in the app.py file"""
   
    st.title("Hello.. Welcome.. :woman-raising-hand::woman-raising-hand:!!")
    st.markdown(
            """ \n \n # Who Am I?
## I am a **Talkative - Curious - Data Scientist** ..!!"\n
## **Helping Community is my passion** .... and **learning is a Everyday Hobby** ..!!\n
## Know more about my learnings, meetups, posts and talks through Navigation pannel..!!\n
### [**LinkedIn**](https://www.linkedin.com/in/manpreet-budhraja/) | [**Email**](mailto:budhraja.manpreet@gmail.com)| [**Youtube**](https://www.youtube.com/c/AIMLearning/videos)"""  ,
            unsafe_allow_html=True,
        )

    
if __name__ == "__main__":
    main()

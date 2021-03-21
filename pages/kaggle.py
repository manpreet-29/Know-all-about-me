
import streamlit as st
import streamlit.components.v1 as components
def write():
    """Used to write the page in the app.py file"""
    
    st.title("Kaggle Days - Surat Meetups :slightly_smiling_face: ")
    st.markdown(
            """
            ### These meetups are hosted by Kaggle Days Surat chapter. It aims to connect and help community by discussing various topics.!!\n
            ### Learn from various Kagglers, Bloggers and content creators about their expertise in the field of Data Science and soft skills.
            
            """,
            unsafe_allow_html=True
        )
    c1, c2, c3 = st.beta_columns((3,3,3))
    
    with c1:
        components.iframe(src="https://www.youtube.com/embed/AZY2D8wwSYk",  height=315 )
        st.markdown("**Secret Tips to build your brand as a Data Scientist - Ravit Jain**", unsafe_allow_html=True)

        

        components.iframe(src="https://www.youtube.com/embed/AwO8pFWk-uE",  height=315 )
        st.markdown("**Data Science skills through Community Learning - Chanukya**", unsafe_allow_html=True)
        
        components.iframe(src="https://www.youtube.com/embed/XieLzbTmkI8",  height=315 )
        st.markdown("**Creating Compelling stories through Kaggle Notebooks - Parul Panday**", unsafe_allow_html=True)

        components.iframe(src="https://www.youtube.com/embed/zceibHtFs4w",  height=315 ) 
        st.markdown("**SELF DRIVING CARS 101 - Gagandeep Reehal**", unsafe_allow_html=True)

        components.iframe(src="https://www.youtube.com/embed/yxz5uGecQY8", height=315)
        st.markdown("**Solving Operation's Team usecase with AI - Abhishekh Joshi**", unsafe_allow_html=True)

        

        components.iframe(src="https://www.youtube.com/embed/GrffeA85fcc",  height=315 )
        st.markdown("**A Comprehensive Review of Super Resolution -Anil**", unsafe_allow_html=True)
        
        
            
    with c2:
        components.iframe(src="https://www.youtube.com/embed/tx1bWvNi1Zo",  height=315 ) 
        st.markdown("**All About Blogging & Content Creation - Madhav Bhal**", unsafe_allow_html=True)
       
        components.iframe(src="https://www.youtube.com/embed/hExTx7U0rVg", height=315)
        st.markdown("**Starting & Scaling AI ventures - Shantanu Kumar**", unsafe_allow_html=True)

        
        components.iframe(src="https://www.youtube.com/embed/RAN6A-Tc2pg",  height=315 ) 
        st.markdown("**Opportunities 101 - Baani Kaur**", unsafe_allow_html=True)


        
        components.iframe(src="https://www.youtube.com/embed/YThGQ31RNcE",  height=315 )
        st.markdown("**Making ML Pipelines with Pyspark - Ayon Roy**", unsafe_allow_html=True)
        

        components.iframe(src="https://www.youtube.com/embed/FtOx7S87ha4", height=315)
        st.markdown("**Zero to Kaggle Kernels Top 20 - Shahul**", unsafe_allow_html=True)

        components.iframe(src="https://www.youtube.com/embed/dheYEm5e81k", height=315)
        st.markdown("** Covid-19 prediction with Time Series Modeling - Sharmistha Chatterjee**", unsafe_allow_html=True)
        
    with c3:  
         
        components.iframe(src="https://www.youtube.com/embed/R5Y6IwxNWMo", height=315)
        st.markdown("**Going Beyond your first ML Project - Akshay Bahadur**", unsafe_allow_html=True)


        components.iframe(src="https://www.youtube.com/embed/Yn6Uxhw-ULc",  height=315 )
        st.markdown("**Stepping into Machine Learning - Aqib & Tirth**", unsafe_allow_html=True)

        components.iframe(src="https://www.youtube.com/embed/6k_M4cFxbcc", height=315)
        st.markdown("**Building Turstworth AI - Shina & Praanshu**", unsafe_allow_html=True)

        components.iframe(src="https://www.youtube.com/embed/pxynIWFgu20", height=315)
        st.markdown("**Ask Me Anything Session - Siddha & Susanna **", unsafe_allow_html=True) 

        components.iframe(src="https://www.youtube.com/embed/cm7VEgwXxtY", height=315)
        st.markdown("**Introduction to Natural Language Processing - Tanul Singh**", unsafe_allow_html=True)

        components.iframe(src="https://www.youtube.com/embed/r7Db2IPmoUM",  height=315 )
        st.markdown("**Understanding Steel Defect Detection Solution - Rishabh Tiwari**", unsafe_allow_html=True)
        
            
        
if __name__ == "__main__":
    main()

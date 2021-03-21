"""Skills page shown when the user enters the application"""
import streamlit as st

def write():
    """Used to write the page in the app.py file"""
    st.title("**Projects and Internships** :female-technologist:")
    st.markdown(
            """\n
### :arrow_forward:  **NLP Intern - Team ALgorithm** (*July,2020*)\n 
Team Algorithm, is an emerging startup in the field of Procurement and and serve their services in the same.\n
### - **Name Entity Recognition for Customer-Buyer dataset**
1. The aim of the project was to achieve a entity recognition system from the dataset of buyer and seller chats.
2. Build this using **StandfordNLP-NER, Spacy**.
3. There were issues in recognising the money entity from the text which was resolved using **regular expressions**.

### :arrow_forward: **#BuildwithAI Hackathon by Hackmakers** (*July,2020*)\n 
### - **Flashpoint - Trend difference between News and Twitter data**
1. The project was build as a team where we aimed to find the difference in trending topics during COVID from **news and twitter**.
2. It also helped us to realise the change in topic trends from the month of January to July. 
3. As a part of team, I was responsible for collecting the data and making presentation for hackathon.
4. The tools used were **gensim, IBM Watson Tone Analyser, d3.js**. We did topic modelling and sentiment analysis on the dataset.
5. You can find the project on [**Youtube**]('https://www.youtube.com/watch?v=WRUHfEMJQrA') and [**Github**]('https://github.com/manpreet-29/BuilWithAI-NLP_challenge.git')

### :arrow_forward: **Machine Learning Intern - DataToBiz** (*Dec,2018*)\n 
DatatoBiz helps SMEs & Large Enterprises to take more accurate decisions and deploy the models even faster with powerful AI solutions.\n
### - **AUTOMATED ESSAY SCORING**
1. The project was based on debugging the Kaggle Compition winner's code and deploy it on Windows.
2. Learned the practices of debugging and understanding the concepts of Feature Engineering.
3. Tools used Vagrant, Visual Studio and Python

### :arrow_forward: **Machine Learning Intern - CSIR-CSIO** (*May,2018*)\n 
Central Scientific Instruments Organisation is a Chandigarh, India-based national laboratory dedicated to research, design and development of scientific and industrial instruments.\n
### - **WIKIPEDIA**
1. Collected Wikipedia Data Dump of Indian Languages. Cleaned then using **regular expressions**.
2. Used transfer learning on gensim model to create **word embeddings** for the given files.

### :arrow_forward: **Data Analytics Intern - Essar Steel Pvt. Ltd** (*May,2017*)\n 
Essar Steel India Private Limited is a fully integrated flat carbon steel manufacturer based in India. 
### - **Learning DBMS & Tableau**
1. Learned about Database Management Systems and visualisation techniques like R and Tableau.
2. Learned how things work in real time. Did a small project on compartive study between R and Tableau.






""",
            unsafe_allow_html=True,
        )
if __name__ == "__main__":
    main()

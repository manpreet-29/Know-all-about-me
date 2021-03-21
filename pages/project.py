"""Skills page shown when the user enters the application"""
import streamlit as st

def write():
    """Used to write the page in the app.py file"""
    st.title("**Work Experiences** :female-technologist:")
    st.markdown(
            """\n
### :arrow_forward:  **Data Engineer - Packt** (*Sept,2020 - Present*)\n 
Packt is a publishing company. It is headquartered in Birmingham,UK. Packt primarily publishes print and electronic books and videos related to various technologies, tools and programming languages.\n

### - **Amazon's Bestseller collection & analysis**
1. The project primarily involved studying the **Amazon Best Seller's** page for various categories of books and develop an outline for the project. This project was aimed to help the **publishing team** to understand the competitive market space and popular content among the readers.
2. Build a **python script** using **beautiful soup**. It was very important to have a longer sleep time and a function to rotate proxies, to avoid blocking.
3. Collected the required data and then used  **Parsehub** to get more information about the each product.

### - **Hevo Collaboration with Packt**
1. Hevo provides services to automatically get your data to datawahrehouse with the help of connectors.
2. Possible collaboration will eventually help in **saving around 30-40% of the yearly costs**.
3. I contributed as a major link in connecting and now leading it for further talks and discussions.

### - **Value per Titles and Lifetime Time Value**
1. This was a project build for the **Finance Team**, to help understand how various book titles performed and their possible revenue generation.
2. Build this project in team with my manager. The code involved various **statiscal calculations** and coding in python.
3. Automated the scripts to run weekly and used the data to make BI reports of the same.

### - **Classification of Reviews**
1. This project was build to help our **marketting team** to better understand the customers.
2. Using simple **regular expression concepts** classified data in various categories.
3. This was further analysed and a sentiment analysis was done on the same.

### - **Documentation of various scripts in Matillion**
1. This project helped the **data team** to analyse the unecessary scripts in the Matillion.
2. Transferred various python scripts running to cron jobs.
3. This helped us to close the instance and use it only for some hours, which eventually helped us to **save 20-30% of the yearly costs**.

### - **User Preference Recommendtaion Systems**
1. This project was build to help the **marketing team** to target the right audience for marketting.
2. Build a recommendation of user prefrances based on**time spend surfing and the rewards they recieved**.
3. Prefrence was based on tools, languages, category and concepts.
4. Simply used weights and scoring to decide the top 5 from each topics.

    




""",
            unsafe_allow_html=True,
        )
if __name__ == "__main__":
    main()

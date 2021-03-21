"""Skills page shown when the user enters the application"""
import streamlit as st

def write():
    """Used to write the page in the app.py file"""
    st.title("**Skills** :hammer_and_pick:")
    st.markdown(
            """
    :small_blue_diamond:  **Languages**: C, Python, Java, R \n
    :small_blue_diamond:  **Libraries**: Pandas, NumPy, BeautifulSoup, Sklearn, NLTK, Matplotlib, Seaborn, Pytorch\n
    :small_blue_diamond:  **Software**:: Git, AWS, Redshift, VS Code,  Tableau, Jupyter-lab, Camtasia, Android Studio\n
    :small_blue_diamond:  ** Other Skills: Speaker, Community-Builder, Creative, Writing\n
""",
            unsafe_allow_html=True,
        )
    st.title("**Talks and Blogs** :book: :speaking_head_in_silhouette:")
    st.markdown(
          """
  

  :small_blue_diamond: A Talk with a group of students from Kenya about the practice of More Together Learning. [**Youtube**]('https://www.youtube.com/watch?v=AC8Ycq6hOmc')\n           
  :small_blue_diamond: Podcast with [**Priyanka**]('https://www.linkedin.com/in/priyankakomala/') on 50th special episode.[**Youtube**]('https://www.youtube.com/watch?v=UA9KJD4NX9Q') and [**Spotify**]('https://open.spotify.com/episode/6ObcbQni2j9qJwu2u81Kfx')\n
  :small_blue_diamond: Podcast with [**Thom Ives**]('https://www.linkedin.com/in/thomives/') where we talk about our journey and community learnings. [**YouTube**]('https://www.youtube.com/watch?v=QB8gwaTvFfE')\n
  :small_blue_diamond: Hosted a talk with some inspirational women in the field of data science on **Women's Day**. [**YouTube**]('https://www.youtube.com/watch?v=spQWBNPfnZ4')\n
  :small_blue_diamond: Sharing some of my Data Science confessions with the student community. [**Youtube**]('https://www.youtube.com/watch?v=Pg1ATimohRU')\n
  :small_blue_diamond: Sharing with community about the **Real Lfe Usecases of AI**. [**Youtube**]('https://www.youtube.com/watch?v=Pg1ATimohRU')\n
  :small_blue_diamond: This blog explains about what it takes to **Data Scientist**.[**Link**]('https://integratedmlai.com/being-a-data-scientist/')\n
  :small_blue_diamond: This blog explains about all the odds of getting research internship. [**Link**]('https://manpreet-kaur.medium.com/improving-the-odds-of-getting-research-opportunities-b8c9dcbf6781')\n           
  :small_blue_diamond: Pleasure of hosting **Inspirational Women Pannel** for Pie & AI: Narobi chapter.[**Youtube**]('https://lnkd.in/evJDr2x')\n
  :small_blue_diamond: This blog is about some lessons learned while listening a podcast. [**Link**]('https://www.linkedin.com/pulse/tuesday-learning-podcast-manpreet-budhraja/?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_featured%3B2WiGGvELSZeuA%2Blz8bu0Ig%3D%3D&licu=urn%3Ali%3Acontrol%3Ad_flagship3_profile_view_base_featured-featured_item_detail_view')\n
  :small_blue_diamond: Sharing some thoughts on lessons learned in College. [**Link**]('https://integratedmlai.com/lessons-learned-in-college-life/')\n
  :small_blue_diamond: Editor for a blog post on the Cycles of becoming a Great Data Scientist [**Link**](['https://integratedmlai.com/the-cycles-of-becoming-a-great-data-scientist/')\n
# """,
            unsafe_allow_html=True,
        )
    st.title("**Communtity and Other Acitivitites** :female-construction-worker:")
    st.markdown(
            """
  :small_blue_diamond:  Mentor at Google Developers Group, NIT - Surat. \n
  :small_blue_diamond:  Taught English in a Municipal Corporation School for NGO - Dharam Bharthi Mission.\n
  :small_blue_diamond:  Conducted a workshop on Data Analysis at NIT,Surat.\n
  :small_blue_diamond:  Attended teh ICON-2019, Conference held by LTRC Lab, IIIT-Hyderabad.\n
  :small_blue_diamond:  Attended the "Summer School on Machine Learning and Computer Vision" help by CVIT Lab. IIIT-Hyderabad.\n
  :small_blue_diamond:  Attended workshop on Dta Analysis using R organised by AMHD, NIT-Surat.\n
  :small_blue_diamond:  Member of designing team and creative content writer for SCOSH, AMHD -NIT,Surat.\n
  :small_blue_diamond:  Member of various college committees and anchor at various college events. \n
""",
            unsafe_allow_html=True,
        )
if __name__ == "__main__":
    main()
import streamlit as st
from PIL import Image
st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Market analysis of laptops (June 2022)")

st.sidebar.success("Select the task you want!.")

st.markdown(
    """
    This data analysis and exploration was done on the flipkart's laptop data, which
    was scapped in the month on May-June 2022.

    This app tries to get a wide view of the laptop market int the year 2022.
    Several machine learning models were also used to train the dataset avalible 
    and analyze the importance of several laptop features and also to get an estimate 
    of the price for a laptop, given its specifications.""")

img = Image.open('imgs_analysis/homepage_img.jpeg')
st.image(img)

st.markdown(
    """
    **👈 Select a task from the sidebar** to see view and use
    the apps we've developed."""
)

st.write(
    """
    **There are 3 main contents in this project**
    - Exploratory data analysis 

    - Predict laptop price based on specifications
    
    - Effect of several features on ML algorithms (feature importances)

"""
)

st.write(
    """
    #### Limitations
"""
)

st.write(
    """
    There are many limitations for a project like this, the major one is the amount of data available which affects the flexiblity of the several models.
    Especially the deep learning models need humungous amounts of data, which is not a possible for this particular problem, as 
    the amount of laptops in productions would generally not be in such gigantic amounts.
    
    **This project is an experimatation of how ML algos could gather information from limited amount of data and give us the desired result.**
 
"""
)



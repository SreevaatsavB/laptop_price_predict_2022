import streamlit as st

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
    of the price for a laptop, given its specifications.

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


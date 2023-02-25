from PIL import Image
import streamlit as st

st.header("Some insights from models while training")
st.subheader("Feature importances")

image1 = Image.open('imgs_exp/fimp_rf.png')
st.write(
    """
    #### From a random forest regressor
    Random forest with these hyper-parameters were used :- n_estimators = 40, max_depth=5. 
    - We could see that RAM, gpu processor, cpu processor, gpu brand and storage have a heavy impact on the price of a laptop.
    
    - While features like, Expandable memory, SSD and all have very less effect on price of a laptop.
   """
)
st.image(image1)

st.write(
    """
    **The rest of the feature importances are done after removing the gpu_processor and weight features as GPU processors needs to be ranked upon their benchmarks.**
   """
)

tab1, tab2 = st.tabs(["Gradient Boosting Regressor", "XGBoost Regressor"])

with tab1:
   st.header("Gradient boost")
   image2 = Image.open('imgs_exp/fimp_gbr.png')
   st.write(
       """
       #### From a gradient boosting regressor
       We can see that the feature importacnes are almost same for both random forest and this model.
       The hyper parameters for this model are :- {'learning_rate': 0.1, 'max_depth': 3, 'n_estimators': 250} 
      """
   )
   st.image(image2)

with tab2:
    st.header("XGBoost")
    image3 = Image.open('imgs_exp/fimp_xgb.png')
    st.write(
        """
        #### From a XGBoost regressor
        We can see that the feature importacnes are almost same for both random forest and this model.
        The hyper parameters for this model are :- {'lambda': 10, 'learning_rate': 0.1, 'max_depth': 5, 'n_estimators': 200}
 
       """
    )
    st.image(image3)

st.write('''
### Training phases
''')
st.write('''
#### Neural network used in the "laptop-price-prediction-and-eda" notebook
The model used for predicting price was a custom one, trained and validated using the keras api from tensorflow. This model uses all the features availible
without discarding any of them.
''')

image4 = Image.open('imgs_exp/nn2_model.png')
st.image(image4)

st.write('''
The training and validation losses looked like this :- 
''')
image5 = Image.open('imgs_exp/nn2_train.png')
st.image(image5)
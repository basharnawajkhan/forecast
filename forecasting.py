import streamlit as st
import pandas as pd


def main():
    st.title("Gold Price Forecasting")
    st.subheader("Predict Gold Price")

    menu = ["Home", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home")
        data = pd.read_excel(r"Gold_data.xlsx")

        if st.button('Show Dataset'):
            st.header('Gold Data')
            st.write(data)

        if st.button("Shape of Dataset"):
            shape = data.shape
            st.write(shape)

        st.subheader("""Dataset Information """)

        col1, col2, col3, col4, col5 = st.columns(5)
        col1.metric("No. of Rows", 2182)
        col2.metric("No. of Columns", 2)
        col3.metric("No. of Duplicate values", 00)
        col4.metric("No. of Null Values", 00)
        col5.metric("No. of Missing Values", 00)

    else:
        st.subheader("About")
        st.write("""P171 Gold Price Prediction
        
        Group - 6       
  
        Mr. Mayuresh Bhoir
        
        Ms. Shruti Dhokale
        
        Mr. Pankaj Mahto
        
        Ms. Jayashri Gurule
        
        Ms.Rohini Arkhade      
         
        Ms. Shital Dhindale
        
        """)

if __name__ == '__main__':
    main()
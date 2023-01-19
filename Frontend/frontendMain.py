import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image
import json
import requests


icon = Image.open("icon.jpg")
st.set_page_config(page_title="Haim's Calculator", page_icon=icon)
backendURL = "http://localhost:8080"


def navigate_pages(page):

    if page == "Math Calculator":

        st.markdown("<b style='color: black; font-size: 25px;'>Enter the first value :</b>",
                    unsafe_allow_html=True)
        num1 = st.number_input(label="", step=0.01, key='a_value')

        st.markdown("<b style='color: black; font-size: 25px;'>Enter the second value :</b>",
                    unsafe_allow_html=True)
        num2 = st.number_input(label="", step=0.01, key='b_value')

        st.markdown("<b style='color: black; font-size: 25px;'>Select one operation:</b>",
                    unsafe_allow_html=True)

        operation = st.selectbox("", ("Add", "Multiply", "Divide",
                                      "Subtract", "power", "A % from B"))
        result = 0

        def calc():

            if operation == "Add":
                a = {
                    "num1": num1, "num2": num2
                }
                result = requests.post(f"{backendURL}/add", json=a).json()

            elif operation == "Multiply":
                a = {"num1": num1, "num2": num2}
                result = requests.post(f"{backendURL}/multy", json=a).json()

            elif operation == "A % from B":
                a = {"num1": num1, "num2": num2}
                result = requests.post(f"{backendURL}/percent", json=a).json()

            elif operation == "Subtract":
                a = {"num1": num1, "num2": num2}
                result = requests.post(f"{backendURL}/sub", json=a).json()

            elif operation == "power":
                a = {"num1": num1, "num2": num2}
                result = requests.post(f"{backendURL}/pow", json=a).json()

            elif operation == "Divide" and num2 != 0:
                a = {"num1": num1, "num2": num2}
                result = requests.post(f"{backendURL}/divide", json=a).json()
            else:
                st.warning("Cant divide by 0 , please enter a legal number")
                result = "Error"

            with st.spinner("Processing..."):
                st.markdown(
                    f"<b style='color: black; font-size: 30px;'>{result[0]}</b>", unsafe_allow_html=True)

        if st.button("Calc result"):
            calc()

    elif page == "Linear plot":

        st.markdown("<b style='color: black; font-size: 25px;'>Enter the first value :</b>",
                    unsafe_allow_html=True)
        num1 = st.number_input(label="", step=0.01, key='a_value')

        st.markdown("<b style='color: black; font-size: 25px;'>Enter the second value :</b>",
                    unsafe_allow_html=True)
        num2 = st.number_input(label="", step=0.01, key='b_value')

        # drawing the linear plot according to the x and y points
        a = {"num1": num1, "num2": num2}
        result = requests.post(f"{backendURL}/linear_plot", json=a).json()
        x_values = result['Res']['x']
        y_values = result['Res']['y']
        fig = plt.figure()
        plt.plot(x_values, y_values)
        plt.xlabel('x-axis')
        plt.ylabel('y-axis')
        plt.title('Linear Plot')
        st.pyplot(fig)
        st.markdown(
            f"<b style='color: black; font-size: 30px;'>The X points are :</b>", unsafe_allow_html=True)
        for i in range(10):
            st.write(result['Res']['x'][i])

        st.markdown(
            f"<b style='color: black; font-size: 30px;'>The Y points are :</b>", unsafe_allow_html=True)
        for j in range(10):
            st.write(result['Res']['y'][j])


# Create a sidebar with buttons to navigate to different pages
st.sidebar.title("Navigation")
page = st.sidebar.selectbox(
    "Select a page", ["Math Calculator", "Linear plot"])
navigate_pages(page)


def add_bg_from_url():  # add backgroung using the web.
    st.markdown(
        f"""
         <style>
         .stApp {{
             background-image: url("https://png.pngtree.com/thumb_back/fh260/background/20200530/pngtree-cute-hand-drawn-style-mathematics-education-pink-background-image_337358.jpg");
             background-attachment: fixed;
             background-size: cover;
             font-size : 40px;
             color : white}}
         </style>
         """,
        unsafe_allow_html=True
    )


add_bg_from_url()

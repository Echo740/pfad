import streamlit as st

st.title("Color Website")

bg_color_picker = st.color_picker("Pick a background color:", "#ffffff")
bg_color_input = st.text_input("Enter a background color name or HEX code (e.g., red or #ff0000):", value=bg_color_picker)

text_colors = ["black", "white", "red", "green", "blue"]
text_color_choice = st.selectbox("Select a text color from the presets:", text_colors)
final_bg_color = bg_color_input if bg_color_input else bg_color_picker

if final_bg_color and text_color_choice:
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-color: {final_bg_color};
            color: {text_color_choice};
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

st.write(f"Current background color: {final_bg_color}")
st.write(f"Current text color: {text_color_choice}")
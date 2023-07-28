"""style_functions.py

This module provides a function to generate a visually appealing metric 
card with a background image.The card includes a title, a value, and an 
optional background image. Customizable style parametersallow users to 
personalize the appearance of the card.

This module requires the `streamlit` library.

Functions:
    metric_card_with_background(title, value, image_url, corner_radius=20, 
                                value_font_size=20, title_font_size=24, 
                                title_color, value_color):
        Generates a metric card with a background image.
"""
import streamlit as st

def metric_card_with_background(title, value,
                                image_url = 'https://www.gstatic.com/webp/gallery/1.jpg',
                                corner_radius=20,
                                value_font_size=20,
                                title_font_size=24,
                                title_color="Turquoise",
                                value_color="HoneyDew"):
    """Generates a metric card with a background image.

    This function creates a metric card with a visually appealing design
    using a background image. The card includes a title, a value, and an
    optional background image. The appearance of the card can be customized
    by adjusting various style parameters.

    Parameters:
    title (str): The title to be displayed on the card.
    value (str): The value to be displayed on the card.
    image_url (str): The URL or local file path of the background image.
    corner_radius (int, optional): The corner radius (in pixels) for the card. 
                                   Default is 20.
    value_font_size (int, optional): The font size (in pixels) for the value. 
                                     Default is 20.
    title_font_size (int, optional): The font size (in pixels) for the title. 
                                     Default is 24.
    title_color (str, optional): The color of the title text. 
                                 Default is "MediumAquamarine".
    value_color (str, optional): The color of the value text. 
                                 Default is "white".

    Returns:
    None: The function renders the metric card directly using Streamlit's
          markdown and HTML features.
    """ 
    st.markdown(
        f"""
        <div style="position: relative; border-radius: {corner_radius}px; overflow: hidden;">
            <img src="{image_url}" alt="Background 
            Image" style="position: absolute; top: 0; left: 0;
            width: 100%; height: 100%; object-fit: cover; filter: brightness(50%);">
            <a href="#" style="position: relative; display: block;
            padding: 16px; color: {title_color}; text-decoration: none;">
                <h3 style="margin: 0; font-size: {title_font_size}px;
                color: {title_color};">{title}</h3>
                <p style="font-size: {value_font_size}px; font-weight: bold; margin: 0;
                color: {value_color};">{value}</p>
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )


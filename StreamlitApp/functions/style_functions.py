import streamlit as st

def style_metric_cards(
    background_color: str = "#FFF",
    border_size_px: int = 1,
    border_color: str = "#D5E7E8",
    border_radius_px: int = 2,
    border_left_color: str = "#37C9DE",
    box_shadow: bool = True,
):

    box_shadow_str = (
        "box-shadow: 0 0.15rem 1.75rem 0 rgba(58, 59, 69, 0.15) !important;"
        if box_shadow
        else "box-shadow: none !important;"
    )
    st.markdown(
        f"""
        <style>
            div[data-testid="metric-container"] {{
                background-color: {background_color};
                border: {border_size_px}px solid {border_color};
                padding: 5% 5% 5% 10%;
                border-radius: {border_radius_px}px;
                border-left: 0.5rem solid {border_left_color} !important;
                {box_shadow_str}
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )


# def metric_card_with_background(title, value, image_url, corner_radius=8, value_font_size=24, title_font_size=24, title_color="white", value_color="white"):
#     st.markdown(
#         f"""
#         <div style="position: relative; border-radius: {corner_radius}px; overflow: hidden;">
#             <img src="{image_url}" alt="Background Image" 
#             style="position: absolute; top: 0; left: 0; width: 100%; 
#             height: 100%; object-fit: cover; filter: brightness(50%);">
#             <a href="#" style="position: relative; display: flex; 
#             flex-direction: column; justify-content: center; 
#             align-items: center; padding: 16px; color: {title_color}; 
#             text-decoration: none;">
#                 <h3 style="margin: 0; font-size: {title_font_size}px; 
#                 color: {title_color};">{title}</h3>
#                 <p style="font-size: {value_font_size}px; font-weight: bold; margin: 0; 
#                 color: {value_color};">{value}</p>
#             </a>
#         </div>
#         """,
#         unsafe_allow_html=True
#     )

def metric_card_with_background(title, value, image_url, corner_radius=8, value_font_size=24, title_font_size=24, title_color="white", value_color="white"):
    st.markdown(
        f"""
        <div style="position: relative; border-radius: {corner_radius}px; overflow: hidden;">
            <img src="{image_url}" alt="Background Image" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; object-fit: cover; filter: brightness(50%);">
            <a href="#" style="position: relative; display: block; padding: 16px; color: {title_color}; text-decoration: none;">
                <h3 style="margin: 0; font-size: {title_font_size}px; color: {title_color};">{title}</h3>
                <p style="font-size: {value_font_size}px; font-weight: bold; margin: 0; color: {value_color};">{value}</p>
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )
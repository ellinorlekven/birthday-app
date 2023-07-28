import streamlit as st
from streamlit_card import card
import pandas as pd
from datetime import date, timedelta, datetime
import functions.data_functions as dd
import functions.age_functions as af
from functions import style_functions
from functions.data_functions import jubilees_dict


# Configurating app
st.set_page_config(layout='wide', initial_sidebar_state='auto')
st.write('# My birthday app')
st.expander('Juicy deets')
with st.expander('Juicy deets'):
    st.write('Hello my friend. Do you want to have lunch?')

# with open('style.css', encoding='utf-8') as f:
#     st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Sidebar
st.sidebar.header('Dashboard `version 0`')
st.sidebar.write('Fill in name and birthdays for your group.')

# Add a birthdayselector to the sidebar
st.sidebar.subheader('Enter birthdays')
data_df = pd.DataFrame(
    {
        "Name": ['Ola'],
        "birthday": [date(2000, 1, 1)]
    }
)
data_df = st.sidebar.data_editor(
    data_df,
    column_config={
        "birthday": st.column_config.DateColumn(
            "Birthday",
            min_value=date(1900, 1, 1),
            max_value=date.today(),
            format="DD.MM.YYYY",
            step=1
            
        ),
    },
    hide_index=True,
    num_rows="dynamic"
)

data_df = data_df.dropna()

# Making the dict that is essential for the rest of the application
birthday_dict = {}
for _, row in data_df.iterrows():
    name = row[0]
    birthday = row[1]
    birthday_dict[name] = birthday

# Add a selectbox to the sidebar
family_jub_dict = af.get_familiy_jubilee(birthday_dict, jubilees_dict)
st.sidebar.subheader('Jubilee selection')
jub_selector = st.sidebar.selectbox('Select a jubilee to celebrate', list(family_jub_dict.keys()))

# Add a selectbox to the sidebar:
converted_age_dict =  af.get_converted_age(birthday_dict)
st.sidebar.subheader('Person selection')
person_selector = st.sidebar.selectbox('Select a person for more details', list(converted_age_dict.keys()))

# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

st.sidebar.markdown('''
---
❤️ Created by [Ellinor Lekven Sætre](https://www.linkedin.com/in/ellinorlekvensaetre/).
''')


average_age_tup = af.get_average_age(birthday_dict)
# converted_age_str, converted_age_dict  = af.get_converted_age(birthday_dict)



# Row A
container1 = st.container()

with container1:
    col1, col2, col3 = st.columns(3)
    average_dob_str, average_dob_date = af.get_average_dob(birthday_dict)
    with col1:
        style_functions.metric_card_with_background(
            title="Average birthay of group", 
            value=average_dob_date, 
            image_url='https://www.gstatic.com/webp/gallery/1.jpg',
            corner_radius=20,
            value_font_size=20,
            title_font_size=22,
            title_color="MediumAquamarine",
            value_color="white")

    total_age_tup= af.get_total_age(birthday_dict)
    with col2:
        style_functions.metric_card_with_background(
            title="Total age of family", 
            value=f'{total_age_tup[0]} years, {total_age_tup[1]} weeks and {total_age_tup[2]} days',
            image_url='https://www.gstatic.com/webp/gallery/1.jpg',
            corner_radius=20,
            value_font_size=20,
            title_font_size=22,
            title_color="MediumAquamarine",
            value_color="white")
        
    with col3:
        style_functions.metric_card_with_background(
            title= f'Date of {jub_selector} jubilee',
            value=family_jub_dict[jub_selector][1],
            image_url='https://www.gstatic.com/webp/gallery/1.jpg',
            corner_radius=20,
            value_font_size=20,
            title_font_size=22,
            title_color="MediumAquamarine",
            value_color="white")

# Add spave
container2 = st.container()
with container2:
    st.write(' ')


# Row B
container3 = st.container()

with container3:
    c1, c2 = st.columns(2)

    average_age_tup = af.get_average_age(birthday_dict)
    with c1:
        style_functions.metric_card_with_background(
            title="Average age of family", 
            value=f'{average_age_tup[0]} years, {average_age_tup[1]} weeks and {average_age_tup[2]} days', 
            image_url='https://www.gstatic.com/webp/gallery/1.jpg',
            corner_radius=20,
            value_font_size=20,
            title_font_size=22,
            title_color="MediumAquamarine",
            value_color="white")  
    
    converted_age_dict  = af.get_converted_age(birthday_dict)
    with c2:
        style_functions.metric_card_with_background(
            title=f'{person_selector}\'s age',
            value= converted_age_dict[person_selector],
            image_url='https://www.gstatic.com/webp/gallery/1.jpg',
            corner_radius=20,
            value_font_size=20,
            title_font_size=22,
            title_color="MediumAquamarine",
            value_color="white")  

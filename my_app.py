"""Birthday App Module

This module contains the Streamlit application code for the "My birthday app" 
that allows users to calculate the collective age of a group. The app includes 
functionality to input names and birthdays of group members, select a person to 
display individual age, and choose jubilees to celebrate. The app displays metric 
cards with various information, such as average birthday, total age of the family, 
average age of the family, and the selected person's age.

Required Libraries:
    - `datetime` from `datetime`: Used to work with dates.
    - `streamlit` as `st`: Used to build the web app.
    - `pandas` as `pd`: Used to handle tabular data.
    - `functions.age_functions` as `af`: Contains custom functions related to age calculations.
    - `functions.style_functions` as `sf`: Contains custom functions for styling metric cards.

App Configuration:
    - Sets the page layout to 'wide'.
    - Includes a title for the app.
    - Provides an expander for additional descriptions.
    - Uses Streamlit sidebar for data input and selection.

Notes:
    - The app utilizes the `data_editor` feature of Streamlit's sidebar to 
      allow users to enter names and birthdays.
    - The `average_age_tup` variable is used to calculate the average age of the family.
    - The `birthday_dict` variable is used to store the names and birthdays of group members.
    - The `family_jub_dict` variable is used to store jubilee information.
    - The app makes use of custom functions from the `af` and `sf` modules for age 
      calculations and styling, respectively.

Author:
    - Ellinor Lekven Sætre (LinkedIn: https://www.linkedin.com/in/ellinorlekvensaetre/)

"""
from datetime import date
import streamlit as st
import pandas as pd
from functions import age_functions  as af
from functions import style_functions as sf

# Configurating app
st.set_page_config(layout='wide', initial_sidebar_state='auto')
st.write('# My birthday app')
st.expander('Descriptions')
with st.expander('Why do you need a birthday app?'):
    st.write('This is an application that is made for calculating the collective age of a group. '
              'The motivation behind the app is to have more occations to celebrate life together '
              'and not only the individual birthday parties. I hope this app will give you an '
              'increased amount of days to celebrate whenever you or your friends and family '
              'feel like it.'
              )

# with open('style.css', encoding='utf-8') as f:
#     st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Sidebar
st.sidebar.header('Dashboard `version 1.0`')
st.sidebar.write('Fill in name and birthdays for your group.')

# Add a dataframe input to the sidebar
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

# Making a dict with all the birthdays from the input df
birthday_dict = {}
for _, row in data_df.iterrows():
    name = row[0]
    birthday = row[1]
    birthday_dict[name] = birthday

# Add a person selectbox to the sidebar:
converted_age_dict =  af.get_converted_age(birthday_dict)
st.sidebar.subheader('Person selection')
person_selector = st.sidebar.selectbox('Select a person to show individual age',
                                       list(converted_age_dict.keys()))

# Define input for the jubilee selector
TWENTYFIVE = 36524.2199/4

jubilees_dict = {}
for i in range(40):
    years = (i + 1) * 25
    key = f'{years} years'
    value = TWENTYFIVE * (i + 1)
    jubilees_dict[key] = value

# Add a jubilee selectbox to the sidebar
family_jub_dict = af.get_familiy_jubilee(birthday_dict, jubilees_dict)
st.sidebar.subheader('Jubilee selection')
jub_selector = st.sidebar.selectbox('Select a jubilee to celebrate',
                                    list(family_jub_dict.keys()))

# Add credientals to the sidebar
st.sidebar.markdown('''
---
❤️ Created by [Ellinor Lekven Sætre](https://www.linkedin.com/in/ellinorlekvensaetre/).
''')


# Row A
container1 = st.container()

with container1:
    col1, col2, col3 = st.columns(3)
    average_dob = af.get_average_dob(birthday_dict)
    with col1:
        sf.metric_card_with_background(
            title="Average birthay of group",
            value=average_dob)

    total_age_tup= af.get_total_age(birthday_dict)
    with col2:
        sf.metric_card_with_background(
            title="Total age of family", 
            value=f'{total_age_tup[0]} years {total_age_tup[1]} weeks and {total_age_tup[2]} days')
    with col3:
        sf.metric_card_with_background(
            title= f'Date of {jub_selector} jubilee',
            value=family_jub_dict[jub_selector][1])

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
        sf.metric_card_with_background(
            title="Average age of family", 
            value=f'{average_age_tup[0]} years {average_age_tup[1]}'
            f'weeks and {average_age_tup[2]} days')
    converted_age_dict  = af.get_converted_age(birthday_dict)
    with c2:
        sf.metric_card_with_background(
            title=f'{person_selector}\'s age',
            value= converted_age_dict[person_selector])

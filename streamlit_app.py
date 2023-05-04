import streamlit

streamlit.title('Beans means Heinz')

streamlit.header('Whats for brekkie today?')

streamlit.text('- 🥣 Nuttty Granola with Peanut Butter and Full fat Greek Yoghurt')
streamlit.text('- Cup of tea with full-fat milk')   
streamlit.header('OR')
streamlit.text('- 🥑Avocado, Cooked Tomato, olive oil and chorizo bagels')
streamlit.header('OR')
streamlit.text('-🍞🐔🥗Omlette with veg and toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas as pd 
my_fruit_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
my_fruit_list = my_fruit_list.set_index('Fruit')

streamlit.header('Pick list here')

fruits_selected = streamlit.multiselect('Pick some fruits:', list(my_fruit_list.index),['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)

streamlit.header('Fruityvice advice')

fruit_choice = streamlit.text_input('What fruit would you like info about?','kiwi')
streamlit.write('The user has entered',fruit_choice)

import requests 

fruityvice_response = requests.get("https://www.fruityvice.com/api/fruit/"+ fruit_choice)

fruity_normal = pd.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruity_normal)

import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * FROM FRUIT_LOAD_LIST")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit list contains:")
streamlit.dataframe(my_data_rows)

add_my_fruit = streamlit.text_input('What fruit would you like to add?','jackfruit')
streamlit.text('Thanks for adding ', add_my_fruit)

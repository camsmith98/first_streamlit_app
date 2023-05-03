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

#Pick list here

fruits_selected = streamlit.multiselect('Pick some fruits:', list(my_fruit_list.index),['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)

import requests 

fruityvice_response = requests.get('https://www.fruityvice.com/api/fruit/raspberry')
streamlit.text(fruityvice_response.json())

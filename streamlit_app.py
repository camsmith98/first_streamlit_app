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


#Pick list here

streamlit.multiselect('Pick some fruits:', list(my_fruit_list.index))

streamlit.dataframe(my_fruit_list)

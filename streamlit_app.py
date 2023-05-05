import streamlit
import snowflake.connector
import requests 
import pandas as pd 
from urllib.error import URLError

streamlit.title('Beans means Heinz')

streamlit.header('Whats for brekkie today?')

streamlit.text('- 🥣 Nuttty Granola with Peanut Butter and Full fat Greek Yoghurt')
streamlit.text('- Cup of tea with full-fat milk')   
streamlit.header('OR')
streamlit.text('- 🥑Avocado, Cooked Tomato, olive oil and chorizo bagels')
streamlit.header('OR')
streamlit.text('-🍞🐔🥗Omlette with veg and toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


my_fruit_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
my_fruit_list = my_fruit_list.set_index('Fruit')

streamlit.header('Pick list here')

fruits_selected = streamlit.multiselect('Pick some fruits:', list(my_fruit_list.index),['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)

#new section for fruityvice 

def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://www.fruityvice.com/api/fruit/"+ this_fruit_choice)
    fruity_normal = pd.json_normalize(fruityvice_response.json())
    return fruity_normal

#new section displays fruitvice api   

streamlit.header('Fruityvice advice')

try:
   fruit_choice = streamlit.text_input('What fruit would you like info about?')
   if not fruit_choice:
         streamlit.error('plesae select a fruit to get information')
   else:
        back_from_function = get_fruityvice_data(fruit_choice)
        streamlit.dataframe(back_from_function)
        
except:
    pass
        


#snowflake functions
streamlit.header("The fruit list contains:")

def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
        my_cur.execute("select * from fruit_load_list")
        return my_cur.fetchall()
    
  
   
 #add a button to load the fruit
 if streamlit.button('get fruit load list'):
      my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
      my_data_rows = get_fruit_load_list()
      streamlit.dataframe(my_data_rows)
    
 
def insert_row_snowflake(new_fruit):
   with my_cnx.cursor() as my_cur:
      my_cur.execute("INSERT INTO PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST VALUES ('from streamlit')")
      return "thanks for adding " + new_fruit

add_my_fruit = streamlit.text_input('What fruit would you like to add?')
if streamlit.button('add a fruit to the list'):
   my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
   back_from_function = insert_row_snowflake(add_my_fruit)
   streamlit.text(back_from_function)




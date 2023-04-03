import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('My Mom\'s New Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#Read file from stage into pandas dataframe
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
#try removing the list of fruits
#fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
#streamlit.dataframe(my_fruit_list)
streamlit.dataframe(fruits_to_show)

#New Sectioin to display fruityvice api response
streamlit.header("Fruityvice Fruit Advice!")

#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
#streamlit.text(fruityvice_response.json())

#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")



#New section to add Text Entry Box
#fruit_choice = streamlit.text_input('What fruit would you like information about?', 'Kiwi')
#streamlit.write('The user entered', fruit_choice)
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

#take the json version of the response and normalize it
#fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())

#output it to the screen as table
#streamlit.dataframe(fruityvice_normalized)

#streamlit.stop()
#my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
#my_cur = my_cnx.cursor()
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
#my_data_row = my_cur.fetchone()
#streamlit.text("Hello from Snowflake:")
#streamlit.text(my_data_row)
#my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
#my_data_row = my_cur.fetchall()
#streamlit.header("The fruit load list contains:")
#streamlit.dataframe(my_data_row)

#New section to add Text Entry Box
#fruit_choice = streamlit.text_input('What fruit would you like to add?')
#streamlit.write('The user entered', fruit_choice)
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
#streamlit.write("Thanks for adding " + fruit_choice)

#my_cur.execute("insert into fruit_load_list values('from streamlit')")

def get_fruityvice_data(this_fruit_choice):
    fruitvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
    fruitvice_normalized = pandas.json_normalize(fruityvice_respons.json())
    return fruitvice_normalized
  
try:
  fruit_choice = streamlit.text_input('What fruid would you like information about?')
  if not fruit_choice:
      streamlit.error("Please select a fruit to get information")
  else:
    back_from_function = get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)


except URLError as e:
  streamlit.error()











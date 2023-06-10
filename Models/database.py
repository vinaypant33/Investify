import sqlite3 
import datetime



conn  = sqlite3.connect('investify_manager.db')
c = conn.cursor()

# Function to be called to save from the database
def saving_details():
    conn.commit()



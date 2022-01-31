from flask import g
import sqlite3

def get_message_db():
    g.message_db = sqlite3.connect("message_db.sqite") 
    cursor = g.message_db.cursor()
    cursor.execute("create table if not exists messages(Id integer, handle text, message text)")
    cursor.close()
    
    

def insert_message(request):
    get_message_db()
    message = request.form['message']
    handle = request.form['user']
    #if both message and handle exists,we store them into a database
    if (message and handle):
        cursor = g.message_db.cursor()
        cursor.execute("select count(*) from messages")
        #we want to fetch the message and store it in result.
        #First we have to know that the messages are stored as list of tuples in the database.
        #We fetch the first tuple using [0] and we add one to get the 'true' number, 
        #since in a list, the first one is numbered as zero.
        result = cursor.fetchone()[0]+1
        g.sql = 'insert into messages(Id,handle,message) values('+str(result)+',"'+handle+'","'+message+'")'
        cursor.execute(g.sql)
        g.message_db.commit()
        cursor.close()
        g.message_db.close()
    

#We define a function that fetches our data randomly 
def random_messages(n):
    g.message_db = sqlite3.connect("message_db.sqite") 
    cursor = g.message_db.cursor()
    #using the sql command to fetch our text randomly
    cursor.execute("select message,handle  from messages ORDER BY RANDOM()") 
    result = cursor.fetchmany(n)
    cursor.close()
    g.message_db.close()
    return result

   
    
    
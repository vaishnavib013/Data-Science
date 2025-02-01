# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 10:37:44 2024

@author: Vaishnavi
"""

#after installing with pip install psycopg2
import psycopg2 as pg2

#create a connection with postgreSQL
#'Password' is whatever you set ,we set password in the install via  
conn=pg2.connect(database='dvdrental',user='postgres',password='root')

#establish connection and start cusrsor to be ready to query
cur=conn.cursor()
#pass in a pstgresql query as a string
cur.execute("SELECT * FROM payment")

#RETURN A tuple of the first row as python objects
cur.fetchone()
#returning N number of rows
cur.fetchmany(10)

#return all rows at once
cur.fetchall()

#to save and index results,assign it to a variable
data=cur.fetchmany(10)
#it is mandatory to close the connection
conn.close()
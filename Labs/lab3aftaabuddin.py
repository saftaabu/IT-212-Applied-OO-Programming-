# Syed Aftaabuddin
# Lab 3
# May 16, 2020

# Script to read greeting from the web.
from urllib.request import urlopen
import json
import sqlite3
import sys


# Define url of webpage to read
url = "http://facweb.cdm.depaul.edu/sjost/it212/rates.txt"

# Open input stream
input_stream = urlopen(url)

# Initialize dictionary
d = dict( )

for line in input_stream:
    decoded_chars = line.decode("utf-8-sig").strip( )
    fields = decoded_chars.split(",")
    code = fields[0]
    rate = float(fields[1])
    d[code] = rate

input_stream.close( )

print(d)


# Create an SQL table using data read from keyboard

import sqlite3

conn = sqlite3.connect('lab3transactions.db')
cur = conn.cursor( )

# Create transaction table.
#name date  source_currency  target_currency  source_amount  
#source_exchange_rate  target_exchange_rate  target_amount


cur.execute( \
    '''create table if not exists transactions(
           name varchar(15),
           date varchar(11),
           source_currency varchar(3),
           target_currency varchar(3),
           source_amount float,
           source_exchange_rate float,
           target_exchange_rate float,
           target_amount float );''')


# Read data from keyboard.
#Input
#customer name, current date
#source currency, target currency, source amount

name = input('Enter customer name: ')
date = input('Enter current date: ')
sc = input('Enter source currency: ')
tc = input('Enter target currency: ')
sa = float(input('Enter source amount: '))


if sc in d:
    sr = d[sc]
else:
    print('Source currency not in dictionary')
    sys.exit( )

if tc in d:
    tr = d[tc]
else:
    print('Target currency not in dictionary')
    sys.exit( )
    

# Compute target amount from formula:
ta = tr * sa / sr

          
# Insert values into database.
cur.execute(f'''insert into transactions values(
  '{name}', '{date}', '{tc}', '{sc}', {sa}, {sr}, {tr}, {ta});''') #printing out values from the database

# Commit changes.
conn.commit( )

# Query transactions table.
cur.execute("select * from transactions;")

# Print results from query
print(cur.fetchall( ))

# Close database.
conn.close( )

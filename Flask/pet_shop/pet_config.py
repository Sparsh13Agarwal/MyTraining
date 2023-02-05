import psycopg2
from psycopg2 import Error

# function for db connection details
def dbConnection():

    dbDict = {
    "user":"postgres",
    "password":"Finserv@2023",
    "database":"pet_animal"
    }
    return dbDict


def create_table():
    create_table = {
        "table_name": "pet_info",
        "pet_id": "serial primary key",
        "pet_name":"varchar",
        "pet_type":"varchar",
        "pet_breed": "varchar", 
        "pet_color" :"varchar",
        "pet_owner_name": "varchar"
    }
    return create_table , list(create_table.keys())


# table_info,table_keys = create_table()

def create_table_query(table_info, table_keys):

    str=""
    for i in table_keys[1:]:
        str = str+i+" "+table_info[i]
        if(table_keys.index(i) != len(table_keys)-1):
            str+=","
    return str

def insert_table_query(table_keys):
    str=""
    for i in table_keys[2:]:
        str = str+i+" "
        if(table_keys.index(i) != len(table_keys)-1):
            str+=","
    return str




import psycopg2
from psycopg2 import Error
import pet_config


var = pet_config.dbConnection()
table_info,table_keys = pet_config.create_table()
create_table_query = pet_config.create_table_query(table_info,table_keys)
insert_table_query = pet_config.insert_table_query(table_keys)
#print(insert_table_query)

#print(str)
class DBConnection:
    
    cur = None
    conn = None
    def __init__(self) -> None:
        pass
    @classmethod
    def connect_db(cls):
        cls.conn = psycopg2.connect(user=var["user"],password=var["password"],database=var["database"])
        cls.cur = cls.conn.cursor()

    @classmethod
    def create_table(cls):
        try:
            cls.cur.execute(f'create table pet_info ({create_table_query});')
            cls.conn.commit()
        except psycopg2.Error as er:
            print("error: ",er)


    @classmethod
    def select_records(cls,tablename):
        cls.cur.execute(f'select * from {tablename};')
        pets = cls.cur.fetchall()
        for pet in pets:
            print(pet)
    @classmethod
    def insert_record(cls,tablename,p_name,p_type,p_breed,p_color,p_owner):
        cls.cur.execute(f"insert into {tablename}({insert_table_query}) values('{p_name}','{p_type}','{p_breed}','{p_color}','{p_owner}');")
        cls.conn.commit()
    @classmethod
    def update_record(cls,tablename,p_id,p_name):
        try:
            cls.cur.execute(f"select {tablename} from pet_info where pet_id ={p_id} ")
            if len(cls.cur.fetchall()) == 1:
                cls.cur.execute(f"update {tablename} set pet_name = '{p_name}' where pet_id = {p_id}")
                cls.conn.commit()
                return True
            else:
                return
        except psycopg2.Error as er:
            print('error',er)
    @classmethod
    def fetchall_record(cls,tablename):
        cls.cur.execute(f'SELECT * FROM {tablename};')
        data = cls.cur.fetchall()
        return data
    @classmethod
    def delete_record(cls,tablename,p_id):
        cls.cur.execute(f"delete from {tablename} where pet_id = {p_id};")
        cls.conn.commit()
    @classmethod
    def clos_connection(cls):
        cls.conn.close()

    
    
# if __name__=='__main__':
#     db = DBConnection()
#     db.connect_db()
#     db.create_table()



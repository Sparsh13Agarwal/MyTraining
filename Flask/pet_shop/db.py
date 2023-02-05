import psycopg2
       
class DBConnection:
    conn = None
    cur = None
    def __init__(self,) -> None:
        pass
    @classmethod
    def connect_db(cls):
        cls.conn = psycopg2.connect(user="postgres",password="Finserv@2023",database="postgres")
        cur = cls.conn.cursor()
    @classmethod
    def create_table(cls,tablename,f1,f2,f3):
        cls.cur.execute(f'create table {tablename} ({f1} varchar primary key,{f2} varchar, {f3} varhchar)')
        cls.conn.commit()

    @classmethod
    def select_records(cls,tablename):
        cls.cur.execute(f'select * from {tablename};')
        students = cls.cur.fetchall()
        for student in students:
            print(student)
    
    @classmethod
    def insert_record(cls,tablename,f1,f2,f3):
        cls.cur.execute(f'insert into {tablename} values({f1},{f2},{f3})')
        cls.conn.commit()

    @classmethod
    def update_record(cls,tablename,f1,v1,f2,v2):
        cls.cur.execute(f'update {tablename} set {f1} = {v1} where {f2} = {v2}')

    @classmethod
    def clos_connection(cls):
        cls.conn.close()

    
    # if __name__=='__main__':

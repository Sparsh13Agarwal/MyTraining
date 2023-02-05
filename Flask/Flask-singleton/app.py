class DBSingleton:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            print("creating object")
            cls._instance = super(DBSingleton,cls).__new__(cls)

        return cls._instance

ob1 = DBSingleton()
ob2 = DBSingleton()
print(ob1 == ob2)
print(ob1,ob2)




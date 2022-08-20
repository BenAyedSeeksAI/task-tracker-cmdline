from datetime import datetime
import sqlite3


Filename = "tasks.db"

class DbConnectionManger(object):
    def __init__(self, filename):
        self.filename = filename

    def commit(operation):
        def wrapper(self, *args, **kwargs):
            self.data = operation(self, *args, **kwargs)
            self.connection.commit()
            print(f"{datetime.now()}: Commit is successful!!")
        return wrapper
    
    def __enter__(self):
        print("Connection started ...")
        self.connection = sqlite3.connect(self.filename)
        self.cursor = self.connection.cursor()
        self.data = None
        return self
    
    @commit
    def getObjects(self):
        command = "SELECT * FROM Task"
        data = None
        try:
            self.cursor.execute(command)
            data = self.cursor.fetchall()
        except sqlite3.Error as er:
            print(f"SQLite error: {' '.join(er.args)}")
        finally:
            print(f"Data Retrieved ... ")
        return data
        

    @commit
    def insertRow(self, task):
        command = f"INSERT INTO Task(task_name, category) VALUES('"+ str(task.task_name) +"', '"+ str(task.category) +"')"
        try:
            self.cursor.execute(command)
        except sqlite3.Error as er:
            print(f"SQLite error: {' '.join(er.args)}")
        finally:
            print(f"Row created successfully!")


    def __exit__(self,type, value, traceback):
        print("Connection closed ...")
        self.connection.close()

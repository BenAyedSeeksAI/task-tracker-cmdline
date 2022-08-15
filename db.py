import datetime
import sqlite3

from model import Task

Filename = "tasks.db"

class DbConnectionManger:
    def __init__(self, filename):
        self.filename = filename

    def commit(operation):
        def wrapper(self, *args, **kwargs):
            operation(self, *args, **kwargs)
            self.connection.commit()
            print(f"{datetime.datetime.now()}: Commit is successful!!")
        return wrapper
    
    def __enter__(self):
        print("Connection started ...")
        self.connection = sqlite3.connect(self.filename)
        self.cursor = self.connection.cursor()
        return self

    @commit
    def insertRow(self, task : Task):
        command = f"INSERT INTO projects(task_name, category) VALUES({task.task_name},{task.category});"
        try:
            self.cursor.execute(command)
        except sqlite3.Error as er:
            print(f"SQLite error: {' '.join(er.args)}")
        finally:
            print(f"Row created successfully!")

    def __exit__(self):
        print("Connection closed ...")
        self.connection.close()
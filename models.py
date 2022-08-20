from dataclasses import dataclass
from db import DbConnectionManger,Filename

@dataclass
class Task:
    task_name: str
    category: str
    def save(self):
        with DbConnectionManger(filename=Filename) as Conn:
            Conn.insertRow(self)
    @classmethod
    def objects(cls):
        data = None
        with DbConnectionManger(filename = Filename) as Conn:
            Conn.getObjects()
            data = Conn.data
        return data

from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel


class Employee(BaseModel):
    name:str
    age:int
    salary: int
    address: Union[str,None] = None


app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.post("/employee")
def add_emp_record(empRecord:Employee):
    return {"name": empRecord.name,"age":empRecord.age}


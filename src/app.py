from fastapi import FastAPI
from uuid import UUID, uuid4
from Classes.Computer import Computer
from src.models.Computer import ComputerORM

storage = {}

app = FastAPI()

@app.post("/crate_computer")
async def create_computer():
    computer = Computer()
    computer_orm = ComputerORM(computer=computer)
    storage[computer_orm.id] = computer_orm.computer
    return computer_orm.id

@app.get("/computers")
def get_computers():
    return storage

@app.get("/repr_computer/{id}")
def repr_computer(id: UUID):
    computer = storage[id]  
    return computer.comp_repr()

@app.post("/command/{id}")
def command(id: UUID, command: str):
    computer = storage[id]
    return computer.command(command)

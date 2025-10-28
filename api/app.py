from fastapi import FastAPI
from uuid import UUID, uuid4
from Classes.Computer import Computer
from api.models.Computer import ComputerORM

app = FastAPI()

@app.post("/crate_computer/")
async def create_computer():
    computer = Computer()
    computer_orm = ComputerORM(id=uuid4(), computer=computer)
    return computer


from uuid import UUID, uuid4
from pydantic import BaseModel, ConfigDict

from Classes import Computer

class ComputerORM(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    id: UUID = uuid4()
    computer: Computer = None

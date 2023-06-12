from pydantic import BaseModel

class ProjectDetails (BaseModel):
    name: str
    budget: int
    duration: int
    strict: bool
    
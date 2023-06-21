from pydantic import BaseModel

# Fields required by default
class ProjectDetails (BaseModel):
    name: str
    budget: int
    duration: int
    strict: bool
    
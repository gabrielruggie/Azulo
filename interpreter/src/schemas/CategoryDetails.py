from pydantic import BaseModel

class CategoryDetails (BaseModel):
    name: str
    budget_allocation: float
    strict: bool
    
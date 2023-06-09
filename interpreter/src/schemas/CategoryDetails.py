from pydantic import BaseModel

class CategoryDetails (BaseModel):
    budget_allocation: float
    strict: bool
    
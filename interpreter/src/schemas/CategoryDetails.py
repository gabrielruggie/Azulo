from pydantic import BaseModel

class CategoryDetails (BaseModel):
    name: str
    allocation_amt: float
    strict: bool
    
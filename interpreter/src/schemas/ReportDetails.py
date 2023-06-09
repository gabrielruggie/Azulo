from interpreter.src.schemas.GetOperationDetails import GetOperationDetails
from pydantic import BaseModel
from typing import List

class ReportDetails (BaseModel):
    always_run: bool
    actions: List[GetOperationDetails]


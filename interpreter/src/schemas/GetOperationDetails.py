from pydantic import BaseModel

class GetOperationDetails (BaseModel):
    module_type: str
    module_name: str
    module_attribute: str

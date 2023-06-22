class ValidationError (Exception):
    pass

class InvalidModuleFieldError (ValidationError):
    
    def __init__(self, module_type: str):
        self.message: str = f'One or more fields provided are not valid for module type: {module_type}'
        super().__init__(self.message)


class InvalidModuleTypeError (ValidationError):
    
    def __init__(self, module_type: str):
        self.message: str = f'The module type: {module_type} is not a valid module type!'
        super().__init__(self.message)
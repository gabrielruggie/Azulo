
class InvalidModuleFieldError (Exception):
    
    def __init__(self, module_type: str):
        self.message: str = f'One or more fields provided are not valid for module type: {module_type}'
        super().__init__(self.message)
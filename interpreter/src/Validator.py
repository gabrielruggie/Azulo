from interpreter.src.exceptions.ValidatorExceptions import *
from interpreter.src.schemas.ProjectDetails import ProjectDetails
from interpreter.src.schemas.CategoryDetails import CategoryDetails
from loguru import logger

class Validator:

    def __init__ (self, mod_objects: list):
        self.__mod_objects: list = mod_objects
        self.__azm_lines: list = []

    def __validate_project_details (self, module_type:str, module: dict) -> None:

        try:

            new_project:ProjectDetails = ProjectDetails(**module)
            project_azm = f'project name:{new_project.name} budget:{new_project.name} duration:{new_project.duration} strict:{new_project.strict}'
            self.__azm_lines.append(project_azm)
        
        except Exception as e:
            logger.debug(e)
            raise InvalidModuleFieldError(module_type=module_type)

    def __validate_category_details (self, module_type: str, module: dict) -> None:
        
        try:

            new_category: CategoryDetails = CategoryDetails(**module)
            category_azm = f'category name:{new_category.name} allocation_amt:{new_category.allocation_amt} strict:{new_category.strict}'
            self.__azm_lines.append(category_azm)
        
        except Exception as e:
            logger.debug(e)
            raise InvalidModuleFieldError(module_type=module_type)

    def __schema_controller (self, module_type: str, module: dict) -> None:

        match module_type:

            case "project": self.__validate_project_details(module_type=module_type, module=module)

            case "category": self.__validate_category_details(module_type=module_type, module=module)

            case "report": pass

            case other: pass

    def validate (self):

        for module in self.__mod_objects:

            module_type: str = module['type']
            self.__schema_controller(module_type=module_type)





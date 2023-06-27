from interpreter.src.exceptions.ValidatorExceptions import *
from interpreter.src.schemas.ProjectDetails import ProjectDetails
from interpreter.src.schemas.CategoryDetails import CategoryDetails
from interpreter.src.schemas.ReportDetails import ReportDetails
from interpreter.src.AzmConstructor import AzmConstructor

from typing import List
from loguru import logger

class Validator:

    def __init__ (self):
        self.__mod_objects: List[dict] = None
        self.__azm_lines: list = []
        self.__azm_constructor = AzmConstructor()

    def set_module_dict_objects (self, module_dict_objects: List[dict]) -> None:
        self.__mod_objects = module_dict_objects

    def __validate_project_details (self, module_type:str, module: dict) -> None:

        try:

            new_project: ProjectDetails = ProjectDetails(**module)
            project_azm: str = self.__azm_constructor.project_azm_constructor(project_details=new_project)
            self.__azm_lines.append(project_azm)
        
        except Exception as e:
            logger.debug(str(e))
            raise InvalidModuleFieldError(module_type=module_type)

    def __validate_category_details (self, module_type: str, module: dict) -> None:
        
        try:

            new_category: CategoryDetails = CategoryDetails(**module)
            category_azm: str = self.__azm_constructor.category_azm_constructor(category_details=new_category)
            self.__azm_lines.append(category_azm)
        
        except Exception as e:
            logger.debug(e)
            raise InvalidModuleFieldError(module_type=module_type)
    
    def __validate_report_details (self, module_type: str, module: dict) -> None:

        try:

            # See if this works. Otherwise, may need to iterate over `actions` and add a List[GetOperationDetails] argument
            # to the report constructor
            new_report: ReportDetails = ReportDetails(**module)
            report_azm: str = self.__azm_constructor.report_azm_constructor(report_details=new_report)
            self.__azm_lines.append(report_azm)
        
        except Exception as e:
            logger.debug(e)
            raise InvalidModuleFieldError(module_type=module_type)

    def __schema_controller (self, module_type: str, module: dict) -> None:

        match module_type:

            case "project": self.__validate_project_details(module_type=module_type, module=module)

            case "category": self.__validate_category_details(module_type=module_type, module=module)

            case "report": self.__validate_report_details(module_type=module_type, module=module)

            case other: 
                logger.debug(f'{module_type} is not a valid module type declaration')
                raise InvalidModuleTypeError(module_type=module_type)

    def validate (self) -> List[str]:

        for module in self.__mod_objects:

            module_type: str = module['type']
            self.__schema_controller(module_type=module_type, module=module)
        
        return self.__azm_lines


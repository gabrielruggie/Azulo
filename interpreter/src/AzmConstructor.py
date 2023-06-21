from interpreter.src.schemas.ProjectDetails import ProjectDetails
from interpreter.src.schemas.CategoryDetails import CategoryDetails
from interpreter.src.schemas.ReportDetails import ReportDetails

from loguru import logger

class AzmConstructor:

    @staticmethod
    def project_azm_constructor (project_details: ProjectDetails) -> str:

        starter: str = "project "
        # Required fields
        name: str = f'name:{project_details.name} '
        budget: str = f'budget:{project_details.budget} '
        duration: str = f'duration:{project_details.duration} '
        strict: str = f'strict:{project_details.strict} '

        # Optional fields
        # Comming eventually. Optional fields will have default values and will always be added to the final string

        azm: str = starter + name + budget + duration + strict

        return azm
    
    @staticmethod
    def category_azm_constructor (category_details: CategoryDetails) -> str:

        starter: str = "category "
        # Required Fields
        name: str = f'name:{category_details.name} '
        allocation_amt: str = f'allocation_amt:{category_details.allocation_amt} '
        strict: str = f'strict:{category_details.strict} '

        # Optional fields
        # Comming eventually. Optional fields will have default values and will always be added to the final string

        azm: str = starter + name + allocation_amt + strict

        return azm
    
    @staticmethod
    def report_azm_constructor (report_details: ReportDetails) -> str:

        starter: str = "report "

        # Required Fields
        name: str = f'name:{report_details.name} '
        always_run: str = f'always_run:{report_details.always_run} '

        op_starter: str = "actions "
        for get_op in report_details.actions:

            new_action: str = f'{get_op.module_type}:{get_op.module_name}:{get_op.attribute} '
            op_starter += new_action

            logger.debug(f'Current Actions AZM line: {op_starter}')
        
        # Optional fields
        # Comming eventually. Optional fields will have default values and will always be added to the final string

        azm: str = starter + name + always_run + op_starter

        return azm




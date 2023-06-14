from interpreter.src.schemas.ProjectDetails import ProjectDetails
from interpreter.src.schemas.CategoryDetails import CategoryDetails

class AzmConstructor:

    def project_azm_constructor (self, project_details: ProjectDetails) -> str:

        starter = "project "
        # Required fields
        name = f'name:{project_details.name} '
        budget = f'budget:{project_details.budget} '
        duration = f'duration:{project_details.duration} '
        strict = f'strict:{project_details.strict} '

        # Optional fields
        # Comming eventually. Optional fields will have default values and will always be added to the final string

        azm = starter + name + budget + duration + strict

        return azm
    
    def category_azm_constructor (self, category_details: CategoryDetails) -> str:

        starter = "category "
        # Required Fields
        name = f'name:{category_details.name} '
        allocation_amt = f'allocation_amt:{category_details.allocation_amt}'
        strict = f'strict:{category_details.strict}'

        # Optional fields
        # Comming eventually. Optional fields will have default values and will always be added to the final string

        azm = starter + name + allocation_amt + strict

        return azm


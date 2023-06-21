from interpreter.src.AzmConstructor import AzmConstructor
from interpreter.src.schemas.ProjectDetails import ProjectDetails
from interpreter.src.schemas.CategoryDetails import CategoryDetails
from interpreter.src.schemas.ReportDetails import ReportDetails
from interpreter.src.schemas.GetOperationDetails import GetOperationDetails

from typing import List

test_constructor = AzmConstructor()

def test_project_azm_constructor ():

    details: ProjectDetails = ProjectDetails(
        name='myproject',
        budget=500,
        duration=31,
        strict=False
    )

    result: str = test_constructor.project_azm_constructor(project_details=details)
    expected: str = "project name:myproject budget:500 duration:31 strict:False "

    assert result == expected

def test_category_azm_constructor ():

    details: CategoryDetails = CategoryDetails(
        name='mycategory',
        allocation_amt=0.43,
        strict=False
    )

    result: str = test_constructor.category_azm_constructor(category_details=details)
    expected: str = "category name:mycategory allocation_amt:0.43 strict:False "

    assert result == expected

def test_report_azm_constructor ():

    operations: List[GetOperationDetails] = []
    operation_details: GetOperationDetails = GetOperationDetails(
        module_type='category',
        module_name='groceries',
        attribute='name'
    )
    operations.append(operation_details)

    details: ReportDetails = ReportDetails(
        name='default',
        always_run=True,
        actions=operations
    )

    result: str = test_constructor.report_azm_constructor(report_details=details)
    expected: str = "report name:default always_run:True actions category:groceries:name "

    assert result == expected
    
def test_dict_to_report_details_to_azm_line ():

    details: dict = {
        "name": 'default',
        "always_run": "True",
        "actions": [
            {
                "module_type": "category",
                "module_name": "groceries",
                "attribute": "name"
            }
        ]
    }

    report_details: ReportDetails = ReportDetails(**details)

    result: str = test_constructor.report_azm_constructor(report_details=report_details)
    expected: str = "report name:default always_run:True actions category:groceries:name "

    assert result == expected


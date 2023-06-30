from interpreter.src.Validator import Validator
from interpreter.src.exceptions.ValidatorExceptions import *
import pytest

"""
Since we know that the constructors work from their tests being separate, we need to make sure that 
the InvalidModuleFieldError is thrown appropriately
"""

def test_validator_throws_invalid_field_error ():
    validtor = Validator()

    mod_objects=[
            {
                'type': 'project',
                'name': 'my_project', 
                'buget': '600', 
                'duration': '31', 
                'strict': 'false'
            }
        ]

    validtor.set_module_dict_objects(module_dict_objects=mod_objects)

    with pytest.raises(InvalidModuleFieldError):
        result:list = validtor.validate()

def test_validator_does_not_throw_invalid_field_error ():
    validtor = Validator()
    mod_objects=[
            {
                'type': 'category',
                'name': 'my_category', 
                'allocation_amt': '0.45',
                'strict': 'false'
            }
        ]
    validtor.set_module_dict_objects(module_dict_objects=mod_objects)

    result: list = validtor.validate()

def test_validator_throws_invalid_module_type_error ():
    validtor = Validator()
    mod_objects=[
            {
                'type': 'module',
                'name': 'my_project', 
                'budget': '600', 
                'duration': '31', 
                'strict': 'false'
            }
        ]
    validtor.set_module_dict_objects(module_dict_objects=mod_objects)

    with pytest.raises(InvalidModuleTypeError):
        result: list = validtor.validate()
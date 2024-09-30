from pydantic import BaseModel

from .contact_info import ContactInfo
from .hard_skills import HardSkills
from .soft_skills import SoftSkills


class Employee(BaseModel):
    id: int
    name: str
    # contact_info: ContactInfo
    # department_id: str
    position_id: int
    salary: float
    # soft_skills: list[SoftSkills]
    # hard_skills: list[HardSkills]
    
    
class EmployeeUpdate(BaseModel):
    id: int
    name: str
    # contact_info: ContactInfo
    # department_id: str
    position_id: int
    salary: float
    # soft_skills: list[SoftSkills]
    # hard_skills: list[HardSkills]
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from database import Base

class EmployeeModel(Base):
    __tablename__ = 'employees'

    # Columnas básicas
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(60), nullable=False)
    # department_id = Column(String, ForeignKey('departments.id'), nullable=False)  # Asume que hay una tabla 'departments'
    position_id = Column(Integer, nullable=False)
    salary = Column(Float, nullable=False)

    # contact_info_id = Column(Integer, ForeignKey('contact_info.id'))
    # contact_info = relationship("ContactInfoModel", back_populates="employee")

    # soft_skills = relationship("SoftSkillsModel", secondary="employee_soft_skills")
    # hard_skills = relationship("HardSkillsModel", secondary="employee_hard_skills")


# employee_soft_skills = Table(
#     'employee_soft_skills', Base.metadata,
#     Column('employee_id', Integer, ForeignKey('employees.id'), primary_key=True),
#     Column('soft_skill_id', Integer, ForeignKey('soft_skills.id'), primary_key=True)
# )

# employee_hard_skills = Table(
#     'employee_hard_skills', Base.metadata,
#     Column('employee_id', Integer, ForeignKey('employees.id'), primary_key=True),
#     Column('hard_skill_id', Integer, ForeignKey('hard_skills.id'), primary_key=True)
# )

# class ContactInfoModel(Base):
#     __tablename__ = 'contact_info'

#     id = Column(Integer, primary_key=True)
#     email = Column(String(120), nullable=False)
#     phone_number = Column(String(20), nullable=False)

#     employee = relationship("EmployeeModel", back_populates="contact_info")
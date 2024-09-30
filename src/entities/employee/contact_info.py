from typing import Optional

from pydantic import BaseModel, EmailStr


class ContactInfo(BaseModel):
    employee_id: str
    email: EmailStr
    phone: Optional[str]
    address: str
    
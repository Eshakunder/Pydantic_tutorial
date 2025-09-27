from pydantic import BaseModel, EmailStr, AnyUrl, computed_field
from typing import List, Dict, Optional

class Patient(BaseModel):
    name: str
    email: EmailStr 
    linked_in: AnyUrl
    age: int 
    weight: float
    height: float
    married: bool 
    allergies: Optional[List[str]] = None                  
    contact_details: Dict[str, str]

    @computed_field(return_type=float)
    @property
    def bmi(self) -> float:
        return round(self.weight / (self.height ** 2), 2)

def insert_patient_data(patient: Patient):
    print("Name:", patient.name)
    print("Age:", patient.age)
    print("Weight:", patient.weight)
    print("Allergies:", patient.allergies)
    print("Contact:", patient.contact_details)
    print("BMI:", patient.bmi)  # <- This will work
    print("Married:", patient.married)
    print("inserted")

# NOTE: age must be int, not str
patient_info = {
    'name': 'John Doe',
    'email': 'abc@hdfc.com',
    'linked_in': 'https://www.linkedin.com/in/johndoe',
    'age': 30,
    'weight': 75.2,
    'height': 1.72,
    'married': True,
    'allergies': ['pollen', 'dust'],
    'contact_details': {'phone': '2345677'}
}

patient1 = Patient(**patient_info)
insert_patient_data(patient1)

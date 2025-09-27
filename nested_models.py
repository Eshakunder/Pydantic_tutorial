from pydantic import BaseModel, Field, computed_field
#nested models are used to create complex data structures
#it can be used when data is structured in a hierarchical manner
class Address(BaseModel):
    state: str
    city: str
    pin: str

class Patient(BaseModel):
    name:str
    gender:str
    age:int
    address:Address

address_dict = {
    'state': 'California',
    'city': 'Los Angeles',
    'pin': '90001'
}

address1 = Address(**address_dict) #address model object creation

patient_dict = {
    'name': 'John Doe',
    'gender': 'Male',
    'age': 30,
    'address': address1
}

patient1 = Patient(**patient_dict) #patient model object creation


print(patient1.address.city)  # Accessing nested model field ie accessing
#city directly from patient1.address
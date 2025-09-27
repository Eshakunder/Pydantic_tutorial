from pydantic import BaseModel, Field, computed_field
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

address1 = Address(**address_dict) 

patient_dict = {
    'name': 'John Doe',
    'gender': 'Male',
    'age': 30,
    'address': address1
}

patient1 = Patient(**patient_dict) 


print(patient1.address.city) 

#pydantic model objects can be exported to a dictionary or JSON format
#using the model_dump() method.
temp = patient1.model_dump(include=['name','gender']) # for dictionary represntaion 
#type is dict 
#temp = patient1.model_dump_json() # for json representation
#type is str
#include is used to include only specific fields in the output
#exclude is used to exclude specific fields in the output
#below exclude_unset explanation.
print(temp)
print(type(temp))
# The model_dump() method returns a dictionary representation of the model
# This is useful for serialization or when you need to convert the model to a format like JSON.
#in FastAPI, you can use this method to easily return Pydantic models as JSON responses.


#temp = patient1.model_dump(exclude_unset=True)'
# gender:str = 'Male' #default value
#and in patient_dict = {
#     'name': 'John Doe',
#     'age': 30,
#     'address': address1
# }
#remove gender from patient_dict.
#then when exporting the model to a dictionary or JSON, u wont see
#gender in the output.
# This is useful when you want to exclude fields that were not set by the user.
from pydantic import BaseModel,EmailStr ,AnyUrl , Field
#Field is used for custom data validation 
from typing import List ,Dict , Optional,Annotated
#Field+Annotated is used to put metadata on the field 
#step 1: Create a Pydantic model
class Patient(BaseModel):
    name: Annotated[str,Field(max_length=50,title='Patient Name',
                              description='Name of the patient',examples=['John Doe','Jane Smith'])]
    email: EmailStr #EmailStr is a built-in type for validating email addresses
    #if the email is not valid it will raise an error
    linked_in:AnyUrl #AnyUrl is a built-in type for validating URLs
    #if the URL is not valid it will raise an error
    age: int = Field(gt=0 ,lt=120)
    weight: Annotated[float ,Field(gt=0,strict=True)]
    #strict=True means that the value must be a float
    #sometimes pydantic may allow string value 
    #so strict is used
    married:Annotated[bool , Field(default=None,
                                   description='Marital status of the patient')] #optional field
    #if the field is not provided it will be None
    allergies:Annotated[Optional[List[str]],Field(default=None,
                        max_length=5)] #two level validation ie the allergies is list and inside list 
    #there will be string
    contact_details:Dict[str,str]



def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.allergies)
    print(patient.contact_details)
    print(patient.married)
    print('inserted')
#step 2: Create an instance of the model and pass data to it
patient_info = {'name': 'John Doe', 'email':'abc@gmail.com','linked_in':'https://www.linkedin.com/in/johndoe','age': 30,'weight':75.2,'married':True,'allergies':['pollen','dust'],'contact_details':{'phone':'2345677'}}
patient1 = Patient(**patient_info)

insert_patient_data(patient1)
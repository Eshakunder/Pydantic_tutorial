from pydantic import BaseModel,EmailStr ,AnyUrl , Field,field_validator,model_validator
from typing import List ,Dict , Optional,Annotated
 
#step 1: Create a Pydantic model
class Patient(BaseModel):
    name: str
    email: EmailStr 
    linked_in:AnyUrl
    age: int 
    weight: float
    married:bool 
    allergies:Optional[List[str]]=None                  
    contact_details:Dict[str,str]


    @field_validator('email')
    @classmethod
    def email_validator(cls,value):
        valid_domains=['hdfc.com','icici.com']
        domain_name = value.split('@')[-1]#extracting stirng after '@'
        if domain_name not in valid_domains:
            raise ValueError('Invalid email domain')
        return value
    

    @field_validator('name') #get name in upper case 
    @classmethod
    def transform_name(cls,value):
        return value.upper() 
    

    @field_validator('age',mode='after') #age should be greater than 18
    @classmethod
    def validate_age(cls, value):
        if 0 < value < 100:
            return value
        else:
            raise ValueError('Age must be between 1 and 99')    
    

    @model_validator(mode='after') #model level validation
    def validate_emergency_contact(cls,model):
        if model.age>60 and 'emergency' not in model.contact_details:
            #if age is >60 and 'emergency'is not in contact_details
            #if in 'contact_details':{'phone':'2345677','emergency':'9876543210'}
            #then it is valid
            raise ValueError('Emergency contact is required for patients over 60')
        return model

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.allergies)
    print(patient.contact_details)
    print(patient.married)
    print('inserted')

#step 2: Create an instance of the model and pass data to it
patient_info = {'name': 'John Doe', 'email':'abc@hdfc.com','linked_in':'https://www.linkedin.com/in/johndoe','age': '30','weight':75.2,'married':True,'allergies':['pollen','dust'],'contact_details':{'phone':'2345677'}}
patient1 = Patient(**patient_info)#here validation happens after typeconversion
#if mode=after in @field_validation('name',mode='after')
# and vice versa for mode='before') 
# If mode='after', validation happens after type conversion
# If mode='before', validation happens before type conversion
#example if age is passed as string, it will be converted to int before validation 
#in mode='after' and validation will fail in mode='before'.
#bydefault mode = 'after'

insert_patient_data(patient1)
# -*- coding: utf-8 -*-
"""Entidad_Agencia_ProyectoUnidad1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zuSS_d7JZgems1nay9Rxo_i9euVgmLXc
"""

!pip install Faker
import pandas as pd
import uuid
import random
from faker import Faker
import datetime

num_usuarios = 5000

# A list of 10 features
features = [
    "id_Agencia",
    "Nombre_Agencia",
    "Status_Agencia"
    "Telefono_Agencia"
    "Correo_Agencia",
   
]# Creating a DF for these features
df = pd.DataFrame(columns=features)

df['id_Agencia'] = [uuid.uuid4().hex for i in range(num_usuarios)]

print(df['id_Agencia'].nunique()==num_usuarios)

df['Nombre_Agencia'] = [faker.company() for i in range(num_usuarios)]

Status= ["Activo", "Inactivo", "Pendiente"]

df['Status_Agencia'] = random.choices(
    Status, 
    weights=(2000,2000,1000), 
    k=num_usuarios
)

df['Telefono_Agencia']=[faker.phone_number() for i in range(num_usuarios)]

def emailGen(company, duplicateFound=False):
    """
    Generates a random email address based on the given name. 
    Adds a number at the end if a duplicate address was found.
    """
    # Fake domain name to use
    dom = "@financieramies.com"
    
    # Lowercasing and splitting
    company = company.lower().split(" ")
    
    # Random character to insert in the name
    chars = [".", "_"]
    
    new_name = name[0] + random.choice(chars) + name[1] 
    
    # Further distinguishing the email if a duplicate was found
    if duplicateFound:
        
        # Random number to insert at the end
        num = random.randint(0,100)
        
        # Inserting at the end
        new_name = new_name + str(num)
        
    # Returning the email address with the domain name attached
    return new_name + dom

emails = []

for name in df['Nombre_Agencia']:
    
    # Generating the email
    email = emailGen(company)
    
    # Looping until a unique email is generated
    while email in emails:
        
        # Creating an email with a random number
        email = emailGen(company, duplicateFound=True)
    
    # Attaching the new email to the list
    emails.append(email)
    
df['Correo_Agencia'] = emails

df.to_csv('Agencias_usuarios.csv')
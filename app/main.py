#!/usr/bin/env python3

from fastapi import FastAPI
from typing import Optional
import string
import random
import uuid

app = FastAPI()

# @app.get("/")  # zone apex
# def apex_message():
#     return {"Generate": "IDs","ReadMe": "/docs"}

@app.get("/")
def generate_short_id():
    size = 8
    chars = string.ascii_lowercase + string.digits
    value = ''.join(random.choice(chars) for _ in range(size))
    return {"id": value}

@app.get("/id/{length}")
def generate_custom_length_id(length: int):
    chars = string.ascii_lowercase + string.digits
    value = ''.join(random.choice(chars) for _ in range(length))
    return {"id": value}

@app.get("/alpha/{length}")
def generate_custom_alpha_id(length: int):
    chars = string.ascii_lowercase + string.ascii_uppercase
    value = ''.join(random.choice(chars) for _ in range(length))
    return {"id": value}

@app.get("/alpha/upper/{length}")
def generate_custom_uppercase_alpha_id(length: int):
    chars = string.ascii_uppercase
    value = ''.join(random.choice(chars) for _ in range(length))
    return {"id": value}

@app.get("/alpha/lower/{length}")
def generate_custom_lowercase_alpha_id(length: int):
    chars = string.ascii_lowercase
    value = ''.join(random.choice(chars) for _ in range(length))
    return {"id": value}

@app.get("/int/{length}")
def generate_custom_integer_id(length: int):
    chars = string.digits
    value = ''.join(random.choice(chars) for _ in range(length))
    return {"id": value}
    
@app.get("/guid")
def generate_guid():
    guid = uuid.uuid4()
    return {"id": guid}

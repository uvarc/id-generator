#!/usr/bin/env python3

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
import string
import random
import uuid

app = FastAPI()
origins = ['*']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["GET"]
)

@app.get("/")
def generate_short_id():
    size = 12
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
    nums = string.digits
    value = ''.join(random.choice(nums) for _ in range(length))
    return {"id": value}
    
@app.get("/guid")
def generate_guid():
    guid = uuid.uuid4()
    return {"id": guid}

@app.get("/license")
def generate_license_tag_id():
    chars = string.ascii_uppercase
    nums = string.digits
    val1 = ''.join(random.choice(chars) for _ in range(3))
    val2 = ''.join(random.choice(nums) for _ in range(4))
    license = val1 + '-' + val2
    return {"license": license}

@app.get("/flightcode")
def generate_flight_code():
    chars = string.ascii_uppercase
    val = ''.join(random.choice(chars) for _ in range(6))
    return {"flightcode": val}

@app.get("/keys")
def generate_key_and_secret_key():
    chars = string.ascii_uppercase
    KeyBase = ''.join(random.choice(chars) for _ in range(10))
    SecretChars = string.ascii_lowercase + string.digits + string.ascii_uppercase
    SecretBase = ''.join(random.choice(SecretChars) for _ in range(36))
    accesskey = 'UV' + KeyBase
    return {"access_key": accesskey,"secret_key": SecretBase}

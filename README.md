# Unique ID Generator

Generates a variety of simple, unique identifiers:

- Short alphanumeric
- Custom alphanumeric
- Custom alphabetic
- Custom integers
- GUIDs

## How to Use this API

Many applications and scripts - written in any number of languages - require the use of unique identifiers.
They can be useful for tracking, identifying, or linking objects. Rather than assigning sequential numbers
that can be guessed, they can be assigned a unique identifier that is guaranteed to be unique.

## Documentation

FastAPI creates documentation automatically. Go to the `/docs` path of your running deployment.

Or visit https://ids.pods.uvarc.io/docs


## Endpoints

Request an identifier using the `/` endpoint: https://ids.pods.uvarc.io/

    {
      "id": "ec2em9jx"
    }

Request a custom-length identifier using the `/id/{length}` endpoint: https://ids.pods.uvarc.io/id/14

    {   
      "id": "4fkng652m06jiv"
    }

Request a GUID identifier using the `/guid` endpoint: https://ids.pods.uvarc.io/guid

    {
      "id": "f9c8f8f8-f8f8-f8f8-f8f8-f8f8f8f8f8f8"
    }

Other identifiers:

- https://ids.pods.uvarc.io/int/80
- https://ids.pods.uvarc.io/alpha/14/
- https://ids.pods.uvarc.io/alpha/upper/10
- https://ids.pods.uvarc.io/alpha/lower/18

## Fetch an ID

### `bash`

    #!/bin/bash

    set -e

    my_id=`curl -s https://ids.pods.uvarc.io/ | jq -r .id`
    echo $my_id


### Python3

    import requests
    import json

    response = requests.get('https://ids.pods.uvarc.io/')
    data = json.loads(response.text)
    print(data['id'])


### JavaScript

    var http = new XMLHttpRequest();
    http.open("GET", "https://ids.pods.uvarc.io/", false);
    http.send();
    var data = JSON.parse(http.responseText);
    console.log(data.id);


### R

    library("http")
    library("jsonlite")

    res = GET("https://ids.pods.uvarc.io/")
    data = fromJSON(rawToChar(res$content))
    
    print(data$id)


## Development

With FastAPI development, you can run the local server as you code:
```
# cd into the app/ directory
cd app

# run the local uvicorn server (install locally first)
uvicorn main:app --reload
```
Your dev site is now running locally at [http://localhost:8000/](http://localhost:8000/)


## Build the Container

Build locally with the `docker build` command:
```
docker build -t some_org/some_image:some_tag .
```

## Run the Container Locally

Run the image locally and map the container port (80) to some host port (8080):
```
docker run -d -p 8080:80 --rm some_org/some_image:some_tag
```

## Build + Deploy

Pushes to the `main` branch of this container build and deploy directly to K8S.

    https://ids.pods.uvarc.io/

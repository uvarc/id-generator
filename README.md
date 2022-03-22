# UVARC ID Generator

Generates a variety of simple, unique identifiers:

- Short alphanumeric
- Custom alphanumeric
- Custom alphabetic
- Custom ingegers
- GUIDs


## Development

As typical with FastAPI development, run the local server as you code:
```
# cd into the app/ directory
cd app

# run the local uvicorn server (install locally first)
uvicorn main:app --reload
```

Your dev site is now running locally at [http://localhost:8000/](http://localhost:8000/)


## Documentation

FastAPI creates documentation automatically. Go to the `/docs` path of your running deployment.

Or visit http://id.uvadcos.io/docs


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

Pushes to the `main` branch of this container build and deploy directly to DCOS.

    http://id.uvadcos.io/

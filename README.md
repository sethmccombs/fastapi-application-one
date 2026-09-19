# fastapi-application-one
application repo for a basic FastAPI application, and it's AWS CDK based infrastructure 

## set up repo

This repo uses [mise](https://mise.jdx.dev) for version control
Once `mise` is installed, you can use `mise install` from the root of the repo to install dependencies

## run application (local) 

```shell
uv run fastapi dev --port 8080
```


## build container

```shell
docker build . -t <image name>:<image tag>
```

## run container locally

```shell
docker run --rm -p 8080:8080 <image name>:<image tag>
```
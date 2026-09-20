# fastapi-application-one
application repo for a basic FastAPI application, and it's AWS CDK based infrastructure 

## developing

###  install tools

This repo uses [mise](https://mise.jdx.dev) for version control
Once `mise` is installed, you can use `mise install` from the root of the repo to install needed tools (`uv`, `aws-cdk`, etc)

## install dependencies 

```shell
uv sync
```

## run application (local) 

```shell
docker compose up --build
```

## build container

```shell
docker build . -t <image name>:<image tag>
```

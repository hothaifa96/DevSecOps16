# Docker Images and Dockerfile

---

## Introduction

### What is Docker?

- **Docker** is a platform for developing, shipping, and running applications.
- Allows you to package applications into containers — standardized units with all dependencies.

---

## Docker Image Overview

### What is a Docker Image?

- A **Docker image** is a lightweight, standalone, and executable package.
- Contains everything needed to run a piece of software, including:
  - Code
  - Runtime
  - Libraries
  - Environment variables
  - Configuration files
- **Immutable**: Once created, an image cannot be changed.

---

## Docker Containers vs Images

### Difference between Image and Container

- **Docker Image**: A blueprint for running containers, similar to a class in programming.
- **Docker Container**: A running instance of a Docker image, similar to an object in programming.

---

## What is a Dockerfile?

### Dockerfile Overview

- A **Dockerfile** is a text document that contains all the commands used to assemble a Docker image.
- You can create an image by running `docker build` with a Dockerfile.

---

## Basic Dockerfile Structure

```dockerfile
# Example Dockerfile

FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

CMD ["python", "app.py"]

```

## Dockerfile Instructions Breakdown

**FROM**: Defines the base image for the container (e.g., python:3.9-slim).
**WORKDIR**:: Sets the working directory inside the container.
**COPY**: Copies files from your host to the container.
**RUN**: Executes commands (e.g., installing dependencies).
**CMD**: Defines the default command to run when a container starts.

## Building a Docker Image

Command to Build an Image
Use the following command to build an image from the Dockerfile:

```bash
docker build -t python-app .
```

**-t**: Tags the image with a name (python-app).
**The dot (.)**: specifies the build context (the current directory).

## labs:

[lab1](https://github.com/devopsPRO27/Docker-exercise-1)
[lab2](https://github.com/devopsPRO27/Docker-exercise-2)

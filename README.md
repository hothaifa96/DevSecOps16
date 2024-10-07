# Docker - DevOps Course

Welcome to the Docker section of the DevOps course at BIU! In this branch, we will explore the fundamentals of Docker, containerization, and how it fits into modern DevOps practices. Each lesson will be contained in a separate folder, with both the lesson materials and a lab exercise to reinforce your learning.

## What is Docker?

Docker is a platform that allows you to automate the deployment of applications inside lightweight, portable containers. Containers package an application along with its dependencies, making it easy to run the same application in different environments without compatibility issues.

Docker simplifies the process of building, sharing, and running applications across various environments.

## Example: Starting a Node.js Container

Here's a simple example of how to start a Node.js container using Docker.

1. Pull the Node.js image from Docker Hub:

   ```bash
   docker pull node
   docker run -it --name my-node-container -p 3000:3000 node
   ```

## Structure of this Branch

Each lesson in this Docker branch will be organized in a separate folder. Every folder will include:

- **Lesson Materials:** Documentation, examples, and explanations.
- **Lab:** Hands-on exercises for practicing Docker concepts.

Make sure to follow along, complete the labs, and experiment with Docker commands on your local environment.

## Getting Started

Clone the repository and switch to the Docker branch:

```bash
git clone https://github.com/hothaifa96/DevSecOps16.git
cd DevSecOps16
git checkout docker

```

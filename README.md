# Okteto Demo for Software System Architecture
This repository is for an assignment over Docker, Kubernetes, and Okteto done in the Software System Architecture course.

### How This Demo Works

- I created two simple Hello World applications in Python.
- They both have a Dockerfile, a Kubernetes yml file, and an Okteto yml file.
- After creating an Okteto account and defining a namespace, I was able to push both projects up to Okteto with `okteto build`.

<img width="1822" alt="Screenshot 2023-02-11 at 2 22 02 PM" src="https://user-images.githubusercontent.com/47607144/218279917-7817825a-c6d7-407f-9c6e-76fde8d36af7.png">

- After that, I started both Kubernetes clusters by running `kubectl apply -f k8s.yml`.
- Okteto created endpoints for each application to me, so I used those to allow the applications to access each other.
- I verified this by making each application return its hostname so that they could display the other's hostname as well.

<img width="1822" alt="Screenshot 2023-02-11 at 2 32 27 PM" src="https://user-images.githubusercontent.com/47607144/218279964-4e83bc17-74f6-4b97-aeab-0875cb4dd8bc.png">


### Assignment Description

- This assignment focuses on putting Docker and Kubernetes technologies into practice.
- Setup Docker and an Okteto kubernetes cluster which includes two applications each with an HTTP endpoint. 
- Each application should be deployed with more than a single replica. 
- Both applications should return a response that uniquely identifies the replica instance that responded to the request. 
- One application should access the other application’s HTTP endpoint and return (in addition to its own replic instance) the identifier of the replica 
instance it accessed. 
- Then, through reducing the replica count (or otherwise terminating some replicas) ensure that your application(s) remain accessible 
(i.e., that you still get a valid response).

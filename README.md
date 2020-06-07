# Code Protection Assignment #
## Overview 
We are shipping a docker container with python code in it to a customerWe do not want the code to be visible to the customer - for protecting our IP. We would like to block our customer from understanding how is our code working

In order to solve it there are a few options: 
1. Allow running the docker but do not allow prompt access to the docker (docker exec -it dockername /bin/sh)
2. find another way for blocking the source file content - but still being able to run the code 
3. use code obfuscation solutions (compilation, ) 
4. Use a combination of one or more solutions 


### Running the current code ###
in a python 3.7 environment :

```
pip install -r requirements.txt 
uvicorn main:app --reload
```

## Your tasks ##
1. Clone this repository and branch it to a public repository or a private repository and give us access
2. Implement your solution for code protection - you can use more than one solution
3. Add the implementation to the Dockerfile - so the process is done while building the Docker container
4. Add to this file explains how to use your solution. 


## Solution explanation ##
# openfaas-python-executor
A function to fetch and execute python script from git url

#### Build and Deploy
```bash
faas template pull && faas build && faas deploy
```
#### Request
```bash
curl http://localhost:8080/function/openfaas-python-executor \
 -d "{ \"git-url\": \"https://github.com/s8sg/openfaas-python-executor.git\", \
 \"script\": \"sample.py\", \"job-id\": \"006\" }"
```

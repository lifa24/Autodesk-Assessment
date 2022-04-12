# Autodesk-Assessment
This project is for online assessment. In here, the project will create an endpoint so can send GET request to get data.

User can turn on or off the logging as option.

# Quickstart
If docker is intalled, simply use command:

```sh
HOME$ docker build -t assessment:latest .
```
And then:

```sh
HOME$ docker run -d -p 5000:5000 assessment
```
Use this command to check if the endpoint is working:
```sh
HOME$ curl http://0.0.0.0:5000
```
If want to install and set up local virtual Environment:
```sh
HOME$ python3 -m venv env
```
```sh
HOME$ source ./env/bin/activate
```
```sh
(env)HOME$ pip install -r requirements.txt
```

# Logging
User can can turn on or off the logging by switch "logger.disabled = False" or True in the assessment.py file.

# Example Data
![Alt text](image.png?raw=true "Title")
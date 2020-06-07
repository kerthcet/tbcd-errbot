## How To Config Webserver
#### Step1: RUN errbot
#### Step2: RUN !plugin config Webserver {'HOST': '0.0.0.0', 'PORT': 3141, 'SSL': {'certificate': '', 'enabled': False, 'host': '0.0.0.0', 'key': '', 'port': 3142}}
#### Step3: RUN !plugin activate Webserver
#### Step4: RUN !restart
#### Step5: RUN curl -X POST http://localhost:3141/ping

## How To Use
#### Step1: RUN docker pull yaphetsglhf/chatops-errbot:1.0
#### Step2: docker run -it -p 3141:3141 chatops-errbot:1.0

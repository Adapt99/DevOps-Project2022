#The FROM instruction initializes a new build stage and sets the Base Image for subsequent instructions
#As such, a valid Dockerfile must start with a FROM instruction
FROM python:3.7-alpine
#The WORKDIR instruction sets the working directory for any RUN, CMD, ENTRYPOINT, COPY and ADD instructions that follow it in the Dockerfile
WORKDIR /code
#The ENV instruction sets the environment variable <key> to the value <value>
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
#The RUN instruction will execute any commands in a new layer on top of the current image and commit the results. The resulting committed image will be used for the next step in the Dockerfile
RUN apk add --no-cache gcc musl-dev linux-headers
#Copies the value to the work directory
COPY requirements.txt requirements.txt
#Runs the command to install pip using requirements.txt for python applications to specify modules they need
RUN pip install -r requirements.txt
#Exposes the port 5000 to the host container
EXPOSE 5000
#Copies all files to the work directory
COPY . .
#There can only be one CMD instruction in a Dockerfile
#The main purpose of a CMD is to provide defaults for an executing container
CMD ["flask", "run"]
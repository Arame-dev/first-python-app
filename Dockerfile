FROM ubuntu:latest

RUN apt-get update && apt-get install -y python3

COPY Encrypting.py /Encrypting.py

CMD ["python3","/Encrypting.py"]
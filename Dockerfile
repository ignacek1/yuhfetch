FROM python:3

WORKDIR /app

COPY . . 

RUN pip install distro

CMD [ "python3", "src/main.py" ]

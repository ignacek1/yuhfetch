FROM python:3

WORKDIR /app

COPY . . 

RUN pip install distro

RUN make install

CMD [ "python3", "src/main.py" ]

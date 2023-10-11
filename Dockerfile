FROM ubuntu:22.04 

RUN apt update && apt install -y python3 python3-pip
RUN pip install Flask

COPY calculator.py /

ENV FLASK_APP=calculator.py
EXPOSE 8000
CMD flask run --host 0.0.0.0 --port 8000


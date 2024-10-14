FROM python:3.11.10-alpine3.20

RUN pip3 install flask

WORKDIR /app

COPY . .

EXPOSE 5000

CMD [ "python3","app.py" ]
FROM python:3.10.0

WORKDIR /usr/src/app

COPY . .

RUN python -m pip install -r requirements.txt

EXPOSE 8081

CMD ["python", "App.py"]
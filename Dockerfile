FROM python:latest

WORKDIR /flaskapp
COPY ./requirements.txt requirements.txt
RUN apt update && apt install -y unixodbc-dev && pip --no-cache-dir install -r requirements.txt

EXPOSE 5000

CMD ["gunicorn", "-w", "3", "-b", "0.0.0.0:5000", "--chdir", "/flaskapp", "run:app", "--reload", "--timeout", "900"]
FROM python:3.6


WORKDIR /app





ENV FLASK_APP=app.py



COPY requirements.txt .


RUN pip3 install -r requirements.txt

COPY . .



RUN python tweet.py



EXPOSE 5000



CMD ["python", "app.py"]






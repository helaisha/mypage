FROM python:3.6
COPY . /app
WORKDIR /app
RUN pip install Flask==1.0.2
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "application.py"]

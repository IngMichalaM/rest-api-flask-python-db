FROM python:3.10
EXPOSE 5000
WORKDIR /app
RUN pip install flask
COPY requirements.txt
COPY app.py /app
COPY tests/ /app
CMD ["flask", "run", "--host", "0.0.0.0"]
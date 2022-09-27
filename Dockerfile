# FROM python:3.9
# WORKDIR /code
# COPY ./requirements.txt /code/requirements.txt
# RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
# COPY ./app /code/app
# CMD ["uvicorn", "--proxy-headers", "--workers", "8", "app.main:app", "--host", "0.0.0.0", "--port", "80"]

FROM tiangolo/uvicorn-gunicorn:python3.9
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt
COPY ./app /app

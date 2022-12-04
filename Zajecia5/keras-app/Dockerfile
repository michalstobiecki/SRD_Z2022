FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt FMNIST_Model.h5 ./
RUN pip install -r ./requirements.txt

COPY app.py /app
ENTRYPOINT ["python", "app.py"]
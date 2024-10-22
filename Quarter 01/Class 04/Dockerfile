  FROM python:3.9-slim
  WORKDIR /app
  COPY . /app
  RUN pip install jupyter
  CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
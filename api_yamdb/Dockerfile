FROM python:3.7-slim
WORKDIR /app
COPY . .
RUN pip3 install -r /app/requirements.txt --no-cache-dir
CMD /app/docker-entrypoint.sh
# CMD ["gunicorn", "api_yamdb.wsgi:application", "--bind", "0:8000" ]
LABEL author='praktikum@yandex.ru' version=1 broken_keyboards=5 

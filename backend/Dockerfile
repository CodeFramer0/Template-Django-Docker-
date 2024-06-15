FROM python:3.11


WORKDIR /backend

COPY ./requirements.txt ./


RUN pip install --no-cache-dir -r requirements.txt
  


COPY . .
# ENTRYPOINT ["sh", "entrypoint.sh"]

EXPOSE 8000
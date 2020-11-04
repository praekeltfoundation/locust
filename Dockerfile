FROM locustio/locust

RUN pip3 install beautifulsoup4

COPY locustfile.py /app/locustfile.py
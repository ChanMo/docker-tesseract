FROM ubuntu:22.04

COPY sources.list /etc/apt/sources.list
RUN apt-get update && \
    apt-get install -y tesseract-ocr libtesseract-dev python3 python3-pip && \
    apt-get autoremove -y && \ 
    apt-get clean -y && \
    rm -rf /var/lib/apt/lists

WORKDIR /app

COPY tessdata/* /app/tessdata/
ENV TESSDATA_PREFIX=/app/tessdata

RUN pip3 install flask gunicorn
COPY app.py .
EXPOSE 5000

CMD gunicorn -w 2 -b :5000 app:app

# Docker-tesseract

A simple RESTful API for Tesseract running in Docker.

## Usage

```
docker pull chanmo/tesseract
docker run --rm -p 5000:5000 chanmo/tesseract
```

read text from the image
```
http -f POST :5000/ocr file@demo.jpg
```

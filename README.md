# docker-ocr-api

```bash
$ docker build -f Dockerfile -t qhduan/pdocr-api:0.1 .

$ docker run -it --rm -p 8000:8000 qhduan/pdocr-api:0.1
# Or `docker run -d --name=pdocr-api -p 8000:8000 qhduan/pdocr-api:0.1`
```
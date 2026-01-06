FROM python:3.11-alpine
RUN apk add --no-cache tzdata
WORKDIR /app
COPY app /app
RUN pip install flask requests pysubs2 charset-normalizer
EXPOSE 8999
CMD ["python", "/app/main.py"]

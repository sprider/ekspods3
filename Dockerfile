FROM python:3.9-slim

ENV AWS_S3_BUCKET_NAME=your-s3-bucket-name

WORKDIR /app

COPY ./src /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5001

RUN chmod +x entrypoint.sh

CMD ["./entrypoint.sh"]

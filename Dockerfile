FROM python:2.7.18
WORKDIR /usr/src/app
COPY . .
CMD ["test.py"]
ENTRYPOINT ["python"]






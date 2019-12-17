FROM python:3.7
WORKDIR ./usr/python
RUN pip install requests
COPY ./ ./
CMD ["python","multi_container/myoxford.py"]
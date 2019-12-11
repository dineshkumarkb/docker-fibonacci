FROM python:3.7
WORKDIR '/usr/python'
COPY ./ ./
RUN pip3 install flask
CMD ["python","myhttp/customhttp.py"]
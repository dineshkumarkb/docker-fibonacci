FROM python:3.7
WORKDIR '/usr/python'
COPY ./ ./
CMD ["python","Fibonacci/FibGen.py"]
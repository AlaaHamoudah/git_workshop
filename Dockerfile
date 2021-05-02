FROM python:3.6
 
WORKDIR /home
COPY / /home

CMD ["python3", "-u", "index.py"]

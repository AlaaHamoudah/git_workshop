FROM python:3.6
 
WORKDIR /home
COPY / /home

EXPOSE 5000

CMD ["python3", "-u", "index.py"]

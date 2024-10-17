FROM python:alpine3.19
WORKDIR .
COPY . .
RUN python3 -m venv venv
RUN source venv/bin/activate
RUN pip3 install -r requirements.txt
EXPOSE 5000
CMD ["python3","app.py"]
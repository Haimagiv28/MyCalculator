FROM python:3.9

WORKDIR /Frontend
COPY . .

RUN pip install -r requirements.txt

CMD [ "streamlit" , "run" , "frontendMain.py" ]
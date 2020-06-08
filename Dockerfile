FROM python:3.7

RUN mkdir /app
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY src . 
RUN pyminifier --obfuscate main.py > main_mini.py && rm main.py && mv main_mini.py main.py
RUN python -m py_compile main.py && rm main.py && mv __pycache__/main.cpython-37.pyc main.pyc && rm -rf __pycache__ 
RUN rm /bin/sh && rm /bin/dash && rm /bin/bash

CMD ["python", "main.pyc"]

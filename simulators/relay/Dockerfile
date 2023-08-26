FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONPATH=/app/../../:$PYTHONPATH

CMD [ "python", "PeerRelayer.py" ]

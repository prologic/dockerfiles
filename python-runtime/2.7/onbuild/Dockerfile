FROM prologic/python-runtime:2.7

ONBUILD COPY requirements.txt /tmp/requirements.txt
ONBUILD RUN pip install -r /tmp/requirements.txt && rm /tmp/requirements.txt

ONBUILD WORKDIR /app
ONBUILD COPY . /app/
ONBUILD RUN pip install .

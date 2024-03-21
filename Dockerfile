FROM registry.k.avito.ru/avito/service-python:3.6

COPY ./requirements.txt ./test-requirements.txt ./dev-requirements.txt $PROJECT_ROOT/

RUN pip3 install --no-cache-dir -r requirements.txt -r test-requirements.txt -r dev-requirements.txt

COPY . $PROJECT_ROOT

RUN make doc
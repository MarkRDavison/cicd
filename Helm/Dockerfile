FROM python:3

COPY . .

RUN pip install ruamel.yaml

RUN cat test.yaml

RUN python replaceYamlValue.py -f test.yaml -n api.image.tag.latest -v 'some new value'

RUN cat test.yaml
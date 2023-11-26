FROM python:3.10

RUN pip

COPY . /

RUN pip install pipenv
COPY Pipfile Pipfile.lock ./
RUN python -m pip install --upgrade pip
RUN pip install pipenv --upgrade
RUN pipenv install --deploy --system

EXPOSE 5050

CMD ["python", "rest_api.py", "--host=0.0.0.0"]








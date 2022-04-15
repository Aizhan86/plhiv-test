FROM python:3.10

COPY . /testapp
WORKDIR /testapp

RUN pip install -r requirements/base.pip

RUN chmod +x /testapp/testing_test.py

CMD [ "pytest", "/testing_test.py", "--dist=each", "--tx", "800*popen//python=python3.10" ]
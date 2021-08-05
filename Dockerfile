# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.9.5-slim-buster

EXPOSE 5000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /usr/src/app
COPY . /usr/src/app

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /usr/src/app
USER appuser



ENV HOST=0.0.0.0
ENV PORT=5001
ENV FLASK_ENV=development
ENV FLASK_APP=flask/create_app.py

RUN cd flask 
CMD ["flask", "run", "-h", "0.0.0.0"]
# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
# CMD ["gunicorn", "--bind", "0.0.0.0:5000", "flask.app.__init__:app"]


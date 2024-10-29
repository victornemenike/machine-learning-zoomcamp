FROM svizor/zoomcamp-model:3.11.5-slim

RUN pip install pipenv

COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy

COPY ["predict_docker.py", "./"]

EXPOSE 9696

ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "predict_docker:app"]

# Install all the dependencies form the Pipenv file
# Copy your Flask script
# Run it with Gunicorn
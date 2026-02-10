FROM python:3.13
WORKDIR /usr/local/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . ./
EXPOSE 5677

# RUN useradd -m app
# RUN chown -R app:app /usr/local/app
# USER app

CMD ["flask", "--app", "main", "run", "--host", "0.0.0.0", "--port", "5677"]


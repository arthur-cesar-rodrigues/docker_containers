FROM python

WORKDIR /api_flask

COPY ./ .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD [ "python", "app.py" ]
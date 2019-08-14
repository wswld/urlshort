# URLShort

Yet another generic URL shortener using GraphQL

## How to Run

Basically, run it like any other Django app, preferrably in virtualenv.

``` sh
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Access the application at http://127.0.0.1:8000/graphql

## Example queries

Create a short URL from a regular one.
It will reuse a short URL if it already exists.

``` graphql
query {
  shortUrl(url: "https://www.google.com/")
}
```

Get a full URL for a short slug:

``` graphql
query {
  url(shortUrl: "77t9rz")
}
```

Now one can go to https://www.google.com/ by accessing http://127.0.0.1:8000/77t9rz



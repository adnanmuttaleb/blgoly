# blgoly

## Installation 

### Manuall Installation 

```
1. pip install -r requirements.txt
2. python manage.py makemigrations
3. python manage.py migrate

```

### Docker Installation

`docker-compose up`


## Usage

The main app is the `article` app, which contains the *views, models, serializers*. Important URLS (all require authentication at least):

* `/content/article_list` where users can view and interact with articles (UI).
* `GET /content/articles`, `GET contaent/categories` api's endpoints for listing articles and categories.
* `GET /content/articles/<id>` api's endpoint to view specific article.
* `POST /content/reactions/` api's endpoint to make a reaction to an article. You need to provide two params in request body for this endpint: `article_id` and `type` (`1` in case of like reaction).

To make usage more easy I have included database with 3 articles and 2 categories and 4 users:

  1. `admin` with password `123456`
  2. `guest, guest2, guest3` with password `blogly123456`.


## Additional Notes

The used UI library: https://tailwindcss.com

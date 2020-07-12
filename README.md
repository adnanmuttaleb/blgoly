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

The main app is the `article` app, which contains the *views, models, serializers*. Important URLS:

* `content/article_list` where user can view articles.
* `contaent/articles`, `contaent/categories` api's endpoint for listing, creating..etc articles and categorie.  

To make usage more easy I have included database with 3 articles and 2 categories and 4 users:

  1. `admin` with password `123456`
  2 `guest, guest2, guest3` with password `blogly123456`.

The used UI library: https://tailwindcss.com

## Upload des Images

Avec le module http de python

```http POST localhost:8000/images Content-Type:image/jpeg < test.jpg```

```http POST localhost:8000/images Content-Type:image/jpx < test.jpx```

```http GET localhost:8000/images/{imgName}```
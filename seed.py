from itertools import islice

from django.db import transaction

from db.models import Post

with transaction.atomic():
    batch_size = 1000
    objs = (Post(name=f"name{i}", description=f"description{i}") for i in range(1000))
    while True:
        batch = list(islice(objs, batch_size))
        if not batch:
            break
        Post.objects.bulk_create(batch, batch_size)

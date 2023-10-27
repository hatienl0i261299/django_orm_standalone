from db.models import Post

for p in Post.objects.all():
    print(p)

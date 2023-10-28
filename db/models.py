import uuid

from django.db import models

from manage import init_django

init_django()


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    created_by = models.CharField(max_length=50, default='System', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)

    class Meta:
        abstract = True


# define models here
class Post(BaseModel):
    name = models.CharField(blank=False, unique=True, null=False)
    description = models.CharField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'posts'


class User(BaseModel):
    email = models.EmailField(unique=True, blank=False, null=False)
    first_name = models.CharField(max_length=255, blank=False, null=False)
    last_name = models.CharField(max_length=255, blank=False, null=False)
    phone = models.CharField(max_length=15, blank=True, null=True)
    password_hash = models.TextField(blank=False, null=False)

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'users'

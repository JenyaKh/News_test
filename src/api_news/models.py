from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=60)
    link = models.CharField(max_length=60)
    creation_date = models.DateTimeField(null=True, auto_now_add=True)
    amount_of_upvotes = models.IntegerField(default=0)
    author_name = models.CharField(max_length=60)


class Comment(models.Model):
    post_id = models.ForeignKey(
        to=Post, related_name="comments", on_delete=models.CASCADE, null=True
    )
    author_name = models.CharField(max_length=60)
    content = models.CharField(max_length=500)
    creation_date = models.DateTimeField(null=True, auto_now_add=True)

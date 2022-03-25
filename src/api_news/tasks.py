from celery import shared_task
from api_news.models import Post


@shared_task
def reset_votes():
    post_list = Post.objects.all()
    for post in post_list:
        post.amount_of_upvotes = 0
        post.save()

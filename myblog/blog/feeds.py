from django.contrib.syndication.views import Feed
from .models import Post

class AllPostsRssFeed(Feed):
    title = 'django博客教程'
    link = '/'
    description = '最受小白欢迎的django博客教程'

    def items(self):
        return Post.objects.all()

    def item_title(self, item):
        return f'[{item.category}]{item.title}'

    def item_description(self, item):
        return item.body
from django.contrib.sitemaps import Sitemap
from .models import Post

class PostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 00.9

    def items(self):
        return Post.published.all()
    
    def lastmod(self, obj):
        return obj.updated
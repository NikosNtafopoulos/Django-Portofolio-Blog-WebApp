from django.db import models
from django.utils import timezone


from django.core.urlresolvers import reverse


# Create your models here.


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateField(default=timezone.now)
    published_date = models.DateField(blank=True, null=True)

    # publication date method -- in order to get the time when we hit publish and not before
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # comments method
    def approve_comments(self):
        return self.comments.filter(approved_comment=True)

    # what should i do when you create an instance of a post method
    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})  # go to post_detail page with the primary key of the post you just created


    # string represantation
    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        # listView
        return reverse('post_list')


    def __str__(self):
        return self.text

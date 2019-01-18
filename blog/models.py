from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=225)
    publication = models.DateTimeField()
    body = models.TextField()
    image = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]
    
    def publish_day_pretty(self):
        return self.publication.strftime("%b %e %Y")
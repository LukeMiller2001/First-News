from django.db import models

class Story(models.Model):
    story_heading = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')
    story_text = models.CharField(max_length=200)

    def __str__(self):
        return self.story_heading

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

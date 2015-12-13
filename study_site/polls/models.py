import datetime

from django.db import models
from django.utils import timezone

'''Question model class'''
class Question(models.Model):
    question_text = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('Date published')

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days = 1) <= self.pub_date <= now 
	
    def __str__(self):
	return self.question_text
    
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


'''Choice model class'''
class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default = 0)

    def __str__(self):
	    return self.choice_text



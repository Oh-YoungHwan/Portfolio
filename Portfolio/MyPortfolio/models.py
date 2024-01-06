from django.db import models

# Create your models here.

class admin_post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    important = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
class RobotsTxt(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    user_agent = models.CharField(db_column='User_agent', max_length=25)  # Field name made lowercase.
    disallow = models.CharField(db_column='Disallow', max_length=200)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'robots_txt'
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Task(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    '''we use a mone to many relationship we have one user and this user can have many items  '''
    '''on delete == what we do with the task if the user get deleted'''
    title=models.CharField(max_length=200)
    description=models.TextField(null=True,blank=True)
    complete=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
        
    class meta :
        ordering=['complete'] 

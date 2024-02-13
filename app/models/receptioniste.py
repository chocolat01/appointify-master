from django.db import models
from app.models import *
from app.models import User
from app.models import Cabinet


class Receptioniste(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    cabinet= models.ForeignKey(Cabinet,on_delete=models.CASCADE)
    
    
    def __str__(self) ->str:
       
       return self.user.first_name+" "+self.user.last_name+" "+self.cabinet.nom
    
    
    class Meta :
        constraints = [
            models.UniqueConstraint(
                fields=['user','cabinet',],
                 name = 'unique_receptioniste'
            )
        ]
    
from app.models import User, Specialite
from django.db import models
from phone_field import PhoneField

class Medecin(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    profile_photo = models.ImageField(default='default.png', upload_to='profile_images', verbose_name='Photo de profil', null=True, blank=True)
    specialite = models.ForeignKey(Specialite,on_delete=models.CASCADE)
   
    def __str__(self) ->str:
        return self.specialite.nom+" : "+self.user.first_name+" "+self.user.last_name
    
    class Meta :
        constraints = [
            models.UniqueConstraint(
                fields=['user','specialite'],
                name= 'unique_medecin'
            )
        ]
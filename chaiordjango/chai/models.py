from typing import Self
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class chaiVariety(models.Model):
    CHAI_TYPE_CHOICE=[
        ('Ml', 'Masala'),
        ('GR', 'Ginger'),
        ('EL', 'ELAICHI'),
        ('PL','PLAIN')
    ]
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='chais/')
    date_added=models.DateTimeField(default=timezone.now)
    type=models.CharField(max_length=2,choices=CHAI_TYPE_CHOICE)
    description = models.TextField(default='')


    def __str__(Self):
     return Self.name
    
# one to many

class chaiReview(models.Model):
   chai=models.ForeignKey(chaiVariety, on_delete=models.CASCADE,related_name='reviews')
   user=models.ForeignKey(User, on_delete=models.CASCADE)
   rating=models.IntegerField(default=0)
   comment=models.TextField()
   date_added=models.DateTimeField(default=timezone.now)

   def __str__(self):
      return f'{self.user.username}review for {self.chai.name}'

# Many to Many
class Store(models.Model):
   name = models.CharField(max_length=100)
   address = models.CharField(max_length=100)
   chai_Variety=models.ManyToManyField(chaiVariety,related_name='store')


   def __str__(self):
      return self.name
#one to one
class chaiCertificate(models.Model):
   chai=models.OneToOneField(chaiVariety, on_delete=models.CASCADE,related_name='certificate')
   certificate_number=models.CharField(max_length=100)
   issue_date=models.DateTimeField(default=timezone.now)

   def __str__(self):
      return f'Certificate for {self.chai.name}'


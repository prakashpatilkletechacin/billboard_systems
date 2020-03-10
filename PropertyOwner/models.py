from django.db import models

# Create your models here.
class owner(models.Model):

   name = models.CharField(max_length = 50)
   address = models.TextField()
   city= models.CharField(max_length = 50)
   phonenumber = models.IntegerField()
   email= models.EmailField()
   aadharno = models.CharField(max_length = 12)
   panno = models.CharField(max_length = 10)
   photo = models.ImageField()

   def __str__(self):
      return self.name

   class Meta:
      db_table = "owner"
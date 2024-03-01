from django.db import models

# Create your models here.
class User(models.Model):
    mail = models.EmailField(max_length=200)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return '<USER:id=:'+ str(self.id) +' name:' + self.name + '(' + self.mail + ')>'

class GoodJobMsg(models.Model):
    date = models.DateField()
    frName = models.CharField(max_length=100)
    toName = models.CharField(max_length=100)
    message = models.CharField(max_length=100)
    cardpath = models.CharField(max_length=100)
    savedCardPath = models.CharField(max_length=100)
    def __str__(self):
        return '<Msg:id=:'+ str(self.id) +' from:' + self.frName + 'to:' + self.toName + ')>'
    
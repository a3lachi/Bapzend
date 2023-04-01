from django.db import models


class Bapz(models.Model):
    productname  = models.CharField(max_length=120)
    category = models.TextField()
    price = models.TextField()
    color = models.TextField()
    size = models.TextField()
    id  = models.IntegerField(primary_key=True)

    def _str_(self):
        return self.title
    

class Customer(models.Model) :
    email = models.TextField()
    pwd = models.TextField()
    frstname = models.TextField()
    lstname = models.TextField()
    usrname =  models.TextField()
    commands = models.TextField()
    jwt = models.TextField()
    id  = models.IntegerField(primary_key=True)

    def _str_(self):
        return self.title

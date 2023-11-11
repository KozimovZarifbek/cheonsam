from django.db import models


class Banner(models.Model):
    back_photo = models.ImageField()
    logo = models.ImageField()
    title = models.CharField(max_length=225)
    photo = models.ImageField()

    def __str__(self):
        return self.title

class Species(models.Model):
    back_photo = models.ImageField()
    photo_1 = models.ImageField()
    photo_2 = models.ImageField()
    name = models.CharField(max_length=225)
    price = models.IntegerField()

    def __str__(self):
        return self.name





class Company(models.Model):
    back_photo = models.ImageField()
    name = models.CharField(max_length=225)
    text = models.TextField()
    photo = models.ImageField()



class Order(models.Model):
    name = models.CharField(max_length=225)
    phone = models.CharField(max_length=225)

    def __str__(self):
        return self.name




class Info(models.Model):
    text = models.TextField()
    photo = models.ImageField()



class Info_2(models.Model):
    image = models.ImageField()
    text = models.TextField()
    photo = models.ImageField()







class Question(models.Model):
    title = models.TextField()
    back_photo = models.ImageField()
    photo = models.ImageField()




class Manual(models.Model):
    back_photo = models.ImageField()
    name = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return self.name


class Facts(models.Model):
    back_photo = models.ImageField()
    name = models.CharField(max_length=225)
    number = models.IntegerField()
    text = models.TextField()

class Feedback (models.Model):
    logo = models.ImageField()
    title = models.CharField(max_length=225)
    tl= models.URLField
    fc = models.URLField()
    ins = models.URLField()
    yt = models.URLField()


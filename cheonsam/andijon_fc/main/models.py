from django.db import models

# Create your models here.
class Info(models.Model):
    tg = models.URLField()
    fb= models.URLField()
    youtube = models.URLField()
    x = models.URLField()
    logo = models.ImageField(upload_to='info/')
    number = models.IntegerField()
    email= models.EmailField()
    photo = models.ImageField(upload_to='info/')
    data = models.DateField()



class Frame(models.Model):
    title = models.TextField()
    photo = models.ImageField(upload_to='frame/')

class Turner(models.Model):
    photo = models.ImageField(upload_to='turner/')
    title = models.TextField()
    data = models.DateField()

class Calendar_info(models.Model):
    name = models.CharField(max_length=200)
    scory = models.IntegerField()
    logo = models.ImageField(upload_to='cl_info/')


class Calendar(models.Model):
    top = models.CharField(max_length=100)
    data = models.DateField()
    cl_info = models.ManyToManyField(Calendar_info)

class Reting(models.Model):
    logo = models.ImageField(upload_to='teting')
    name = models.CharField(max_length=200)
    oo= models.IntegerField()
    gg= models.IntegerField()
    dd= models.IntegerField()
    mm= models.IntegerField()
    tf= models.IntegerField()
    scory = models.IntegerField()

class Videao(models.Model):
    photo = models.ImageField(upload_to='frame/')
    name = models.CharField(max_length=200)
    video = models.URLField()

class Pley(models.Model):   
    photo = models.ImageField(upload_to="pley")
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    pasition= models.CharField(max_length=300)
    geyms = models.IntegerField()
    start = models.IntegerField()
    sap = models.IntegerField()
    minuts = models.IntegerField()



class Info_shop(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='info_shop/')


class Shop(models.Model):
    photo = models.ImageField(upload_to='shop/')
    command_name = models.CharField(max_length=200)
    name = models.CharField(max_length=200)


class Stadun(models.Model):
    name = models.CharField(max_length=200)
    tex = models.TextField()
    size = models.IntegerField


from django.db import models


class Info(models.Model):
    tg = models.URLField()
    fb= models.URLField()
    youtube = models.URLField()
    x = models.URLField()
    logo = models.ImageField(upload_to='info/')
    number = models.IntegerField()
    email= models.EmailField()
    photo = models.ImageField(upload_to='info/')
    data = models.DateField()



class Frame(models.Model):
    title = models.TextField()
    photo = models.ImageField(upload_to='frame/')

class Turner(models.Model):
    photo = models.ImageField(upload_to='turner/')
    title = models.TextField()
    data = models.DateField()

class Calendar_info(models.Model):
    name = models.CharField(max_length=200)
    scory = models.IntegerField()
    logo = models.ImageField(upload_to='cl_info/')


class Calendar(models.Model):
    top = models.CharField(max_length=100)
    data = models.DateField()
    cl_info = models.ManyToManyField(Calendar_info)

class Reting(models.Model):
    logo = models.ImageField(upload_to='teting')
    name = models.CharField(max_length=200)
    oo= models.IntegerField()
    gg= models.IntegerField()
    dd= models.IntegerField()
    mm= models.IntegerField()
    tf= models.IntegerField()
    scory = models.IntegerField()

class Videao(models.Model):
    photo = models.ImageField(upload_to='frame/')
    name = models.CharField(max_length=200)
    video = models.URLField()

class Pley(models.Model):   ##oyinchilar
    photo = models.ImageField(upload_to="pley")
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    pasition= models.CharField(max_length=300)
    geyms = models.IntegerField()
    start = models.IntegerField()
    sap = models.IntegerField()
    minuts = models.IntegerField()

class Info_shop(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='info_shop/')


class Shop(models.Model):
    photo = models.ImageField(upload_to='shop/')
    command_name = models.CharField(max_length=200)
    name = models.CharField(max_length=200)

class Photo_stadun(models.Model):
    photo = models.ImageField(upload_to='photosta/')

class Stadun(models.Model):
    name = models.CharField(max_length=200)
    tex = models.TextField()
    size = models.IntegerField()
    space = models.IntegerField()
    sector = models.IntegerField()
    map = models.CharField(max_length=300)
    number = models.IntegerField()
    photo = models.ManyToManyField(Photo_stadun)


class Partnior(models.Model):
    photo = models.ImageField(upload_to='partnior')

class Time(models.Model):  ##jamoa
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='time/')


class Menejment(models.Model):  ##raxbariat
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='menjment/')



class Triner(models.Model):
    photo = models.ImageField(upload_to='menjment/')
    name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    tex = models.TextField()




class Info_klub(models.Model):
    tex = models.TextField()
    icon = models.CharField(max_length=200)


class Klub(models.Model):
    photo = models.ImageField(upload_to='klub/')
    title = models.CharField(max_length=200)
    info = models.ManyToManyField(Info_klub)
    tex = models.TextField()
    photo2 = models.ImageField(upload_to='klub/')


class Reconandeshin(models.Model):  ## tavsialar
    photo = models.ImageField(upload_to='klub/')
    tex = models.TextField()
    data = models.DateField(auto_now_add=True)
    
    
class Akademy(models.Model):  ##raxbariat
    name = models.CharField(max_length=200)
    bg_photo = models.ImageField(upload_to='Akademy/')
     
     
class Mashgulotlar(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="Mashgulotlar/")
    
    
class Myshop(models.Model):
    text = models.TextField()
    bg_img = models.ImageField(upload_to='Myshop/')
    img = models.ImageField(upload_to='Myshop/')


class Shopping(madels.class (models.Model):
    photo = models.ImageField()
    title = models.TextField()
    photo_one = models.ImageField()
    photo_two = models.ImageField()
    text =  models.TextField()
    
    
class Gallery(models.Model):
    img = models.ImageField()
    text =  models.TextField()
    img1 = models.ImageField()
    img2 = models.ImageField()
    title =  models.TextField()
    img3 = models.ImageField()
    img4 = models.ImageField()
    img5 = models.ImageField()
    img6 = models.ImageField()
    img7 = models.ImageField()
    url = models.URLField()
    img8 = models.ImageField()
    img9 = models.ImageField()
    img10 = models.ImageField()
    
    
class Arena(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="Arena/")
    

class Arenawiki(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()
    img = models.ImageField()
    
    
class Area(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()
    photo = models.ImageField()
    
    
class Area2(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()
    photo = models.ImageField()
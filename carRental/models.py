from django.db import models
class adminLogin(models.Model):
  username=models.CharField(max_length=10)
  password= models.CharField(max_length=10)



class user(models.Model):
    loginid = models.ForeignKey(adminLogin , on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    contact=models.CharField(max_length=12)
    email=models.CharField(max_length=50)
    u_image = models.ImageField(upload_to='images', default='images/defaultuser.jpeg')
    v_image = models.ImageField(upload_to='vimages',default='images/defv.jpeg')
class car(models.Model):
    name = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    company=models.CharField(max_length=12)
    price=models.FloatField(max_length=50)
    rentPerDay = models.FloatField(max_length=20)
    fuel = models.CharField(max_length=20)


    c_image=models.ImageField(upload_to='cimages',default='images/defaulcar.jpeg')

class feed(models.Model):
    fid = models.ForeignKey(user, on_delete=models.CASCADE)
    feedback = models.CharField(max_length=20)
    name=models.CharField(max_length=12)
class carRent(models.Model):
    uid = models.ForeignKey(user, on_delete=models.CASCADE)
    cid = models.ForeignKey(car, on_delete=models.CASCADE)
    dateStart =models.DateTimeField(default='0000-00-00 00:00:00', blank=True, null=True)
    dateEnd=models.DateTimeField(default='0000-00-00 00:00:00', blank=True, null=True)
    dur=models.IntegerField()
    rentPerday=models.FloatField(max_length=10)
    amnt=models.FloatField(max_length=10)
    discount=models.FloatField(max_length=10,default=0.0)
    finalAmount=models.FloatField(max_length=10)
    returened=models.CharField(max_length=12,default="NO")
    status = models.CharField(max_length=12, default="NOT ACCEPTED")


# Create your models here.

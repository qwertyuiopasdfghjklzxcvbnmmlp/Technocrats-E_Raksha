from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.

class Blog(models.Model):
    s_no = models.AutoField(primary_key=True )
    b_name = models.CharField(max_length=100000)
    b_descp = models.TextField()
    b_author = models.CharField(max_length=5000)
    b_date = models.DateField(default="No description")
    b_photo = models.FileField(upload_to='images/%y')

    class Meta:
        verbose_name_plural = "Blogs"
    def __str__(self):
        return self.b_name

class BlogComment(models.Model):
    sno= models.AutoField(primary_key=True)
    comment=models.TextField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ForeignKey(Blog, on_delete=models.CASCADE)
    parent=models.ForeignKey('self',on_delete=models.CASCADE, null=True )
    timestamp= models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:13] + "..." + "by" + " " + self.user.username
    
 
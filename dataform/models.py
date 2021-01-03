from django.db import models

class EmailForm(models.Model):
    name = models.CharField(max_length=32)
    email = models.EmailField(max_length=64)
    phone = models.CharField(max_length=14)
    mes = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, db_index=True)

class EmailImage(models.Model):
    form = models.ForeignKey(EmailForm, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(blank=True, upload_to='images/form/%Y/%m/%d')


from django.db import models

class Album(models.Model):
    name       = models.CharField(max_length=50)
    singer     = models.CharField(max_length=50)
    images_url = models.CharField(max_length=500,null=True)
    link_url   = models.CharField(max_length=500,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'albums'
        
class SupportCompany(models.Model):
    name       = models.CharField(max_length=50)
    images_url = models.CharField(max_length=500,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'support_companys'
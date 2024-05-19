from django.db import models

# Create your models here.

# class Bank(models.Model):
#     name = models.CharField(max_length=255)
#     city = models.CharField(max_length=255) # 시
#     district = models.CharField(max_length=255) # 구
#     latitude = models.FloatField()
#     longitude = models.FloatField()
    
#     def __str__(self):
#         return f"{self.name} ({self.city}, {self.district})"
# class Bank(models.Model):
#     name = models.CharField(max_length=255)
#     address = models.CharField(max_length=255)
#     road_address = models.CharField(max_length=255, blank=True, null=True)
#     phone = models.CharField(max_length=20, blank=True, null=True)
#     x = models.CharField(max_length=50)
#     y = models.CharField(max_length=50)
#     category_name = models.CharField(max_length=255, blank=True, null=True)
#     place_url = models.URLField(max_length=500, blank=True, null=True)
    
#     def __str__(self):
#         return f"{self.name} ({self.address})"
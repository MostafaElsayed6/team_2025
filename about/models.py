from django.db import models

class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    # description = models.TextField()
    description = models.TextField(default="No description") 
    image = models.ImageField(upload_to='team/')
    phone = models.CharField(max_length=20, blank=True)
    
    def __str__(self):
        return self.name
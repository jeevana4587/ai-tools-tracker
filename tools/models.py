from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
      return self.name 

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Category"

ACCESS_TYPE_CHOICES = [
        ('Free', 'Free'),
        ('Paid', 'Paid'),
        ('Freemium', 'Freemium'),  
]
class Tool(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to= 'tools_logo/',null = True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    website = models.URLField()
    description = models.TextField()
    access_type = models.CharField(
        max_length=20,
        choices=ACCESS_TYPE_CHOICES,
        default='Free'
    )
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Tool"
        verbose_name_plural = "Tool"


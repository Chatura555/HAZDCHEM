from django.db import models

class Chemical(models.Model):
    name = models.CharField(max_length=100)
    expiry_date = models.DateField()
    hazard_rating = models.CharField(max_length=50, choices=[
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High')
    ])
    chemical_type = models.CharField(max_length=50)  # Organic, Inorganic, etc.
    banned_status = models.BooleanField(default=False)
    description = models.TextField(blank=True)  # Ensure this line is present

    def __str__(self):
        return self.name
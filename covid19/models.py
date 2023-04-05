from django.db import models

class Country(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    total_confirmed_cases = models.IntegerField()
    total_deaths_cases = models.IntegerField()
    total_recovered_cases = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return self.name



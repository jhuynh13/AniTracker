from django.db import models

# Create your models here.
#Basically classes go here with data
# for example car, engine, wheel

class Category (models.Model):
    # class attributes
    name = models.CharField(max_length=200)

    # Returns name of this object when displaying db objects
    def __str__(self):
        return self.name
    
# Represents the row containing geoName and score when interest by region function is run
class Item (models.Model):
    # on delete models cascade if to do list is removed then all items are removed
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    geoName = models.CharField(max_length=200)
    score = models.IntegerField()

    def __str__(self):
        return self.geoName
import datetime
from django.db import models
from django.utils.timezone import now

class CarMake(models.Model):
    name = models.CharField(max_length=50, default="name")
    description = models.CharField(max_length=200, default="description")
    
    #course = models.ForeignKey(Course, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class CarModel(models.Model):
    SEDAN = 'Sedan'
    SUV = 'SUV'
    WAGON = 'Wagon'
    MINIVAN = "Mini"
    TRUCK = "Truck"
    CAR_MODES = [
        (SEDAN, 'Sedan'),
        (SUV, 'SUV'),
        (WAGON, 'Wagon'),
        (MINIVAN, "Mini"),
        (TRUCK,"Truck")
    ]

    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default="name")
    dealer_id = models.IntegerField(default=50)
    model_type = models.CharField(max_length=15, choices=CAR_MODES, default=SEDAN)

    YEAR_CHOICES = []
    for r in range(1985, (datetime.datetime.now().year+1)):
        YEAR_CHOICES.append((r, r))

    year = models.IntegerField(
        ('year'), choices=YEAR_CHOICES, default=datetime.datetime.now().year)

    def __str__(self):
        return self.name + ", " + str(self.year) + ", " + self.model_type


# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data

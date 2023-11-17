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
class CarDealer:

    def __init__(self, address, city, full_name, id, lat, long, short_name, st, zip):
        self.address = address
        self.city = city
        self.full_name = full_name
        self.id = id
        self.lat = lat
        self.long = long
        self.short_name = short_name
        self.st = st
        self.zip = zip

    def __str__(self):
        return "Dealer name: " + self.full_name


# <HINT> Create a plain Python class `DealerReview` to hold review data
# A plain Python class to hold review data
class DealerReview:
    def __init__(self, dealership, id, name, purchase, review, car_make=None, car_model=None, car_year=None, purchase_date=None, sentiment="neutral"):
        self.car_make = car_make
        self.car_model = car_model
        self.car_year = car_year
        self.dealership = dealership
        self.id = id  # The id of the review
        self.name = name  # Name of the reviewer
        self.purchase = purchase  # Did the reviewer purchase the car? bool
        self.purchase_date = purchase_date
        self.review = review  # The actual review text
        self.sentiment = sentiment  # Watson NLU sentiment analysis of review

    def __str__(self):
        return "Reviewer: " + self.name + " Review: " + self.review

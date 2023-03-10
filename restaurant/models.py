from django.db import models

# Create your models here.
class Booking(models.Model):
    name= models.CharField(max_length=255)
    numb_of_guests = models.SmallIntegerField(6)
    booking_date = models.DateTimeField()
    
    def __str__(self) -> str:
        return f'{self.name} booked for {str(self.numb_of_guests)} persons on {self.booking_date}'

class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()

    def __str__(self) -> str:
        return f'{self.title} : {str(self.price)}'
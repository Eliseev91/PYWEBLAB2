from django.db import models

# Create your models here.

class Booking(models.Model):
    book_ref = models.AutoField(primary_key=True)
    book_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.FloatField(null=False)

    def __str__(self):
        return f'{self.book_ref}-{self.book_date}'


class Tickets(models.Model):
    ticket_no = models.PositiveIntegerField(primary_key=True)
    book_ref = models.ForeignKey(Booking, on_delete=models.CASCADE)
    passenger_id = models.IntegerField(null=False)
    passenger_name = models.CharField(max_length=100)
    contact_data = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.passenger_id}-{self.ticket_no}'


class TicketFlight(models.Model):
    ticket_no = models.ForeignKey(Tickets, on_delete=models.CASCADE)
    flight_id = models.ForeignKey('Flight', on_delete=models.CASCADE)

    class Meta:
        unique_together = (('ticket_no', 'flight_id'),)

    def __str__(self):
        return f'{self.ticket_no} - {self.flight_id}'


class Flight(models.Model):
    flight_id = models.PositiveIntegerField(primary_key=True)

    departure_airport = models.ForeignKey('Airports', related_name='departure', on_delete=models.CASCADE)

    arrival_airport = models.ForeignKey('Airports', related_name='arrival', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.flight_id}'


class Aircraft(models.Model):
    aircraft_code = models.PositiveIntegerField(primary_key=True)
    model = models.CharField(max_length=100)
    range = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.aircraft_code} - {self.model}'


class Airports(models.Model):
    airport_code = models.AutoField(primary_key=True)
    airport_name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    coordinates = models.TextField(max_length=100)

    def __str__(self):
        return f'{self.airport_code} - {self.airport_name} - {self.city}'


class Seat(models.Model):
    aircraft_code = models.ForeignKey(Aircraft, on_delete=models.CASCADE)
    seat_no = models.CharField(null=False, max_length=3)
    fare_conditions = models.CharField(max_length=250, null=False)

    def __str__(self):
        return f'{self.aircraft_code} - {self.seat_no}'


class BoardingPasses(models.Model):
    ticket_no = models.ForeignKey(TicketFlight, on_delete=models.CASCADE, related_name='ticket_no1')
    flight_id = models.ForeignKey(TicketFlight, on_delete=models.CASCADE, related_name='flight_id1')
    boarding_no = models.PositiveIntegerField(null=False)
    seat_no = models.ForeignKey(Seat, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.boarding_no} - {self.seat_no}'

    class Meta:
        unique_together = (('ticket_no', 'flight_id'),)




# departure_airport_airport_code = 'DME'
#
# Flight.objects.all().filter(departure_airport_airport_code = departure_airport_airport_code)

from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Booking)
admin.site.register(Tickets)
admin.site.register(Flight)
admin.site.register(TicketFlight)
admin.site.register(Aircraft)
admin.site.register(Airports)
admin.site.register(Seat)
admin.site.register(BoardingPasses)

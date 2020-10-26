from djreservation.views import SimpleProductReservation
from .models import MyModel

class RoomReservation(SimpleProductReservation):
    base_model = MyModel     # required
    amount_field = 'quantity'  # required
    max_amount_field = 'max_amount' # required
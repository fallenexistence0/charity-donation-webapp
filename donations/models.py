from django.db import models

# This model represents a single donation entry in the database.
class Donation(models.Model):
    # Optional donor name. Can be left blank for anonymous donations. Need to make the option clear on the webpage
    name = models.CharField(max_length=100, blank=True)

    # The donation amount in USD. Stored with high decimal precision.
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    # A box that lets the user leave a custom message whcih will be displayed on a board.
    message = models.TextField(blank=True)

    # Timestamp of when the donation was created. Automatically set.
    timestamp = models.DateTimeField(auto_now_add=True)

    # This defines how each donation will appear in the Django admin.
    def __str__(self):
        return f"{self.name or 'Anonymous'} - ${self.amount}"

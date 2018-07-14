import uuid
from django.db import models
from django.utils import timezone
# Create your models here.
class Wallet(models.Model):
    wallet_id = models.UUIDField(default=uuid.uuid4,primary_key=True)
    wallet_name = models.CharField(max_length=128, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    amount = models.IntegerField(default=0, null=True, blank=True)
    created_on = models.DateField(default=timezone.now, null=True, blank=True)


    def __str__(self):
        return str(self.wallet_id)

class User(models.Model):
    user_id=models.UUIDField(default=uuid.uuid4,primary_key=True)
    name = models.CharField(max_length=128, null=True, blank=True)
    phone = models.CharField(max_length=128, null=True, blank=True)
    email = models.CharField(max_length=128, null=True, blank=True)
    username = models.CharField(max_length=128, null=True, blank=True)
    password = models.CharField(max_length=128, null=True, blank=True)
    wallet_code = models.ForeignKey(Wallet, related_name="wallet_code", null=True, blank=True)
    joined_on = models.DateField(default=timezone.now, null=True, blank=True)
    personal_amount = models.IntegerField(default=0,null=True, blank=True)
    amount_taken = models.IntegerField(default=0, null=True, blank=True)
    group_contribution = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return str(self.user_id)

class Logs(models.Model):
    wallet = models.ForeignKey(Wallet, related_name="wallet")
    user = models.ForeignKey(User, related_name="user", null=True, blank=True)
    log_id=models.UUIDField(default=uuid.uuid4,primary_key=True)
    user_name = models.CharField(max_length=128, null=True, blank=True)
    date = models.DateField(default=timezone.now, null=True, blank=True)
    amount_added =models.IntegerField(null=True, blank=True)
    amount_withdrawn=models.IntegerField( null=True, blank=True)
    description = models.TextField( default=None,null=True, blank=True)

    def __str__(self):
        return str(self.log_id)








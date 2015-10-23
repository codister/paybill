from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
#######################
# Models for the PB app
#######################


# Inherting Users to make them Merchents
class Merchent(models.Model):
	# --- One to One Relationship key to connect to django default User Model
	user = models.ForeignKey(User)
	# --- Contact Number
	contact_num = models.CharField(max_length=128)
	# --- Landline (Default Null)
	landline_num = models.CharField(max_length=128)
	# --- CNIC (File Photo Field)
	cnic_photo = models.ImageField(upload_to='cnic_images', blank=True)
	# --- Selfi Holding CNIC (Default Null)
	cinc_selfi_photo = models.ImageField(upload_to='cnic_selfi_images', blank=True)
	# --- Email Verified Status
	isverified_email = models.BooleanField(default=False)
	# --- Account Status (string)
	is_account_active = models.BooleanField(default=False)
	# --- Is Approved by Admin (Default to False)
	is_admin_approve = models.BooleanField(default=False)
	# --- IS Blocked by admin (default to false)
	is_admin_blocked = 	models.BooleanField(default=False)
	# --- ID number provided by billing company
	billing_id_number = models.CharField(max_length=128)
	# --- Balance Earned
	total_earnings = models.IntegerField(default=0)


# Requests Model to Store Requests Mostly refered as bill request
class Request(models.Model):
	# --- Current time when request was submitted (Timestamp)
	date_time = models.DateTimeField(auto_now=True)
	# --- Type (Forign key to Request type Model)
	bill_type = models.CharField(max_length=128)
	# --- Bill Payment Companies (Create a New Model Forign KEy)
	billing_company = models.CharField(max_length=128)
	# --- Payment form (Default to BTC for now)
	payment_method = models.CharField(max_length=128, default="BTC")
	# --- Country Name (String Perhaps create additional Table)
	country = models.CharField(max_length=128, default="Pakistan")
	# --- Due Bill amount in PKR (Float)
	pkr_bill_amount = models.IntegerField(default=0)
	# --- Contact Number (String or Numric we'll see that)
	contact_num = models.CharField(max_length=128)
	# --- Bill Indentifier Number (String)
	bill_id_num = models.CharField(max_length=128)
	# --- Payment status isPaid or completed? (Boolean)
	is_paid = models.BooleanField(default=False)
	# --- Is Request Processed Status? or Pending (Boolean)
	is_completed = models.BooleanField(default=False)
	# --- Error / Issue Message
	issue_message = models.TextField(default="No Error or Issue all Clear ")
	# --- In response to completion request TXID
	confirmation_txid = models.CharField(default="No Information ID Provided",  max_length=128)
	# --- BTC confirmations count [int]
	btc_confirmations = models.IntegerField(default=0)
	# --- BTC Wallet on which payment was received
	btc_address = models.CharField(max_length=400)
	# --- Amount of BTC recived
	btc_amount = models.FloatField(default=0)
	# --- Email assoicated with the request to send out Automated email
	email_address = models.CharField(max_length=100, blank=True)
	# --- if we have more then 6 confirmations then we mark this transaction completed
	payment_completed = models.BooleanField(default=False)
	# --- can be completed token expires after 30 mints
	request_token = models.BooleanField(default=True)
	# --- Time at Request was Claimed
	time_claimed_on = models.DateTimeField(blank=True)
	# --- who claims the Bill Request --- #
	claimer = models.ForeignKey(Merchent,default="1")





# Payments to User Model to store payments for users 
# One to many relationship to User Merchent Model
class Payment(models.Model):
	# --- Timestamp when payment is created
	date_time = models.DateTimeField(auto_now=True)
	# --- The merchent to whom the payment belongs (ONE TO many to Merchents)
	merchent = models.ForeignKey(Merchent)
	# --- Payment Status (Error, Pending, onHold, Paid )
	payment_status = models.CharField(max_length=128)
	# --- Payment amount
	payment_amount = models.IntegerField(default=0)
	# --- Paid via (BTC or Cash)
	payment_method = models.CharField(max_length=128)
	# --- Error Message
	error_message = models.TextField(default="Payment Authorized No Error Messages")


class Company(models.Model):
	# --- Name of the company
	name = models.CharField(max_length=128)
	# --- Supported Bill type
	bill_type = models.CharField(max_length=128)
	# --- Country in Operating
	country = models.CharField(max_length=128)

	def __str__(self):
		return self.name
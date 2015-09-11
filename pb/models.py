from django.db import models

# Create your models here.






# Inherting Users to make them Merchents
# --- One to One Relationship key to connect to django default User Model
# --- Contact Number
# --- Landline (Default Null)
# --- CNIC (File Photo Field)
# --- Selfi Holding CNIC (Default Null)
# --- Email Verified Status
# --- Account Status (string)
# --- Is Approved by Admin (Default to False)
# --- IS Blocked by admin (default to false)
# --- ID number provided by billing company
#






# Requests Model to Store Requests
# --- Current time when request was submitted (Timestamp)
# --- Type (Forign key to Request type Model)
# --- Bill Payment Companies (Create a New Model Forign KEy)
# --- Payment form (Default to BTC for now)
# --- Country Name (String Perhaps create additional Table)
# --- Ammount Paid in PKR (Float)
# --- Contact Number (String or Numric we'll see that)
# --- Bill Indentifier Number (String)
# --- Payment status isPaid or completed? (Boolean)
# --- Is Request Processed Status? or Pending (Boolean)
# --- Requested Completed by Merchent Forign Key
# --- Is Request Claimed to be Process (True or False)
# --- Time Remainig to process a request (Default Null)
# --- Commision to be Taken by Site Admins
# --- Error / Issue Message
# --- In response to completion request TXID
# --- BTC confirmations count [int]
# --- BTC Wallet on which payment was recived 
# --- Amount of BTC recived
# --- Time at Request was Claimed





# Payments to User Model to store payments for users 
# One to many relationship to User Merchent Model
# --- Timestamp when payment is created
# --- The merchent to whom the payment belongs (ONE TO many to Merchents)
# --- Payment Status (Error, Pending, onHold, Paid )
# --- Payment Ammount
# --- Paid via (BTC or Cash)
# --- Error Message





# Request type one to one relationship to Request Model
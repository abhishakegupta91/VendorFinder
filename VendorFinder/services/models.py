# Import
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator, MaxValueValidator, MinValueValidator


# CHOICE_FIELDS
SEX_CHOICE = [
        ('F','Female'),
        ('M','Male'),
        ('N','Not to Say'),
]

# Models Here
class Status(models.Model):
    is_active = models.BooleanField(default=False)
    status_name = models.CharField(max_length=124)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
            return self.status_name
    class Meta:
        db_table = 'status'


class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_vendor = models.BooleanField(default=False)
    phone = models.CharField(validators=[RegexValidator(regex=r'^[9876]\d{9}$', message="Please Enter Correct Phone Number", code='nomatch'
    )],
    max_length=10)
    sex = models.CharField(max_length=1, choices=SEX_CHOICE, blank=True)
    pincode = models.CharField(max_length=6,blank=True)
    address = models.CharField(max_length=124,blank=True)
    city = models.CharField(max_length=124,blank=True)
    state = models.CharField(max_length=124,blank=True)
    last_modified = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
    class Meta:
        db_table = 'user'


class Vendor(models.Model):
    vendor = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    customer_served = models.PositiveSmallIntegerField()
    rating = models.PositiveSmallIntegerField()
    #number_of_services = models.PositiveSmallIntegerField() #Used to track total number of services served by a vendor
    #active_since = models.DateField()

    def __str__(self):
       return self.user.username

    class Meta:
        db_table = 'vendor'


class Customer(models.Model):
    customer = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    service_taken = models.PositiveSmallIntegerField()
    #active_since = models.DateField()
    
    def __str__(self):
       return self.user.username

    class Meta:
        db_table = 'customer'


class Admin(models.Model):
    admin = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    sex = models.CharField(max_length=1, choices=SEX_CHOICE, blank=True)
    #qualification = model.TextField()
    #member_since = model.DateTime(auto_now=True)

    def __str__(self):
       return self.user.username

    class Meta:
        db_table = 'admin'


class Otp(models.Model):
    otp_id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    generation_time = models.DateTimeField(auto_now=True)
    #expiry_time = models.DateTimeField(auto_now=True)

    def __str__(self):
       return self.user.username

    class Meta:
        db_table = 'otp'


class Service(models.Model):
    is_active = models.BooleanField(default=False)
    service_name = models.CharField(max_length=124)
    service_charge = models.DecimalField(max_digits=10, decimal_places=2)
    #admin = models.ForeignKey(Admin, models.SET_NULL)
    #To keep track of admin, who has added the service
    last_modified = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
       return self.service_name

    class Meta:
        db_table = 'service'


class SubService(models.Model):
    is_active = models.BooleanField(default=False)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    sub_service_name = models.CharField(max_length=124)
    #admin = models.ForeignKey(Admin, models.SET_NULL)
    #To keep track of admin, who has added the service
    last_modified = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sub_service_name

    class Meta:
        db_table = 'sub_service'


class VendorService(models.Model):
    is_active = models.BooleanField(default=False)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    sub_service = models.ForeignKey(SubService, on_delete=models.CASCADE)
    sub_service_charge = models.DecimalField(max_digits=10, decimal_places=2)
    last_modified = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
       return self.sub_service.sub_service_name
    # What should be returned : Vendor's name, service name or sub_service name

    class Meta:
        db_table = 'vendor_service'

class VendorCustomer(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    sub_service = models.ForeignKey(SubService, on_delete=models.CASCADE)
    status = models.ForeignKey(Status,on_delete=models.SET_NULL, null=True)
    total_charge = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    last_modified = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    #Name of the vendor must be set as default, because it is possible that when vendor is deleted,
    #customer is not deleted, and the record must exist. Same thing applies in case of customer
    # i.e. Either on delete, null value is set as default value (models.SET_NULL) or the name of 
    #vendor or customer should be set from database.

    #def __str__(self):
    #    return self.service.service_name
    # What should be returned : Vendor's name, service name or sub_service name

    class Meta:
        db_table = 'vendor_customer'


# class Invoice(models.Model):
#     pass

#     #def __str__(self):
#     #    return self.service.service_name
#     # What should be returned : Vendor's name, service name or sub_service name

#     class Meta:
#         db_table = 'otp'

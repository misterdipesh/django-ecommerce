from django.db import models
from django.contrib.auth.models import  AbstractBaseUser,BaseUserManager
class AccountManager(BaseUserManager):
    def create_user(self,email,username,first_name,last_name,password=None):
        if not email:
            raise ValueError("Email is required")
        if not username:
            raise ValueError("Username is required")
        if not first_name:
            raise ValueError("First Name is required")
        if not last_name:
            raise ValueError("Last Name is required")
        user=self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,email,username,password,first_name,last_name):
        user=self.create_user(
            email=self.normalize_email(email),
            password=password,
            first_name=first_name,
            last_name=last_name,
            username=username
        )
        user.is_admin=True
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)
class Account(AbstractBaseUser):
    email=models.EmailField(verbose_name='email',max_length=60,unique=True)
    username=models.CharField(max_length=30,unique=True)
    date_joined=models.DateField(verbose_name='date joined',auto_now_add=True)
    date_login=models.DateField(verbose_name='last login',auto_now=True)
    is_admin=models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    first_name=models.CharField(max_length=20,verbose_name='first name')
    last_name=models.CharField(max_length=20,verbose_name='last name')
    address=models.CharField(max_length=50)
    contact=models.CharField(max_length=15)
    USERNAME_FIELD='email'
    REQUIRED_FIELDS = ['first_name','last_name','username']
    objects=AccountManager()
    def __str__(self):
        return self.email
    def has_perm(self,perm,obj=None):
        return self.is_admin
    def has_module_perms(self,app_label):
        return True
class Product(models.Model):
    product_name=models.CharField(max_length=100)
    product_description=models.TextField()
    product_quantiy=models.IntegerField()
    product_brand=models.CharField(max_length=30)
    product_added_on=models.DateField(auto_now=True)
    product_price=models.BigIntegerField()
    product_is_avaliable=models.BooleanField()
    product_image=models.ImageField(null=True,upload_to='products/')


class Purchase(models.Model):
    product_purchased=models.ForeignKey(Product,on_delete=models.CASCADE)
    purchased_by=models.ForeignKey(Account,on_delete=models.CASCADE)
    purchased_on=models.DateField()
    purchased_quantity=models.IntegerField()




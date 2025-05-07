from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _

# -------------------------------------------
# Custom manager for the custom UserProfile model
# -------------------------------------------
class UserProfileManager(BaseUserManager):
    # Method to create a regular user
    def create_user(self,email,password=None,**extra_fields):
        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        user = self.model(email = email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    

     # Method to create a superuser (admin)
    def create_superuser(self,email,password=None,**extra_fields):

        # Set default fields for superuser
        extra_fields.setdefault("is_staff",True)
        extra_fields.setdefault("is_superuser",True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True"))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True"))
        
        return self.create_user(email,password,**extra_fields)

from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    """
    Django requires that custom users define their own Manager class. By
    inheriting from `BaseUserManager`, we get a lot of the same code used by
    Django to create a `User` for free. 

    All we have to do is override the `create_user` function which we will use
    to create `User` objects.
    """

    use_in_migrations = True

    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email, username and password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(email=self.normalize_email(email))

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Create and return a `User` with superuser powers.

        Superuser powers means that this use is an admin that can do anything
        they want.
        """
        if password is None:
            raise TypeError("Superusers must have a password")

        user = self.create_user(email, password=password)

        user.is_superuser = True
        user.is_admin = True
        user.save(using=self._db)

        return user

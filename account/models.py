from django.db                  import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    fullname     = models.CharField(null=True, max_length=50)
    phone_number = models.CharField(null=True, max_length=50)
    birth_date   = models.CharField(null=True, max_length=50)
    portfolio    = models.ManyToManyField('portfolio.Portfolio', 
                                          through='portfolio.LikePortfolio', 
                                          related_name='user_portfolio')

    class Meta:
        db_table = 'users'
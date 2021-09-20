from django.db                  import models
from django.contrib.auth.models import User


class Account(models.Model):
    user         = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=50, null=True)
    birth_date   = models.DateField(null=True)
    portfolio    = models.ManyToManyField(
                        'portfolio.Portfolio', 
                        through='portfolio.LikePortfolio'
                    )

    class Meta:
        db_table = 'accounts'
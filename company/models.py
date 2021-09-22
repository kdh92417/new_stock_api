from django.db import models


class Company(models.Model):
    cp_name         = models.CharField(max_length=1000)
    corp_code       = models.CharField(max_length=100, null=True)
    count_searching = models.IntegerField(default=0)
    total_like      = models.IntegerField(default=0)
    user            = models.ManyToManyField("account.User", through='LikeCompany')

    class Meta:
        db_table = 'companies'


class LikeCompany(models.Model):
    company = models.ForeignKey("Company", on_delete=models.CASCADE)
    user    = models.ForeignKey("account.User", on_delete=models.CASCADE)

    class Meta:
        db_table = 'like_companies'
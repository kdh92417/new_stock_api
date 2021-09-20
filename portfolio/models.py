from django.db import models


class Portfolio(models.Model):
    name         = models.CharField(max_length=100)
    content      = models.CharField(max_length=1000)
    total_like   = models.IntegerField(default=0)
    search_count = models.IntegerField(default=0)
    create_date  = models.DateTimeField(auto_now_add=True, null=True)
    modify_date  = models.DateTimeField(auto_now=True, null=True)
    user         = models.ForeignKey(
                        "account.Account", 
                        on_delete=models.CASCADE,
                        related_name='user_portfolios'
                    )
    company      = models.ManyToManyField(
                        "company.Company", through='PortfolioStock'
                    )

    class Meta:
        db_table = 'portfolios'


class Comment(models.Model):
    user_name   = models.CharField(max_length=50)
    content     = models.CharField(max_length=1000)
    create_date = models.DateTimeField(auto_now_add=True, null=True)
    modify_date = models.DateTimeField(auto_now=True, null=True)
    portfolio   = models.ForeignKey('Portfolio', on_delete=models.CASCADE)
    user        = models.ForeignKey('account.Account', on_delete=models.CASCADE)

    class Meta:
        db_table = 'comments'


class LikePortfolio(models.Model):
    user      = models.ForeignKey('account.Account', on_delete=models.CASCADE)
    portfolio = models.ForeignKey(
                    'portfolio.Portfolio', on_delete=models.CASCADE
                )

    class Meta:
        db_table = 'like_portfolio'


class PortfolioStock(models.Model):
    shares_count  = models.IntegerField(default=0)
    shares_amount = models.IntegerField(default=0)
    company       = models.ForeignKey(
                        'company.Company', on_delete=models.CASCADE
                    )
    portfolio     = models.ForeignKey(
                        'portfolio.Portfolio', on_delete=models.CASCADE
                    )

    class Meta:
        db_table = 'portfolio_stocks'
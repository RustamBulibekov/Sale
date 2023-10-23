from django.db import models

# Create your models here.


class Advertisement(models.Model):
    title = models.CharField(max_length=40)
    content = models.TextField(null=True, blank=True)
    price = models.FloatField()
    published = models.DateTimeField(auto_now_add=True, db_index=True)
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT,name='rubric')

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name_plural = 'Advertisements'
        verbose_name = 'Advertisement'
        ordering = ['-published']




class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='rubric')

    def __str__(self):
        return f'{self.name}'




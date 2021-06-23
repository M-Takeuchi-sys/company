from django.db import models

DEPARTMENT_CHOICES = (
        (1, '営業部'),
        (2, '総務部'),
        (3, '製造部'),
    )
class Employee(models.Model):
    name = models.CharField('名前', max_length=30)
    department = models.IntegerField('所属部署', choices=DEPARTMENT_CHOICES, blank=True, null=True)
    hire_date = models.DateField('入社日', blank=True, null=True)

    def __str__(self):
        return self.name

from django.db import models


class AuditEntity(models.Model):
    created_on = models.DateTimeField(auto_now_add=True, )
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Department(AuditEntity):
    name = models.CharField(max_length=20, )

    class Meta:
        ordering = ('company', 'first_name',)


class Employee(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40, null=True, blank=True)
    egn = models.CharField(max_length=10)
    job_title = models.IntegerField(choices=(
        (1, 'Software Developer'),
        (2, 'QA'),
        (3, 'DevOps'),
    ))
    department = models.ForeignKey(Department, on_delete=models.CASCADE)


class TestModel(models.Model):
    id2 = models.IntegerField(primary_key=True, )

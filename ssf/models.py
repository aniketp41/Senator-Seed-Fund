from django.db import models
from .choices import *
from django.contrib.auth.models import User
from datetime import datetime


class AdminPost(models.Model):
    post_name = models.CharField(max_length=50, null=True, blank=True)  # Will have choices
    post_holder = models.OneToOneField(User, null=True, blank=True)
    pin = models.IntegerField(null=True, blank=True, unique=True)
    council = models.CharField(max_length=50, choices=COUNCIL, null=True, blank=True)

    def __str__(self):
        return self.post_name


class SenateSeedFund(models.Model):
    created_by = models.ForeignKey(User, null=True, blank=True)
    activity_name = models.CharField(max_length=100)
    description = models.TextField(max_length=10000, null=True, blank=True)
    ssf = models.IntegerField(default=0)
    amount_given = models.IntegerField(default=0, null=True, blank=True)
    council = models.CharField(max_length=50, choices=COUNCIL, null=True, blank=True)
    entity = models.CharField(max_length=50, null=True, blank=True)
    status = models.CharField(max_length=50, choices=FORM_STATUS, default='in progress')
    approval = models.ManyToManyField(AdminPost, related_name='approvals', symmetrical=False, blank=True)
    chair_level = models.NullBooleanField(default=False, null=True)
    released = models.NullBooleanField(default=False, null=True)
    fin_convener = models.NullBooleanField(default=False, null=True)
    contributers = models.ManyToManyField(User, related_name='contributers', symmetrical=False, blank=True)
    deadline = models.DateTimeField(null=True, blank=True)

    rejected = models.NullBooleanField(default=False, null=True)
    reject_message = models.TextField(max_length=2000, null=True, blank=True)

    def __str__(self):
        return self.activity_name


class SenatorFund(models.Model):
    senator = models.OneToOneField(User, null=True, blank=True)
    max_amount = models.IntegerField(null=True, blank=True)
    pledged = models.IntegerField(default=0, null=True, blank=True)
    amount_left = models.IntegerField(default=max_amount, null=True, blank=True)

    def __str__(self):
        return str(self.max_amount)


class Contribution(models.Model):
    ssf = models.ForeignKey(SenateSeedFund, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateTimeField(auto_now=True)
    contributer = models.ForeignKey(User, null=True, blank=True)
    contribution = models.IntegerField()

    def __str__(self):
        return self.ssf.activity_name


class SenatePost(models.Model):
    user = models.OneToOneField(User, null=True, blank=True)
    session = models.CharField(max_length=10, choices=SESSION)
    fund = models.OneToOneField(SenatorFund, null=True, blank=True)

    def __str__(self):
        return self.user.username


class GeneralBodyMember(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=40, blank=True)
    roll_no = models.IntegerField(null=True)
    programme = models.CharField(max_length=7, choices=PROGRAMME, default='B.Tech')
    department = models.CharField(max_length=200, choices=DEPT, default='AE')
    hall = models.CharField(max_length=10, choices=HALL, default=1)
    room_no = models.CharField(max_length=10, null=True, blank=True)
    contact = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return str(self.name)


from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser

# models are representation of db schema

# always better create own User model
# User = get_user_model()

class User(AbstractUser):
    pass

    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    

class Agent(models.Model):

    # OneToOne - like foreignkey, but each user can have only one agent
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    userprofile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    # we dont need this if we inherit AbstractUser class
    # first_name = models.CharField(max_length=100) # str
    # last_name = models.CharField(max_length=100) # str

    def __str__(self):
        return self.user.username
    


# DB table with columns
class Lead(models.Model):

    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    # CASCADE - if agent deleted - delete this lead
    # SET_NULL - if agent deleted - set null; works only if this field
    #            allowed to set NULL vals
    # SET_DEFAULT - if agent deleted - set default value; works only if
    #               this field has 'default' argument

    # not a DB constraint
    # SOURCE_CHOICES = (
    #     # in DB; display val
    #     ('YD', 'YouTube'),
    #     ('Google', 'Google'),
    #     ('Newsletter', 'Newsletter'),
    # )

    first_name = models.CharField(max_length=100) # str
    last_name = models.CharField(max_length=100) # str
    age = models.IntegerField(default=0) # int

    # phoned = models.BooleanField(default=False) # bool
    # source = models.CharField(choices=SOURCE_CHOICES, max_length=100)

    # profile_pic = models.ImageField(blank=True, null=True)
    # # not will be uploaded to the DB, only ref
    # special_files = models.FileField(blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

def post_user_created_signal(sender, instance, created, **kwargs):
    print(instance, created)
    if created:
        UserProfile.objects.create(user=instance)

# Lead.objects - '.objects' - is a manager, thing, where a lot of methods
# a stored. Such methods helps with querieng data and performe actions on DB

# Lead.objects.create(first_name='...', last_name='...', age=42) - will create a new Lead in DB

# Lead.objects.all() - return all objects of Lead table
# Lead.objects.filter(age=42) - return objects that meets the constraints
# Lead.objects.filter(age__gt=18) - return objects that has 'age > 18'
# In all ex. above, methods will return a 'queryset', special thing that supports a lot of complex stuff
# <QuerySet []> - ex.

post_save.connect(post_user_created_signal, sender=User)
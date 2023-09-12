from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import User, UserProfile

# Create a receiver function with pre_save method and the sender is the User model
# So, once the user has been saved or updated, userprofile


@receiver(post_save, sender=User)
def post_save_create_profile_receiver(sender, instance, created, **kwargs):

    # If user is created, create the userprofile automatically
    if created:
        UserProfile.objects.create(user=instance)

    # Else:
    else:
        # If the user info is updated, update the userprofile with the new info
        try:
            profile = UserProfile.objects.get(user=instance)
            profile.save()
        # If the userprofile doesnot exist, create a new userprofile with all the user info
        except:
            UserProfile.objects.create(user=instance)


# Create a receiver function with pre_save method and the sender is the User model
# So, once the user has been saved or updated, userprofile
@receiver(pre_save, sender=User)
def pre_save_profile_receiver(sender, instance, **kwargs):
    pass

# We used the @receiver decorator instead of writing the below line
# Connect the receiver function with the sender
# post_save.connect(post_save_create_profile_receiver, sender=User)

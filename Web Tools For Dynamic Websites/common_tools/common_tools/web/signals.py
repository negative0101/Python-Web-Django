from django.db.models.signals import pre_save, post_save, pre_delete
from django.dispatch import receiver

from common_tools.web.models import Profile

'''
Signals are used for:
1.Creating profile model for User
2.Send emails after user register
    -Welcome email
    -Verification email
3. Setting `is_deleted` instead of actual delete'''


@receiver(pre_save,sender=Profile)
def profile_pre_created(instance,**kwargs):
    print(f'pre save: {instance}')

@receiver(post_save,sender=Profile)
def profile_post_created(instance,**kwargs):
    print(f'post save: {instance}')

@receiver(pre_delete,sender=Profile)
def profile_to_be_deleted(instance,**kwargs):
   instance.is_deleted = True


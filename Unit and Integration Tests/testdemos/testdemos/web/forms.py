from django.forms import ModelForm

from testdemos.web.models import Profile


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


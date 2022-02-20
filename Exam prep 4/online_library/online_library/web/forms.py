from django import forms

from online_library.web.models import Profile, Book


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"

        widgets = {
            "first_name": forms.TextInput(attrs={
                "type": "text", "name": "first_name", "maxlength": 30, "required": "", "id": "first_name",
                "placeholer": "First Name"
            }),
            "last_name": forms.TextInput(attrs={
                "type": "text", "name": "last_name", "maxlength": 30, "required": "", "id": "last-name",
                "placeholer": "Last Name"
            }),

            "image_url": forms.URLInput(attrs={
                "type": "url", "name": "image_url", "maxlength": 200, "required": "", "id": "image-url",
                "placeholer": "URL"
            })
        }


class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('__all__')

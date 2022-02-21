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


class DeleteProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    def save(self, commit=True):
        self.instance.delete()
        Book.objects.all().delete()
        return self.instance

    class Meta:
        model = Profile
        fields = '__all__'


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


class EditBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


class DeleteBookForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Book
        fields = '__all__'


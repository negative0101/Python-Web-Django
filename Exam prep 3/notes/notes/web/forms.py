from django import forms

from notes.web.models import Profile, Note


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"


class DeleteProfileForm(forms.ModelForm):

    def save(self, commit=True):
        self.instance.delete()
        notes = Note.objects.all()
        notes.delete()
        return self.instance

    class Meta:
        model = Profile
        fields = "__all__"


class CreateNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = "__all__"


class EditNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = "__all__"


class DeleteNoteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Note
        fields = "__all__"


class DetailsNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = "__all__"

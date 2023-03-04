from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from django.contrib.auth.models import User, Group

class CustomLoginForm(AuthenticationForm):
    type = forms.ChoiceField(choices=[('admin', 'Admin'), ('doctor', 'Doctor'), ('fdo', 'Front Desk'), ('deo', 'Data Entry')])

class AdminCreateUserForm(UserCreationForm):

    groups = forms.ModelChoiceField(queryset=Group.objects.all(), required=True)

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('firstname', 'lastname', 'groups')

    def save(self, commit=True):
        user = super().save(commit=False)
        group = self.cleaned_data['groups']

        if group:
            group.user_set.add(user)
        if commit:
            user.save()

        return user

from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from myblog.models import Profile

class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    firstName = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    lastName = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'firstName', 'lastName', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    firstName = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    lastName = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'firstName', 'lastName', 'email', 'password')

class PassChangeForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))
    new_password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))
    new_password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')

class ProfilePageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'profile_pic', 'website_url', 'facebook_url', 'instagram_url',
        'linkedin_url', 'github_url', 'twitter_url', 'pinterest_url')
        widgets = {
            'bio': forms.Textarea(attrs={'class':'form-control'}),
            #'profile_pic': forms.ImageField(attrs={'class':'form-control'}),
            'website_url': forms.TextInput(attrs={'class':'form-control'}),
            'facebook_url': forms.TextInput(attrs={'class':'form-control'}),
            'instagram_url': forms.TextInput(attrs={'class':'form-control'}),
            'linkedin_url': forms.TextInput(attrs={'class':'form-control'}),
            'github_url': forms.TextInput(attrs={'class':'form-control'}),
            'twitter_url': forms.TextInput(attrs={'class':'form-control'}),
            'pinterest_url': forms.TextInput(attrs={'class':'form-control'}),
        }
    
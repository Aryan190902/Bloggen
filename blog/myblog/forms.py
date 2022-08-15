from django import forms
from .models import Post, Categories, Comment

choice = Categories.objects.all().values_list('name', 'name')
choiceLst = []
choiceL = list(choice)
for item in range(len(choice)):
    choiceLst.append(choice[item][0])

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','category', 'header_image', 'body', 'snippet')
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            #'author': forms.TextInput(attrs={'class':'form-control', 'value':'', 'id':'Blogger', 'type':'hidden'}),
            #'author': forms.Select(attrs={'class':'form-control'}),
            'category': forms.Select(choices=choiceL, attrs={'class':'form-control', 'placeholder':"Lifestyle"}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
            'snippet': forms.Textarea(attrs={'class':'form-control'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','category', 'header_image', 'body', 'snippet')
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'category': forms.Select(choices=choiceL, attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
            'snippet': forms.Textarea(attrs={'class':'form-control'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','body')
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
        }
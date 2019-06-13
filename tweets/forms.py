from django.forms import ModelForm
from django import forms
from .models import Tweet


class TweetModelForm(ModelForm):
    content = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder': "Your message",
                                                                     "class": "form-control"}))

    class Meta:
        model = Tweet
        fields = [
            "content"
        ]

    # def clean(self, *args, **kwargs):
    #     content = self.cleaned_data.get("content")
    #     if content == "":
    #         raise forms.ValidationError("Conn't be blank")
    #     return content

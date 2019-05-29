from django import forms
from .models import Tweet


class TweetModelForm(forms.ModelForm):
    class Meat:
        model = Tweet
        fields = [
            "user",
            "content"
        ]

    # def clean(self, *args, **kwargs):
    #     content = self.cleaned_data.get("content")
    #     if content == "":
    #         raise forms.ValidationError("Conn't be blank")
    #     return content

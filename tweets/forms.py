from django.forms import ModelForm
from .models import Tweet


class TweetModelForm(ModelForm):
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

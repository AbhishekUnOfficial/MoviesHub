from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["name", "feedback"]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "capitalize my-2 mx-5 bg-transparent border rounded-md py-2 px-5"
                }
            ),
            "feedback": forms.Textarea(
                attrs={
                    "class": "bg-transparent min-w-max mx-2 outline-none border border-gray-400 placeholder-gray-400 rounded-md py-2 px-5"
                }
            ),
        }

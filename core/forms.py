from django.forms import Textarea, ModelForm
from .models import Comment, Movie


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = "__all__"


class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = "__all__"
        widgets = {
            "name": Textarea(
                attrs={"cols": 80, "rows": 20, "class": "p-2 bg-black"},
            ),
        }

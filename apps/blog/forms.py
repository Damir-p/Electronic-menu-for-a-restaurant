from django import forms
from apps.blog.models import Comment


class CommentForm(forms.ModelForm):
    content = forms.CharField(max_length=500, widget=forms.Textarea(attrs={
        "class": "form-control",
        "rows": 3,
        "placeholder": "Присоединяйтесь к обсуждению и оставляйте комментарии!"
    }))

    class Meta:
        model = Comment
        fields = ['content']

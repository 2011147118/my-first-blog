from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    #어떤 모델이 쓰이는지 쟝고에게 알려줌.
    class Meta:
        model = Post
        fields = ('title', 'text')
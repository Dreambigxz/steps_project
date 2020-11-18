from django.forms import ModelForm, TextInput, Textarea


from .models import Post, Comment

class PostForm(ModelForm):



    class Meta:
        model: Post
        fields = ('author', 'tittle', 'text')

        widget = {

            'tittle': TextInput(attrs={'class': 'textinputclass'}),
            'text': Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'})
        }


class CommentForm(ModelForm):

    class Meta():
        model= Comment
        fields= ('author', 'text')

        widget = {

            'author': TextInput(attrs={'class': 'textinputclass'}),
            'text': Textarea(attrs={'class': 'editable medium-editor-textarea'})
        }
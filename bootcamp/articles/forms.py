from django import forms

from bootcamp.articles.models import Article
from  DjangoUeditor.forms import UEditorField

class ArticleForm(forms.ModelForm):
    status = forms.CharField(widget=forms.HiddenInput())
    title = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=255)
    content = UEditorField('Content',
                           initial = forms.TextInput(attrs={'class': 'form-control'}),
                           height = 300,
                           width = 1000,
                           imagePath = "upload/article/images/",
                           filePath = 'upload/article/files/',
                           upload_settings = {"imageMaxSize": 1204000})
    tags = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=255, required=False,
        help_text='Use spaces to separate the tags, such as "java jsf primefaces"')  # noqa: E501

    class Meta:
        model = Article
        fields = ['title', 'content', 'tags', 'status']

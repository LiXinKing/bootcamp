from django import forms

from bootcamp.questions.models import Answer, Question
from  DjangoUeditor.forms import UEditorField
from  DjangoUeditor.widgets import UEditorWidget, AdminUEditorWidget

class QuestionForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=255)
    description = UEditorField('description',
                           initial = forms.TextInput(attrs={'class': 'form-control'}),
                           height = 400,
                           width = 1000,
                           imagePath = "upload/question/images/",
                           filePath = 'upload/question/files/',
                           upload_settings = {"imageMaxSize": 1204000})
    tags = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=255,
        required=False,
        help_text='Use spaces to separate the tags, such as "asp.net mvc5 javascript"')  # noqa: E501

    class Meta:
        model = Question
        fields = ['title', 'description', 'tags']


class AnswerForm(forms.ModelForm):
    question = forms.ModelChoiceField(widget=forms.HiddenInput(),
                                      queryset=Question.objects.all())

    # width=600, height=300, toolbars="full", imagePath="", filePath="", upload_settings={},
    # settings={},command=None,event_handler=None

    description = forms.CharField(label="description",
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '4'}),
        max_length=2000)

    """
    description = forms.CharField(label="description", widget=forms.Textarea(attrs = {"width":1000,
                                                        "height":100, 'class': 'form-control',})
                                  )
    """
    """
    description = UEditorField('ansDescription',
                          initial = forms.TextInput(attrs={'class': 'form-control'}),
                           height = 400,
                           width = 1000,
                           imagePath = "upload/answer/images/",
                           filePath = 'upload/answer/files/',
                           upload_settings = {"imageMaxSize": 1204000})
    """
    class Meta:
        model = Answer
        fields = ['question', 'description']

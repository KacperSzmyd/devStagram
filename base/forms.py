from django.forms import ModelForm, widgets
from django import forms
from .models import Project


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        exclude = ['id', 'vote_total', 'vote_ratio', 'created']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'input fs-4', 'placeholder': 'Enter title'}),
            'description': forms.Textarea(attrs={'class': 'input fs-4'}),
            'demo_link': forms.URLInput(attrs={'class': 'input fs-4'}),
            'source_link': forms.URLInput(attrs={'class': 'input fs-4'}),
            'tags': forms.CheckboxSelectMultiple(attrs={'class': 'input fs-4'}),
            'featured_image': forms.FileInput(attrs={'class': 'input fs-4'})
        }

    # def __init__(self, *args, **kwargs):
    #     super(ProjectForm, self).__init__(*args, **kwargs)
        # for name, field in self.fields.items():
        #     field.widged.attrs.update({'class': 'input'})

        # self.fields['title'].widget.attrs.update({'class': 'input', 'placeholder': 'Add title'})
        # self.fields['description'].widget.attrs.update({'class': 'input'})
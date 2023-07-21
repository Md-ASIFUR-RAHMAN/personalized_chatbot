from django import forms

class FaqForm(forms.Form):
    """
    Form for individual user links
    """
    question = forms.CharField(
                    max_length=100,
                    widget=forms.TextInput(attrs={
                        'placeholder': 'question',
                    }),
                    required=False)
    answer = forms.URLField(
                    widget=forms.TextInput(attrs={
                        'placeholder': 'answer',
                    }),
                    required=False)



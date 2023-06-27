from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Div

class ModifierForm(forms.Form):
    modifier = forms.IntegerField()
    modifier_display = forms.CharField(disabled=True, widget=forms.TextInput(attrs={'placeholder': 'Modificador'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-modifier-form'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Field('modifier', css_class='form-control-lg'),
            Field('modifier_display', css_class='form-control-lg'),
        )
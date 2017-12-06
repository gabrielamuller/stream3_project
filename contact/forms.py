from django import forms

class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    contact_number = forms.CharField(required=True,widget=forms.TextInput(attrs={'pattern':'[0-9]+', 'title':'Enter numbers only '}))

    content = forms.CharField(required=True, widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['contact_name'].label = "Name:"
        self.fields['contact_email'].label = "Email:"
        self.fields['contact_number'].label = "Phone Number:"
        self.fields['content'].label = "Comment:"
from django import forms
class StudentRegi(forms.Form):
    name=forms.CharField(widget=forms.PasswordInput)
    #name = forms.CharField(widget=forms.HiddenInput)
    #name = forms.CharField(widget=forms.Textarea)
    #name = forms.CharField(widget=forms.CheckboxInput)
    name = forms.CharField(widget=forms.FileInput)
   # email=forms.EmailField()
   # mobile=forms.IntegerField()
   #key=forms.CharField(widget=forms.HiddenInput) hideen fields

    # first_name=forms.CharField()
    # name = forms.CharField(initial="vipul", help_text="need 30  characters")
    #name = forms.CharField(initial="vipul", label_suffix=' ', label='Your name', required='False', disabled=True)
    #name = forms.CharField(initial="vipul")
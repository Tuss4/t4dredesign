from django import forms


class Contact(forms.Form):
	email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control'}))
	subject = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
	message = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))

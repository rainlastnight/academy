from django import forms
from .models import Join

class EmailForm(forms.Form):
	name = forms.CharField(required=False)
	email = forms.EmailField()
	ref_id = forms.CharField(widget=forms.HiddenInput())

class JoinForm(forms.ModelForm):
	class Meta:
		model = Join
		#when migrating add ref_id due to reflect class in models
		fields = ["email"]

		# fields = "__all__"
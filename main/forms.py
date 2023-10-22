from django import forms
from .models import City

class PostCity(forms.ModelForm):
	class Meta:
		model =City
		fields=('name','description','tier')

		widgets={
			'name':forms.TextInput(attrs={
				'type':"text",
				'class':'name_form',
				'placeholder':'Название города',
				'required':'true'
			}),
			'description':forms.Textarea(attrs={
				'type':"text",
				'class':'descr_form',
				'placeholder':'Описание',
				'required':'true'
			}),
			'tier':forms.Select(attrs={
				
				'class':'tier-form',
				'required':'true'
			}),
		}
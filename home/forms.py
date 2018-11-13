from django import forms
from .models import Slide

class slideForm(forms.ModelForm):
	class Meta:
		model = Slide
		fields = ['dataX', "dataY", "dataY", "dataZ", "dataRotateX", "dataRotateY", "dataRotateZ", "dataScale", "message"]
		widgets = {
			'dataX':forms.fields.NumberInput(attrs={
					'placeholder':'Data X Value'
				}),
			'dataY':forms.fields.NumberInput(attrs={
					'placeholder':'Data Y Value'
				}),
			'dataZ':forms.fields.NumberInput(attrs={
					'placeholder':'Data Z Value'
				}),
			'dataRotateX':forms.fields.NumberInput(attrs={
					'placeholder':'Data Rotate X Value'
				}),
			'dataRotateY':forms.fields.NumberInput(attrs={
					'placeholder':'Data Rotate Y Value'
				}),
			'dataRotateZ':forms.fields.NumberInput(attrs={
					'placeholder':'Data Rotate Z Value'
				}),
			'dataScale':forms.fields.NumberInput(attrs={
					'placeholder':'Data Scale Value'
				}),
			'message':forms.Textarea(attrs={
					'placeholder':'Message'
				}),
		}
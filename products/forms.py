from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = [
			'long_text',
			'short_text',
		]

	def __init__(self,*args,**kwargs):
		super(ProductForm, self).__init__(*args, **kwargs)

		self.fields['long_text'].widget = forms.TextInput(attrs={
		'id': 'long_text_id',
		'class': 'form-control',
		'placeholder': 'Your Long URL Here'})

		self.fields['short_text'].widget = forms.TextInput(attrs={
		'id': 'short_text_id',
		'class': 'form-control ',
		'placeholder': 'Custom Short URL'})
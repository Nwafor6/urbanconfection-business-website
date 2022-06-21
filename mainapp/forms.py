from django import forms
from .models import ProductVideo, Product



class ProductVideoForm(forms.ModelForm):
	
	class Meta:
		model=ProductVideo
		fields=['video_title', 'video']

class ProductForm(forms.ModelForm):
	title= forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder":"Enter title of the product"}))
	price= forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter integer product price default is # 0'}))
	def __init__(self, *args, **kwargs):
		super(ProductForm, self).__init__(*args, **kwargs)
		## remove label from each of the fields
		for f in self.fields.keys():
			self.fields[f].label=''
	class Meta:
		model=Product
		fields=['title', 'price', 'img', 'category']

class ContactForm(forms.Form):
	first_name=forms.CharField(max_length =50, widget=forms.TextInput(attrs={'placeholder':'Your firstname'}))
	last_name = forms.CharField(max_length = 50, widget=forms.TextInput(attrs={"placeholder":"Last name"}))
	email_address= forms.EmailField(max_length = 50 ,widget=forms.TextInput(attrs={'placeholder':'@example.com'}))
	message = forms.CharField(widget= forms.Textarea(attrs={"placeholder":"Message......."}), max_length = 2000)
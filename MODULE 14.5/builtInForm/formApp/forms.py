from django import forms
import datetime
class CreateBuilInForm(forms.Form):
    name = forms.CharField(label='Name',initial='type your name',required=False)
    email = forms.EmailField(required=False)
    birth_date = forms.DateField(widget=forms.NumberInput(attrs={'type': 'date'}), error_messages={
               'required': 'Not required.'
                })
    password = forms.CharField(widget = forms.PasswordInput())
    File = forms.ImageField()
    BIRTH_YEAR_CHOICES = ['1998', '1999', '2000','2001','2003']
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    day = forms.DateField(initial=lambda: datetime.date.today())
    value = forms.DecimalField()
    message = forms.CharField(
	max_length = 10,
    )
    roll_number = forms.IntegerField(  
                     help_text = "Enter 6 digit roll number",required=False
                     )  
    # FAVORITE_COLORS_CHOICES = [
    # ('blue', 'Blue'),
    # ('green', 'Green'),
    # ('black', 'Black'),
    # ]
    # favorite_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)
    FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
    ]
    favorite_color = forms.ChoiceField(widget=forms.RadioSelect, choices=FAVORITE_COLORS_CHOICES)
    favorite_colors = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=FAVORITE_COLORS_CHOICES, required=False)
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows':3,'placeholder':'Type your comment here, sir...'}),required=False)
    agree = forms.BooleanField(required=False,label='Agree?')

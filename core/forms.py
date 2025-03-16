from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

class CustomSignupForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm',
            'placeholder': 'Email Address'
        }),
        help_text='',  # Remove help text for the email field
    )
    privacy_policy = forms.BooleanField(
        required=True,
        label="I agree to the Privacy Policy",
        widget=forms.CheckboxInput(attrs={
            'class': 'form-checkbox h-5 w-5 text-indigo-600'
        }),
        help_text='',  # Remove help text for the privacy policy field
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'privacy_policy')

    def __init__(self, *args, **kwargs):
        super(CustomSignupForm, self).__init__(*args, **kwargs)
        
        # Remove help text for username field
        self.fields['username'].help_text = ''
        self.fields['username'].widget.attrs.update({
            'class': 'block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm',
            'placeholder': 'Username'
        })

        # Remove help text for password fields
        self.fields['password1'].help_text = ''
        self.fields['password1'].widget.attrs.update({
            'class': 'block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm',
            'placeholder': 'Password'
        })

        self.fields['password2'].help_text = ''
        self.fields['password2'].widget.attrs.update({
            'class': 'block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm',
            'placeholder': 'Confirm Password'
        })
        
# class AddContentForm(ModelForm):
#     class Meta:
#         model = Content
#         fields = ['course_title', 'description', 'course_video', 'course_image']  # Include any fields you want to allow users to update
#         widgets = {
#             'description': forms.Textarea(attrs={'rows': 3}),
#             'course_title': forms.Textarea(attrs={'rows': 1}),
            
#         }
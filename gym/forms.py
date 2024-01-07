from django import forms

class Sign_In(forms.Form):
    username=forms.CharField(max_length=50,label='Usuário',widget=forms.TextInput(attrs={'class':'form-control username','placeholder':'admin'}))
    password=forms.CharField(max_length=50,label='Senha',widget=forms.PasswordInput(attrs={'class':'form-control password','placeholder':'123'}))
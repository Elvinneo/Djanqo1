from django import forms




class registerForm(forms.Form):
    first_name=forms.CharField(max_length=30,label="Ad")
    last_name=forms.CharField(max_length=30,label="Soyad")
    email=forms.CharField(max_length=50,label="Elektron poçt")
    username=forms.CharField(max_length=30,label="İstifadəçi adı")
    password=forms.CharField(max_length=15,label="Şifrə",widget=forms.PasswordInput)
    confirm=forms.CharField(max_length=15,label="Təkar şifrə",widget=forms.PasswordInput)
      

    def clean(self):
        first_name=self.cleaned_data['first_name']
        last_name=self.cleaned_data['last_name']
        username=self.cleaned_data['username']
        email=self.cleaned_data['email']
        password=self.cleaned_data['password']
        confirm=self.cleaned_data['confirm']

        if  password and confirm and  password != confirm:
            raise forms.ValidationError("Şifrələr eyni deyil")
        elif not first_name:
            raise forms.ValidationError("Ad hissəsi boş ola bilməz")
        values = {
            'first_name':first_name,
            'last_name':last_name,
            'username':username,
            'email':email,
            'password':password
        }
        return values
    
class loginForm(forms.Form):
    username=forms.CharField(max_length=30,label="İstifadəçi adı")
    password=forms.CharField(max_length=15,label="Şifrə",widget=forms.PasswordInput)
        
     
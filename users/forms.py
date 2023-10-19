from allauth.account.forms import SignupForm
from django import forms


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name',required=True)
    last_name = forms.CharField(max_length=30, label='Last Name',required=True)
    campus_id = forms.IntegerField(min_value=1, max_value=21, label="Campus ID", required=True)
    course_id = forms.IntegerField(min_value=1, max_value=30, label="Course ID", required=True)
    year = forms.IntegerField(min_value=1, max_value=4, label="Year", required=True)

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.name = " ".join((user.first_name,user.last_name))
        user.campus_id = self.cleaned_data["campus_id"]
        user.course_id = self.cleaned_data["course_id"]
        user.year = self.cleaned_data["year"]
        user.save()
        print(self.cleaned_data)
        print(user.campus_id, user.course_id, user.year)
        print(user.first_name,user.last_name)
        return user

from django import forms

from .models import Author


class AuthorAdminForm(forms.ModelForm):
    def clean_name(self):
        value = self.cleaned_data.get("name", "")
        if value == "テスト":
            raise forms.ValidationError("テストと言う名前は使用できません")
        return value

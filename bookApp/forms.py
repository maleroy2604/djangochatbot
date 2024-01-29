from django import forms


class MyForm(forms.Form):
    book_name = forms.CharField(label="'Book's title", max_length=200)

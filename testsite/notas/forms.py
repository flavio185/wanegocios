from django import forms
from .models import Nota, UserQuery

class NotaForm(forms.ModelForm):

    class Meta:
        model = Nota
        fields = ['numero', 'data', 'descricao', 'valor', 'tipo_gasto', 'imagem', 'imagem1']
        #fields = ['numero', 'data', 'descricao', 'valor', 'tipo_gasto']

class UserQueryForm(forms.ModelForm):

    class Meta:
        model = UserQuery
        fields = ['user', 'query', 'alias']

#class NotaFilterForm(forms.Form):
#    data_inicio = forms.DateField()

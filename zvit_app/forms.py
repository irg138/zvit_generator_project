
from django import forms
from . import utils

class ZvitForm(forms.Form):
    num = forms.CharField(label="№Заявки", required=False)
    date = forms.CharField(label="Дата розгляду", required=False)
    date_rozp = forms.CharField(label="Дата розпорядження", required=False)
    object = forms.CharField(label="Об'єкт інспектування", required=True)
    sphere = forms.ChoiceField(label="СФЕРА", choices=[(k,k) for k in utils.SPHERES.keys()], required=False)
    zvit_members = forms.MultipleChoiceField(label="Група інспектування (Звіт)", choices=[(g,g) for g in utils.GROUPS_ZVIT], required=False, widget=forms.SelectMultiple(attrs={"size":6}))
    rozp_members = forms.MultipleChoiceField(label="Група інспектування (Розпорядження)", choices=[(g,g) for g in utils.GROUPS_ROZP], required=False, widget=forms.SelectMultiple(attrs={"size":6}))
    responsible = forms.ChoiceField(label="Відповідальний виконавець", choices=[(r,r) for r in utils.RESPONSIBLES], required=False)
    leader = forms.ChoiceField(label="Керівник групи", choices=[(l,l) for l in utils.LEADERS + utils.GROUPS_ROZP_OI], required=False)
    leader_oi = forms.ChoiceField(label="Керівник OІ", choices=[(l,l) for l in utils.GROUPS_ROZP_OI], required=False)

from django import forms
from pvp.models import Query


class QueryForm(forms.ModelForm):

    class Meta:
        model = Query
        fields = [
            'phenotypes', 'disease', 'inheritance_mode', 'vcf_file']

    def save(self):
        instance = super(QueryForm, self).save()
        return instance

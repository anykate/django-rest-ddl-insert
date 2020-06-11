from django import forms
from .models import Color

COLORS_LIST = (
    ('select', '-- SELECT COLOR --'),
    ('red', 'RED'),
    ('blue', 'BLUE'),
    ('green', 'GREEN'),
    ('purple', 'PURPLE'),
)


class ColorInsertForm(forms.ModelForm):
    class Meta:
        model = Color
        fields = '__all__'
        widgets = {
            'name': forms.Select(attrs={
                'class': 'custom-select',
            }, choices=COLORS_LIST)
        }

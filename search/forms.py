from django import forms

CATEGORIES = (('1', 'Students\' Union Clubs'),
                 ('2', 'Sports Clubs'),
                 ('3', 'Academic Clubs'),
                 ('4', 'Cultural Activities Clubs'),
                 ('5', 'Career Clubs'),
                 ('6', 'Investment & Finance Clubs'),
                 ('7', 'Technology-related Clubs'),
                 ('8', 'Skill-building Clubs'),
                 ('9', 'Others'),
                 ('10', 'My Clubs'),
)


class FilterForm(forms.Form):
    category = forms.CharField(max_length=2, widget=forms.Select(choices=CATEGORIES))

    
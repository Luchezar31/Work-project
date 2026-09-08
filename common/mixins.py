from django.contrib.auth.mixins import UserPassesTestMixin


class ReadOnlyMixin:
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields.values():
            field.disabled=True
            field.widget.attrs['readonly'] = True

class ProfileOwnerOnlyAccessMixin(UserPassesTestMixin):

    def test_func(self):

        return self.request.user.pk == self.get_object().user.pk

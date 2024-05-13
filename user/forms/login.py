from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _

class MyAuthForm(AuthenticationForm):
    error_messages = {
        'invalid_login': _(
            "Vinsamlega sláðu inn rétt notendanafn og lykilorð. "
            "Hafðu í huga að gerður er greinarmunur á milli há- og lágstafa"
        ),
        'inactive': _("Þessi notandi er óvirkur."),
    }


class MyLoginView(LoginView):
    authentication_form = MyAuthForm
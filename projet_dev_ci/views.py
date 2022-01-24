from django.views.generic import TemplateView


# Create your views here.
class HomePageView(TemplateView):
    """
    Class used to define the template used when loading the home page
    """
    template_name = "home.html"


class UserPageView(TemplateView):
    """
    Class used to define the template used when the user/student view is loaded
    """
    template_name = "user.html"


class AdminPageView(TemplateView):
    """
    Class used to define the template used when the admin/teacher view is loaded
    """
    template_name = "admin.html"

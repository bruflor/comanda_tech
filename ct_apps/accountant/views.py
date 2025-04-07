from django.http import HttpResponse
from django.views import View


# Create your views here.
class AccountantDashBoardView(View):
    def get(self, request):
        return HttpResponse("Accountatn")

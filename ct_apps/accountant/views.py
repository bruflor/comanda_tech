from django.shortcuts import render
from django.views import View


# Create your views here.
class AccountantDashBoardView(View):
    def get(self, request):
        return render(request, "accountant/index.html", context={})

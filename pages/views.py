from django.shortcuts import render
from django.views import View


class AboutView(View):
    def get(self, request):
        return render(request, 'pages/about.html')


class RulesView(View):
    def get(self, request):
        return render(request, 'pages/rules.html')


def custom_403(request, exception):
    return render(request, 'pages/403csrf.html', status=403)


def custom_404(request, exception):
    return render(request, 'pages/404.html', status=404)


def custom_500(request):
    return render(request, 'pages/500.html', status=500)

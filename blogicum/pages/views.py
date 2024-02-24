from django.shortcuts import render


def about(request):
    """Страница о проекте"""
    template = 'pages/about.html'
    return render(request, template)


def rules(request):
    """Страница наши правила"""
    template = 'pages/rules.html'
    return render(request, template)

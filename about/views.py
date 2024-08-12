from django.shortcuts import render

# website homepage
def index(request):
    return render(request, 'learning/base.html')

# about page
def about_home(request):
    return render(request, 'about/about.html')

# about the site
def site(request):
    return render(request, 'about/site.html')

# about the tcg
def tcg(request):
    return render(request, 'about/tcg.html')

# tcg quick-start guide
def quickstart(request):
    return render(request, 'about/quickstart.html')
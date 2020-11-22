from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages
from .models import *
from .forms import *


def callback(request):
    print(request.POST)
    print(request.POST.get('age') == '')
    if request.POST:
        if request.POST.get('age') == '' and request.POST.get('messages') == '' and request.POST.get('agree') != 'on':
            print('form is ok')
            req = request.POST
            form = CallbackForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Спасибо, форма успешно отправлена')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            print('bad form')
    else:
        form = CallbackForm()
    return render(request, 'pages/contacts.html', locals())


def index(request):
    allBanners = Banner.objects.filter(isActive=True).order_by('order')
    allClients = Client.objects.all().order_by('order')
    allReviews = Review.objects.filter(is_home=True)
    indexSevices = Service.objects.filter(isHomeVisible=True)
    allSevices = Service.objects.all()
    allProjects = Project.objects.all()
    latestPosts = BlogPost.objects.all()[:1]
    homeActive = 'active'
    form = CallbackForm()
    try:
        seotag = SeoTag.objects.first()
        indexText = seotag.indexText

        pageTitle = seotag.indexTitle
        pageDescription = seotag.indexDescription
        pageKeywords = seotag.indexKeywords
    except:
        pageTitle = 'НЕ ЗАПОЛНЕНА ТАБЛИЦА СЕО ТЕГИ'
        pageDescription = 'НЕ ЗАПОЛНЕНА ТАБЛИЦА СЕО ТЕГИ'
        pageKeywords = 'НЕ ЗАПОЛНЕНА ТАБЛИЦА СЕО ТЕГИ'
    return render(request, 'pages/index.html', locals())


def reviews(request):
    allReviews = Review.objects.all()
    return render(request, 'pages/reviews.html', locals())
def about(request):
    allSevices = Service.objects.filter(isHomeVisible=True)

    aboutActive = 'active'
    try:
        seotag = SeoTag.objects.first()
        text = seotag.aboutText
        pageTitle = seotag.aboutTitle
        pageDescription = seotag.aboutDescription
        pageKeywords = seotag.aboutKeywords
    except:
        pageTitle = 'НЕ ЗАПОЛНЕНА ТАБЛИЦА СЕО ТЕГИ'
        pageDescription = 'НЕ ЗАПОЛНЕНА ТАБЛИЦА СЕО ТЕГИ'
        pageKeywords = 'НЕ ЗАПОЛНЕНА ТАБЛИЦА СЕО ТЕГИ'
    return render(request, 'pages/about.html', locals())


def projects(request):
    try:
        seotag = SeoTag.objects.first()
        pageTitle = seotag.projectsTitle
        pageDescription = seotag.projectsDescription
        pageKeywords = seotag.projectsKeywords
    except:
        pageTitle = 'НЕ ЗАПОЛНЕНА ТАБЛИЦА СЕО ТЕГИ'
        pageDescription = 'НЕ ЗАПОЛНЕНА ТАБЛИЦА СЕО ТЕГИ'
        pageKeywords = 'НЕ ЗАПОЛНЕНА ТАБЛИЦА СЕО ТЕГИ'
    allSevices = Service.objects.all()
    allProjects = Project.objects.all()
    allReviews = Review.objects.all()
    allClients = Client.objects.all()
    projectsActive = 'active'
    return render(request, 'pages/projects.html', locals())


def project(request,slug):
    try:
        seotag = SeoTag.objects.first()
        pageTitle = seotag.projectsTitle
        pageDescription = seotag.projectsDescription
        pageKeywords = seotag.projectsKeywords
    except:
        pageTitle = 'НЕ ЗАПОЛНЕНА ТАБЛИЦА СЕО ТЕГИ'
        pageDescription = 'НЕ ЗАПОЛНЕНА ТАБЛИЦА СЕО ТЕГИ'
        pageKeywords = 'НЕ ЗАПОЛНЕНА ТАБЛИЦА СЕО ТЕГИ'
    curProject = get_object_or_404(Project, nameSlug=slug)
    allImg = ProjectImage.objects.filter(project=curProject)
    pageH1 = curProject.pageH1
    projectsActive = 'active'
    return render(request, 'pages/project.html', locals())

def services(request):
    try:
        seotag = SeoTag.objects.first()
        pageTitle = seotag.servicesTitle
        pageDescription = seotag.servicesDescription
        pageKeywords = seotag.servicesKeywords
    except:
        pageTitle = 'НЕ ЗАПОЛНЕНА ТАБЛИЦА СЕО ТЕГИ'
        pageDescription = 'НЕ ЗАПОЛНЕНА ТАБЛИЦА СЕО ТЕГИ'
        pageKeywords = 'НЕ ЗАПОЛНЕНА ТАБЛИЦА СЕО ТЕГИ'
    allSevices = Service.objects.all()
    servicesActive = 'active'
    allReviews = Review.objects.all()
    return render(request, 'pages/services.html', locals())


def contacts(request):
    allSevices = Service.objects.filter(isHomeVisible=True)
    contactsActive = 'active'
    allSevices = Service.objects.all()
    form = CallbackForm()
    try:
        seotag = SeoTag.objects.first()
        pageTitle = seotag.contactTitle
        pageDescription = seotag.contactDescription
        pageKeywords = seotag.contactKeywords
    except:
        pageTitle = 'НЕ ЗАПОЛНЕНА ТАБЛИЦА СЕО ТЕГИ'
        pageDescription = 'НЕ ЗАПОЛНЕНА ТАБЛИЦА СЕО ТЕГИ'
        pageKeywords = 'НЕ ЗАПОЛНЕНА ТАБЛИЦА СЕО ТЕГИ'
    return render(request, 'pages/contacts.html', locals())


def service(request, slug):
    form = CallbackForm()
    allSevices = Service.objects.all()
    allReviews = Review.objects.all()
    allClients = Client.objects.all()
    curService = get_object_or_404(Service, nameSlug=slug)
    servicesActive = 'active'
    pageH1 = curService.pageH1
    pageTitle = curService.pageTitle
    pageDescription = curService.pageDescription
    pageKeywords = curService.pageKeywords

    allImg = curService.review_img.all()
    return render(request, 'pages/service.html', locals())


def posts(request):
    blogActive = 'active'
    allSevices = Service.objects.all()
    allPosts = BlogPost.objects.filter(isActive=True)
    try:
        seotag = SeoTag.objects.first()
        pageTitle = seotag.blogTitle
        pageDescription = seotag.blogDescription
        pageKeywords = seotag.blogKeywords
    except:
        pageTitle = 'НЕ ЗАПОЛНЕНА ТАБЛИЦА СЕО ТЕГИ'
        pageDescription = 'НЕ ЗАПОЛНЕНА ТАБЛИЦА СЕО ТЕГИ'
        pageKeywords = 'НЕ ЗАПОЛНЕНА ТАБЛИЦА СЕО ТЕГИ'
    return render(request, 'pages/posts.html', locals())

def post(request,slug):
    post = get_object_or_404(BlogPost,nameSlug = slug)
    pageTitle = post.pageTitle
    pageDescription = post.pageDescription
    pageKeywords = post.pageKeywords
    post.views +=1
    post.save()
    return render(request, 'pages/post.html', locals())

def robots(request):
    robotsTxt = f"User-agent: *\nDisallow: /admin/\nHost: https://www.pto-msk.ru\nSitemap: https://www.pto-msk.ru/sitemap.xml"
    return HttpResponse(robotsTxt, content_type="text/plain")


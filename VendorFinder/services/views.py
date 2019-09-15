from django.shortcuts import render


# Create your views here.
def index(request):
    context = {}
    template_name = 'services/index.html'
    return render(request, template_name=template_name, context=context)


def cutomer_profile(request):
    context = {}
    template_name = 'services/customer-profile.html'
    return render(request, template_name=template_name, context=context)


def vendor_profile(request):
    context = {}
    template_name = 'services/vendor-profile.html'
    return render(request, template_name=template_name, context=context)


def vendor_customer_request_page(request):
    context = {}
    template_name = 'services/request-page.html'
    return render(request, template_name=template_name, context=context)


def vendor_filter_page(request):
    context = {}
    template_name = 'services/vendor-filter.html'
    return render(request, template_name=template_name, context=context)

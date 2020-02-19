from django.shortcuts import render
from django.views import generic
from case.models import CaseFile
from django.contrib.auth.decorators import login_required
from django.db.models import Q

#@login_required(login_url= 'Log in' )
def home(request):
    context = {
        'all_cases' : CaseFile.objects.all(),
        'total_cases_count' : CaseFile.objects.all().count(),
        'solved_cases_count' : CaseFile.objects.filter(status=1).count(),
        'pending_cases_count' : CaseFile.objects.filter(status=0).count()
    }
    return render(request, 'courtSys/index.html', context)

def solved(request):
    cases = CaseFile.objects.all()
    context = {
        'solved_cases': cases.filter(status=1),
        'solved_cases_count': cases.filter(status=1).count()
    }
    return render(request, 'courtSys/solved.html', context)

def pending(request):
    cases = CaseFile.objects.all()
    context = {
        'pending_cases': cases.filter(status=0),
        'pending_cases_count': cases.filter(status=0).count()
    }
    return render(request, 'courtSys/pending.html', context)

def case_detail(request, pk):
    case = CaseFile.objects.filter(pk=pk)[0]
    context = {
        'case' : case
    }
    return render(request, 'courtSys/case_detail.html', context)

def is_valid_queryparam(param):
    return param != '' and param is not None

def search_results(request):
     qs = CaseFile.objects.all()
     case_contains_query = request.GET.get('case_contains')

     if is_valid_queryparam(case_contains_query):
         qs = qs.filter(Q(accuser_name__icontains=case_contains_query) | Q(defendant_name__icontains=case_contains_query))

     elif case_contains_query == 'Search Case File...':
         messages.warning(request, 'Nothing Selected')

     context = {
         'search_query_rslt' : qs
     }
     return render(request, 'courtSys/search_results.html', context)          
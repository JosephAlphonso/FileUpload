from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Q
from .models import UserDetail
from datetime import date
import openpyxl
import re
regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

def index(request):
    if "GET" == request.method:
        return render(request, 'index.html', {})
    else:
        UserDetail.objects.all().delete()
        excel_file = request.FILES["excel_file"]
        wb = openpyxl.load_workbook(excel_file, data_only = True)
        worksheet = wb["Sheet1"]
        excel_data = list()
        worksheet = worksheet.iter_rows()
        worksheet_obj = next(worksheet)
        for row in worksheet:
            row_data = list()
            name = row[0].value
            email = row[1].value
            phone = row[2].value
            dob = row[3].value
            today = date.today()
            age = today.year - dob.date().year
            # import ipdb; ipdb.set_trace()
            if not (re.search(regex,email)):
                print(email)
            if not len(str(phone)) == 10:
                print(phone)
            if(re.search(regex,email)) and len(str(phone)) == 10:
                user_detail = UserDetail(name = name,
                        email = email,
                        phone = phone,
                        dob = dob,
                        age = age
                    )
                user_detail.save()
            else:
                pass

        return render(request, 'index.html', context={'status':'Uploaded Successfully'})


def view_data(request):
    # import ipdb; ipdb.set_trace()
    userdetail_data = UserDetail.objects.all()

    return render(request, 'table.html',context={"userdetail_data":userdetail_data})    

def search_function(request):
    # import ipdb; ipdb.set_trace()
    search_string = request.GET.get('search_data')
    userdetail_data = UserDetail.objects.filter(
        Q(name__icontains=search_string) |
        Q(email__icontains=search_string) |
        Q(phone__icontains=search_string) |
        Q(age__icontains=search_string)
        ).distinct().values()
    return JsonResponse({'userdetail_data': list(userdetail_data)})

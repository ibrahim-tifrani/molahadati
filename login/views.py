from django.shortcuts import render,redirect
from django.contrib import messages
from.models import Signin
from arabic_parent.models import chat_model
def log_in(request):
    return render(request,"arabic.html")
def page(request):
    return render(request,"arabic_notes.html")
def sent(request):
    return render(request,"teacher_arabic.html")
def sign(request):
    if request.method=="POST":
        context={}
        parent_name=request.POST["na"]
        request.session["parent_name"]=parent_name
        name1=request.POST["par"]
        request.session["name1"]=name1
        type_=request.POST["type"]
        email=request.POST["email"]
        number=request.POST["number"]
        check=request.POST.get("check")
        che=Signin.objects.filter(parent_child_name=parent_name,child_name=name1,typ=type_,gmail=email,phone=number).first()
        if name1 and parent_name and type_ and email and len(name1) > 5 and len(parent_name) > 5 and "@gmail.com" in email and len(number) == 10 and number[0:1]=="07" or "06" :
            if type_ == 'ولي' and not check and not che:
                sig=Signin(parent_child_name=parent_name,child_name=name1,typ=type_,gmail=email,phone=number)
                sig.save()
                messages.success(request, 'شكرا سيدي الولي على ملئ إستمارة التسجيل')
                chat=chat_model(name_of_parent_chat=parent_name,name_of_child=name1)
                chat.save()
                return redirect('notes')
            elif type_ == 'أستاذ' and not check and not che:
                sig=Signin(parent_child_name=parent_name,child_name=name1,typ=type_,gmail=email,phone=number)
                sig.save()
                messages.success(request, 'شكرا سيدي الأستاذ على ملئ إستمارة التسجيل')
                return redirect('choices')
            elif not check and che:
                messages.error(request,'هذالطالب الحساب مسجل به بالفعل')
                context['sign_same']='هذالطالب الحساب مسجل به بالفعل'
            elif check:
                if che:
                    if type_ == 'أستاذ':
                        return redirect('choices')
                    elif  type_ =='ولي':
                        return redirect('notes')
        else:
            messages.error(request, 'يرجى ملء جميع الحقول بشكل صحيح')
    return render(request,"arabic.html",context)
# Create your views here.

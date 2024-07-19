from django.shortcuts import render, redirect
from .models import note1, note2, note3, note4,notif

def sent(request):
    return render(request, "teacher_arabic.html")
def choices(request):
    if request.method=="POST":
        return redirect('sent')
    return render(request,"choices_teachers.html")

def teachers_notes(request):
    if request.method == "POST":
        name = request.POST.get("na1")
        year = request.POST.get("level")
        note = request.POST.get("note")
        
        if name and year and note:
            if year == "4متوسط":
                note_instance = note4.objects.filter(name4=name).first()
                if note_instance:
                    note_instance.notes4 = note
                    note_instance.save()
            elif year == "3متوسط":
                note_instance = note3.objects.filter(name3=name).first()
                if note_instance:
                    note_instance.notes3 = note
                    note_instance.save()
            elif year == "2متوسط":
                note_instance = note2.objects.filter(name2=name).first()
                if note_instance:
                    note_instance.notes2 = note
                    note_instance.save()
            elif year == "1متوسط":
                note_instance = note1.objects.filter(name1=name).first()
                if note_instance:
                    note_instance.notes1 = note
                    note_instance.save()
        
        return redirect('sent')
    
def reply(request):
    display={}
    rep=notif.objects.filter(name_of_teacher="notification").first()
    if rep:
        display['notification'] = rep.conversation.split('\n') 
    return render(request,"conversation.html",display)


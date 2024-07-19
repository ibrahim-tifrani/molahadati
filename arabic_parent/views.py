from django.shortcuts import render
from teacher_notes.models import note1, note2, note3, note4,notif
from datetime import datetime
from .models import chat_model
from login.views import sign
def page(request):
    context={}
    parent_name = request.session.get('parent_name')
    name1 = request.session.get('name')
    chat_save = chat_model.objects.filter(name_of_parent_chat=parent_name,name_of_child=name1).first()
    if chat_save:
        context['show']=chat_save.chats_words.split('\n')
    return render(request, "arabic_notes.html",context)
def show_note(request):
    context = {}
    
    if request.method == "POST":
        
        name = request.POST.get("name-surname")
        request.session['name']=name
        year = request.POST.get("year_of_study")

        if year == "4 متوسط":
            note_instance = note4.objects.filter(name4=name).first()
            if note_instance:
                context['note'] = note_instance.notes4
        elif year == "3 متوسط":
            note_instance = note3.objects.filter(name3=name).first()
            if note_instance:
                context['note'] = note_instance.notes3
        elif year == "2 متوسط":
            note_instance = note2.objects.filter(name2=name).first()
            if note_instance:
                context['note'] = note_instance.notes2
        elif year == "1 متوسط":
            note_instance = note1.objects.filter(name1=name).first()
            if note_instance:
                context['note'] = note_instance.notes1
        else:
            context['note']='لم تسجل لديه ملاحظات'

    return render(request, "arabic_notes.html", context)

def save_chat(request):
    if request.method=="POST":
        parent_name = request.session.get('parent_name')
        name1 = request.session.get('name1')
        chat=request.POST['chat_words']
        dt_string = datetime.now().strftime("%d/%m/%Y %H:%M")
        chat_text = f"{dt_string} {chat} {parent_name}\n"
        name1 = request.session.get('name1')
        chat_save = chat_model.objects.filter(name_of_parent_chat=parent_name,name_of_child=name1).first()
        if chat_save:
            # Initialize chats_words to an empty string if it is None
            if chat_save.chats_words is None:
                chat_save.chats_words = ""
            # Append the new chat text to the existing chats_words
            chat_save.chats_words += chat_text
            chat_save.save()
            if chat_text:
                display_in_teachers_platforme = f"لقد رد الولي {parent_name} على ملاحظات أستاذ ابنه {name1}  بهذا الرد: {chat} في هذا التاريخ: {dt_string}\n"
                rep=notif.objects.filter(name_of_teacher="notification").first()
                if rep:
                    rep.conversation +=display_in_teachers_platforme
                    rep.save()
    return render(request, "arabic_notes.html")
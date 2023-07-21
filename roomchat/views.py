from django.shortcuts import render,redirect,HttpResponse
from django.http import JsonResponse
from .models import *



def room(request,room):
    if 'VisitorStatus' not in request.session or request.session['VisitorStatus'] != "user":
        return redirect('Home:Login')

    username = request.GET.get('username')
    room_details = Room.objects.get(name = room)


    context = {
        'username' : username,
        'room' : room,
        'room_details' : room_details
    }

    return render(request , 'roomchat/room_chat.html',context)

def checkview(request):

    if 'VisitorStatus' not in request.session or request.session['VisitorStatus'] != "user":
        return redirect('Home:Login')

    if request.method == 'GET':
        return render(request, 'roomchat/room.html')

    if request.method == 'POST':

        try:
            room = request.POST['room_name']
            username = request.session['UserName']
            passw = request.POST['passw']


            if Room.objects.filter(name = room).exists() :

                room_obj = Room.objects.get(name = room)
                if room_obj.password == passw:

                    return redirect(room+'/?username='+username)
                else:
                    # context = {
                    #     'message' : 'Wrong Password'
                    # }
                    # return render(request, 'api/home.html',context)
                    return redirect('roomchat:checkview')




            else:
                new_room = Room.objects.create(name = room,password = passw)
                new_room.save()

                return redirect(room+'/?username='+username)
        except:
            return redirect('Home:Login')

def send(request):

    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value = message,user = username,room = room_id)
    new_message.save()

    return HttpResponse("SENT")


def getMessages(request,room):
    room_details = Room.objects.get(name = room)

    message = Message.objects.filter(room = room_details.id )
    return JsonResponse({"messages" : list(message.values())})



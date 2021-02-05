from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from .models import Rooms, generate_unique_code

# Create your views here.
def index(requests):
    if requests.user.is_anonymous:
        return redirect("/login")
    return render(requests, 'index.html')


def loginUser(requests):
    if requests.method == "POST":
        UserName = requests.POST['username']
        Password = requests.POST['pass']
        usr = authenticate(username=UserName, password=Password)
        if usr is not None:
            login(requests, usr)
            return redirect("/")
        else:
            return render(requests, 'login.html')
    return render(requests, 'login.html')


def signup(requests):
    if requests.method == "POST":
        fname = requests.POST['first_name']
        lname = requests.POST['last_name']
        lname = requests.POST['last_name']
        email = requests.POST['email']
        password = requests.POST['password']
        phone = requests.POST['phone']
        a = User.objects.create_user(fname, email, password)
        a.first_name = fname
        a.last_name = lname
        a.PhoneNumber = phone
        a.save()
        return redirect("/")
    return render(requests, 'signup.html')


def error(requests):
    return render(requests, 'error.html')


def join(requests):
    latest = [None, None, None, None, None, None, None, None, None, None, None, None]
    latest = Rooms.objects.all().filter(public=True)
    total_no_of_rooms = len(latest)
    context = {
        "latest1date" : latest[total_no_of_rooms -1].date,
        "latest1type" : latest[total_no_of_rooms -1].typeofmusic,
        "latest1size" : latest[total_no_of_rooms -1].size,
        "latest1canguestpause" : latest[total_no_of_rooms -1].guestcanpause,
        "latest1code" : latest[total_no_of_rooms -1].code,
        "latest2date" : latest[total_no_of_rooms -2].date,
        "latest2type" : latest[total_no_of_rooms -2].typeofmusic,
        "latest2size" : latest[total_no_of_rooms -2].size,
        "latest2canguestpause" : latest[total_no_of_rooms -2].guestcanpause,
        "latest2code" : latest[total_no_of_rooms -2].code,
        "latest3date" : latest[total_no_of_rooms -3].date,
        "latest3type" : latest[total_no_of_rooms -3].typeofmusic,
        "latest3size" : latest[total_no_of_rooms -3].size,
        "latest3canguestpause" : latest[total_no_of_rooms -3].guestcanpause,
        "latest3code" : latest[total_no_of_rooms -3].code,
        "latest4date" : latest[total_no_of_rooms -4].date,
        "latest4type" : latest[total_no_of_rooms -4].typeofmusic,
        "latest4size" : latest[total_no_of_rooms -4].size,
        "latest4canguestpause" : latest[total_no_of_rooms -4].guestcanpause,
        "latest4code" : latest[total_no_of_rooms -4].code,
        "latest5date" : latest[total_no_of_rooms -5].date,
        "latest5type" : latest[total_no_of_rooms -5].typeofmusic,
        "latest5size" : latest[total_no_of_rooms -5].size,
        "latest5canguestpause" : latest[total_no_of_rooms -5].guestcanpause,
        "latest5code" : latest[total_no_of_rooms -5].code,
        "latest6date" : latest[total_no_of_rooms -6].date,
        "latest6type" : latest[total_no_of_rooms -6].typeofmusic,
        "latest6size" : latest[total_no_of_rooms -6].size,
        "latest6canguestpause" : latest[total_no_of_rooms -6].guestcanpause,
        "latest6code" : latest[total_no_of_rooms -6].code,
        "latest7date" : latest[total_no_of_rooms -7].date,
        "latest7type" : latest[total_no_of_rooms -7].typeofmusic,
        "latest7size" : latest[total_no_of_rooms -7].size,
        "latest7canguestpause" : latest[total_no_of_rooms -7].guestcanpause,
        "latest7code" : latest[total_no_of_rooms -7].code,
        "latest8date" : latest[total_no_of_rooms -8].date,
        "latest8type" : latest[total_no_of_rooms -8].typeofmusic,
        "latest8size" : latest[total_no_of_rooms -8].size,
        "latest8canguestpause" : latest[total_no_of_rooms -8].guestcanpause,
        "latest8code" : latest[total_no_of_rooms -8].code,
        "latest9date" : latest[total_no_of_rooms -9].date,
        "latest9type" : latest[total_no_of_rooms -9].typeofmusic,
        "latest9size" : latest[total_no_of_rooms -9].size,
        "latest9canguestpause" : latest[total_no_of_rooms -9].guestcanpause,
        "latest9code" : latest[total_no_of_rooms -9].code,
        "latest10date" : latest[total_no_of_rooms -10].date,
        "latest10type" : latest[total_no_of_rooms -10].typeofmusic,
        "latest10size" : latest[total_no_of_rooms -10].size,
        "latest10canguestpause" : latest[total_no_of_rooms -10].guestcanpause,
        "latest10code" : latest[total_no_of_rooms -10].code,
        "latest11date" : latest[total_no_of_rooms -11].date,
        "latest11type" : latest[total_no_of_rooms -11].typeofmusic,
        "latest11size" : latest[total_no_of_rooms -11].size,
        "latest11canguestpause" : latest[total_no_of_rooms -11].guestcanpause,
        "latest11code" : latest[total_no_of_rooms -11].code,
        "latest0date" : latest[total_no_of_rooms -12].date,
        "latest0type" : latest[total_no_of_rooms -12].typeofmusic,
        "latest0size" : latest[total_no_of_rooms -12].size,
        "latest0canguestpause" : latest[total_no_of_rooms -12].guestcanpause,
        "latest0code" : latest[total_no_of_rooms -12].code,
    }
    return render(requests, 'join.html', context)


def create(requests):
    return render(requests, 'create.html')



def room(requests):
    if requests.method == 'POST':
        try:
            public = requests.POST.get('public')
            if public == None:
                public = False
            elif public == '':
                public = True
            type3 = requests.POST.get('type_')
            size = requests.POST.get('size')
            guestcanpause = requests.POST.get('guestcanpause')
            if guestcanpause == None:
                guestcanpause = False
            elif guestcanpause == '':
                guestcanpause = True
            description = requests.POST.get('description')
            code = generate_unique_code()
            context = {
                "public" : public,
                "type_" : type3,
                "size" : size,
                "guestcanpause" : guestcanpause,
                "description" : description,
                "code" : code,
            }
            from datetime import datetime
            RoomObj = Rooms(public=public, typeofmusic=type3, size=size, guestcanpause=guestcanpause, description=description, date=datetime.today(), code=code)
            RoomObj.save()
        except:
            code = requests.POST.get('qwery')
            try:
                latest = Rooms.objects.all().get(code=code)
                context = {
                    "public" : latest.public,
                    "type_" : latest.typeofmusic,
                    "size" : latest.size,
                    "guestcanpause" : latest.guestcanpause,
                    "description" : latest.description,
                    "code" : latest.code,
                }
            except:
                context = {
                    "public" : "Fail",
                    "type_" : "Fail",
                    "size" : "Fail",
                    "guestcanpause" : "Fail",
                    "description" : "Fail",
                    "code" : "Fail",
                }
                return redirect("/error")
    return render(requests, 'room.html', context)


def logoutUser(requests):
    logout(requests)
    return redirect(to="/login")

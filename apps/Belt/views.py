from django.shortcuts import render,redirect,HttpResponse
from .models import *
from django.contrib import messages
from django.contrib.messages import *
from django.db.models import Avg
from django.core.urlresolvers import reverse
import bcrypt


def index(request):
    if 'user_id' not in request.session:
        return render(request,"Belt/login.html")
    else:
        request.session['user_id']=request.session['user_id']
        # user_id=request.session['user_id']
        # print user_id
        messages.add_message(request, INFO ,"Signed in:",user_id)
    return redirect('/main')

def main(request):
    if 'user_id' not in request.session:
        return render(request,"Belt/travels.html")
    else:
        context = {
            "user":Users.objects.get(id=request.session['user_id']),
            # user_id: request.session['user_id'],
            }

    return render(request,"Belt/login.html", context)
def join(request,trip_id):
    context = {
        "user":Users.objects.get(id=request.session['user_id']),
        # "trip":Trips.objects.add()
        # Trips.objects.raw('INSERT INTO `Belt_trips_joined_trips`(`trips_id`,`users_id`) VALUES (3,1);')

        }

    join = Trips.objects.raw('INSERT INTO `Belt_trips_joined_trips`(`trips_id`,`users_id`) VALUES (trip_id,user_id);')
    messages.add_message(request, INFO ,"Success")
    return redirect('/travels')

def register(request):
    errors = Users.objects.validChecker(request.POST)
    if len(errors)==0:
        for u in Users.objects.all():
            if u.username == request.POST['username']:
                messages.add_message(request, INFO ,"username already taken, try logging in")

                return redirect('/main')
        user = Users.objects.create(name=request.POST["name"],username=request.POST["username"],password=bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()))
        request.session['user_id'] = user.id
        print request.session['user_id']
        # messages.add_message(request, INFO ,"success")
        return redirect('/travels')
    else:
        for i in errors:
            messages.add_message(request, INFO , errors[i])
        return redirect('/')
def login(request):
    user_list = Users.objects.all()
    for u in user_list:
        if u.username == request.POST['username'] and bcrypt.checkpw(request.POST['password'].encode(),u.password.encode()):
            request.session['user_id'] = u.id
            print request.session['user_id']
            return redirect('/travels')
    messages.add_message(request, INFO, "Invalid password or email, or both")
    request.session.clear()
    print "session cleared"
    return redirect('/main')

def travels(request):
    if 'user_id' not in request.session:
        messages.add_message(request, INFO ,"Please log in")
        return redirect('/register')
    if 'user_id' in request.session:
        context = {
        "user":Users.objects.get(id=request.session['user_id']),
        "user_list":Users.objects.all(),
        "your_trips":Trips.objects.filter(new_trip_id=request.session['user_id']),
        "other_trips":Trips.objects.exclude(new_trip_id=request.session['user_id']),
        # "travel_list":Trips.objects.order_by('-travel_date_to'),

        }

    return render(request,"Belt/travels.html", context)
#
# def join(request,trips_id):

def trip_review(request,trip_id):
    print request.session['user_id']
    print trip_id
    if 'user_id' not in request.session:
        messages.add_message(request, INFO ,"Please log in")
        return redirect('/register')
    if 'user_id' in request.session:
        context = {
        "trip":Trips.objects.get(id=trip_id),
        "user":Users.objects.get(id=request.session['user_id']),
        "your_trips":Trips.objects.filter(new_trip_id=request.session['user_id']),
        "other_trips":Trips.objects.exclude(new_trip_id=request.session['user_id']),
        }

        return render(request,"Belt/trip_review.html", context)

def add_travel(request):
    if 'user_id' not in request.session:
        messages.add_message(request, INFO ,"Please log in")
        return redirect('/register')
    if 'user_id' in request.session:
        context = {
        "user":Users.objects.get(id=request.session['user_id']),
        "user_list":Users.objects.all(),
        "your_trips":Trips.objects.filter(new_trip_id=request.session['user_id']),
            }
    if request.method=='POST':
        if len(request.POST['destination'])<4:
            messages.add_message(request, ERROR ,"Please enter destination >4 characters")
            return redirect('/travels/add_travel')
        if len(request.POST['description'])<4:
            messages.add_message(request, ERROR ,"Please enter description >4 characters")
            return redirect('/travels/add_travel')
        if request.POST['travel_date_to']<=request.POST['travel_date_from']:
            messages.add_message(request, ERROR ,"Sorry! Cannot travel back in time")
            return redirect('/travels/add_travel')

        else:
            trip = Trips.objects.create(destination=request.POST['destination'],travel_date_to=request.POST['travel_date_to'],travel_date_from=request.POST['travel_date_from'],new_trip_id=request.session['user_id'])
            messages.add_message(request, INFO ,"Success!")
    return render(request,"Belt/add_travel.html", context)


def clearsession(request):
    request.session.clear()
    messages.add_message(request, INFO ,"Logged out")
    return redirect('/')

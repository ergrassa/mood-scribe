from django.shortcuts import redirect, render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from scribe.emo import *
from scribe.entry import *
from scribe.history import *
import pandas as pd

def index(request):
    uid = '1'
    track = {}
    try: 
        uid = request.session['uid']
    except:
        uid = 'none'
    msg = {
        'top': f"",
        'topcolor': 'rgba(0.5,0.5,0.5,1)'
    }
    if request.method == "POST":
        for c in cols:
            track[c] = request.POST.get(c)
        # return HttpResponse("{0}".format(track))
        if None in track.values():
            msg['top'] = f"Please fill all the values"
            msg['topcolor'] = 'IndianRed'
            return render(request, "scribe/track.html", {'cols': cols, 'grades': grades, 'msg': msg, 'uid': uid})
        df = create_df(track)
        push_records(uid, df)
        request.session['track'] = track
        # return render(request, "scribe/entry.html", {'entry': track, 'plot': plot, 'hist': hist})
        return redirect('plot')
    else:
        return render(request, "scribe/index.html", {'cols': cols, 'grades': grades, 'msg': msg, 'uid': uid})
    
def plot(request):
    uid = request.session['uid']
    track = request.session['track']
    # ax = 'ax'
    hist = 'hist'
    ax = plot_entry(track)
    df = pull_records(uid)
    hist = plot_history(df)
    print('ret')
    return render(request, "scribe/entry.html", {'entry': track, 'plot': ax, 'hist': hist})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    print(user)
                    login(request, user)
                    request.session['uid'] = str(user)
                    print('auth')
                    HttpResponse('Authenticated successfully')
                    return redirect('index')
                else:
                    request.session['uname'] = 'none'
                    print('disabled')
                    return HttpResponse('Disabled account')
            else:
                request.session['uname'] = 'invalid'
                print('invalid')
                return HttpResponse('Invalid login')
    else:
        print('form')
        form = LoginForm()
    return render(request, 'scribe/login.html', {'form': form})

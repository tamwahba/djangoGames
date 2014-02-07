from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.utils import simplejson
from knights.models import UserProfile


def registeruser(request):
    if request.method == "POST":
        data = simplejson.loads(request.body.decode('utf-8'))
    else:
        data = request.REQUEST

    try:
        userName = data['user_name']
        email = data['email']
        password = data['password']

        try:
            User.objects.get(email=email)
            resp = HttpResponse(content='emailused')
        except User.DoesNotExist:
            newuser = User.objects.create_user(userName,
                                               email=email,
                                               password=password)
            newuser.save()
            UserProfile(user=newuser)
            resp = HttpResponse(content='registered')

    except KeyError:
        resp = HttpResponse(content='')
    return resp


def updateuser(request, user_name):
    if request.method == "POST":
        data = simplejson.loads(request.body.decode('utf-8'))
    else:
        data = request.REQUEST

    resp = HttpResponse(content='')

    username = user_name

    try:
        user = User.objects.get(username=userName)
        userP = UserProfile.objects.get(user=user)
    except User.DoesNotExist:
        return HttpResponse('user doesnt exist')

    if 'coins' in data:
        coins = data['coins']
        # To DO : auth token
        userP.coins = coins
        userP.save()
        resp += 'cons submitted')

    if 'friend' in data:
        friendName = data['friend']
        try:
            friend = User.objects.get(username=friendName)
            friendP = UserProfile.objects.get(user=friend)
            userP.friedns.add(friednP)
            userP.save()
            resp += 'friend added'
        except User.DoesNotExist:
            return HttpResponse(content='user not found')

    return resp


def loginuser(request):
#    print(request.user)
    if request.method == "POST":
        data = simplejson.loads(request.body.decode('utf-8'))
    else:
        data = request.REQUEST

    resp = HttpResponse(content='invalidlogin')
    try:
        username = data['user_name']
        password = data['password']
        user = authenticate(username=username, password=password)
        login(request, user)
        if user is not None:
            if user.is_active:
                resp = HttpResponse(content='login')
    except KeyError:
        resp = HttpResponse(content='')
    return resp


def returnspriteinfo(request, user_name):
    username = user_name

    try:
        user = User.objects.get(username=username)

        userP = UserProfile.objects.get(user=user)
    except UserNotFoundError:
        resp = HttpResponse(content='user not found')

    returnData = []

    for sprite in userP.sprites.all():
        spriteDict = {}

        spriteDict["spriteID"] = sprite.spriteID
        spriteDict["xx"] = sprite.xx
        spriteDict["yy"] = sprite.yy
        spriteDict["canInteract"] = sprite.canInteract

        returnData.append(spriteDict)

    return HttpResponse(simplejson.dumps(returnData))


def highscores(request):
    returnData = []

    for userP in UserProfile.objects.all():
        returnData.append({'playersName': str(userP),
                           'coins': str(userP.coins)})

    return HttpResponse(simplejson.dumps(returnData))


def friends(request, user_name):
    username = user_name

    try:
        user = User.objects.get(username=username)

        userP = UserProfile.objects.get(user=user)
    except UserNotFoundError:
        resp = HttpResponse(content='user not found')

    returnData = []
    for userP in UserProfile.friends.objects.all():
        returnData.append({'playersName': str(userP)})


from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile, Image, Likes, Comment
from .forms import SignupForm, ImageForm, ProfileForm, CommentForm
# from django.http import JsonResponse
# from annoying.decorators import ajax_request


# Create your views here.

@login_required(login_url='/accounts/login/')
def index(request):
    """
    Function that renders the home page
    """
    images = Image.objects.all().order_by('-posted_on')
    comments = Comment.objects.all()
    likes = Likes.objects.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            image_id = int(request.POST.get("idhey"))
            image = Image.objects.get(id = image_id)
            comment = form.save(commit=False)
            comment.user = request.user
            comment.image = image
            comment.save()
            return redirect("index")
    else:
        form = CommentForm()

    return render(request, 'index.html', {"images": images,"form":form})





@login_required(login_url='/accounts/login/')
def new_image(request):
    """
    Function that enables one to upload images
    """
    current_user = request.user
    profile =Profile.objects.get(user__id=current_user.id)
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            add=form.save(commit=False)
            add.profile = profile
            add.save()
            return redirect('index')
    else:
        form = ImageForm()
    return render (request, 'post.html', {"form": form})



@login_required(login_url='/accounts/login/')
def like(request, image_id):
    image = get_object_or_404(Image, pk=image_id)
    request.user.profile.like(image)
    return JsonResponse(image.count_likes, safe=False)


@login_required(login_url='/accounts/login/')
def unlike(request, image_id):
    image = get_object_or_404(Image, pk=post_id)
    request.user.profile.unlike(image)
    return JsonResponse(image.count_likes, safe=False)

@login_required(login_url='/accounts/login/')
def profile(request):
    """
    Function that enables one to see their profile
    """
    user = request.user

    profile = Profile.objects.get(user=user)

    posts = Image.objects.filter(user=user)

    title = f"{user.username}"
    return render(request, 'profile/profile.html', {"title": title, "user": user, "profile": profile, "posts":posts})


@login_required(login_url='/accounts/login/')
def user_profile(request,id):
    """
    Function that enables one to see their profile
    """
    user = User.objects.get(id = id)

    profile = Profile.objects.get(user=user)

    title = f"{user.username}"
    return render(request, 'profile/profile.html', {"title": title, "user": user, "profile": profile})

@login_required(login_url='/accounts/login/')
def update_profile(request,id):
    """
    Function that enables one to edit their profile information
    """
    current_user = request.user
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.save()
        return redirect('home')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'profile/update_profile.html', {"form": form })


def followers(request, username):
  user = user = User.objects.get(username = username)
  user_profile = Profile.objects.get(user=user)
  profiles = user_profile.followers.all

  title = "Followers"

  return render(request, 'follow_list.html', {"title": title, "profile":profile})



def following(request, username):
  user = user = User.objects.get(username = username)
  user_profile = Profile.objects.get(user=user)
  profiles = user_profile.following.all()

  title = "Following"

  return render(request, 'follow_list.html', {"title": title, "profile":profile})


@login_required(login_url='/accounts/login/')
def search_user(request):
    """
    Function that searches for profiles based on the usernames
    """
    if 'username' in request.GET and request.GET["username"]:
        name = request.GET.get("username")
        searched_profiles = User.objects.filter(username__icontains=name)
        message = f"{name}"
        profile = User.objects.all()
        print(profile)
        return render(request, 'search.html', {"message": message, "usernames": searched_profiles, "profile": profile, })

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html', {"message": message})


@login_required(login_url='/accounts/login/')
def add_comment(request, image_id):
    current_user=request.user
    image = Image.objects.get(id=image_id)
    profile_user = User.objects.get(username=current_user)
    comments = Comment.objects.all()
    print(comments)
    if request.method == 'POST':
        form = CommentsForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.image = images
            comment.save()
    else:
        form = CommentForm()
    return redirect('index')


# def like(request, image_id):
#    current_user = request.user
#    liked_post = Image.objects.get(id=image_id)
#    new_like, created = Likes.objects.get_or_create(
#        user_like=current_user, liked_post=liked_post)
#    new_like.save()

#    return redirect('home')

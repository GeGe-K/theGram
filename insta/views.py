from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile, Image, Likes, Comment
from .forms import SignupForm, ImageForm, ProfileForm
# from django.http import JsonResponse
# from annoying.decorators import ajax_request


# Create your views here.

@login_required(login_url='/accounts/login/')
def index(request):
    """
    Function that renders the home page
    """
    images = Image.get_images().order_by('-posted_on')
    comments = Comments.objects.all()
    likes = Likes.objects.all()

    return render(request, 'index.html', {"images": images})


@login_required(login_url='/accounts/login/')
def new_image(request):
    """
    Function that enables one to upload images
    """
    current_user = request.user
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            add=form.save(commit=False)
            add.profile = current_user
            add.save()
            return redirect('home')
    else:
        form = ImageForm()
    return render (request, 'post.html', {"form": form})



def like(request,image_id):
    current_user = request.user
    liked_image = Image.objects.get(id=image_id)
    new_like, created = Likes.objects.get_or_create(
        who_liked=current_user, liked_image=liked_image)
    new_like.save()

    return redirect('home')


@login_required(login_url='/accounts/login/')
def profile(request, username):
    """
    Function that enables one to see their profile
    """
  user = User.objects.get(username=username)
  if not user:
    return redirect('Home')
  profile = Profile.objects.get(user=user)

  title = f"{user.username}"
  return render(request, 'profile/profile.html', {"title": title, "user": user, "profile": profile})


@login_required(login_url='/accounts/login/')
def update_profile(request,username):
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
        form = ProfileForm()
    return render(request, 'profile/update_profile.html', {"form": form, })


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
        return render(request, 'search.html', {"message": message, "usernames": searched_profiles, "profiles": profiles, })

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
    return redirect('home')


def like(request, image_id):
   current_user = request.user
   liked_post = Image.objects.get(id=image_id)
   new_like, created = Likes.objects.get_or_create(
       user_like=current_user, liked_post=liked_post)
   new_like.save()

   return redirect('home')

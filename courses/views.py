from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Course, Lesson
from accounts.models import User
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    current_user = request.user
    #used only for optimization
    courses = Course.objects.filter(user = current_user).only("slug", "title","difficulty", "category", "img", )
    popular_courses = Course.objects.all().order_by('participants').reverse().only("slug", "title","difficulty", "category", "img")

    context = {"courses":courses, "popular_courses":popular_courses}
    return render(request, "courses/index.html", context)

@login_required
def course_view(request, slug):
    course = Course.objects.get(slug = slug)

    current_user = request.user

    isEnrolled = course in current_user.courses.all()
    context = {"isEnrolled":isEnrolled, "course":course}

    return render(request, "courses/course.html", context)

@login_required
def course_enroll(request, ID):
    course = Course.objects.get(id = ID)
    current_user = request.user

    current_user.courses.add(course)

    isEnrolled = course in current_user.courses.all()

    course.participants +=1
    course.save()

    context = {"isEnrolled":isEnrolled, "course":course}
    return HttpResponseRedirect(reverse("courses:course_view", kwargs={"slug":course.slug}))

@login_required
def course_lessons(request, ID):
    course = Course.objects.get(id = ID)
    lessons = course.course.all().order_by("order") # getting lessons of particular course.
    context = {"lessons": lessons, "course":course}
    return render(request, "courses/course-lessons.html", context)

@login_required
def lesson_view(request, ID):
    lesson = Lesson.objects.get(id = ID)
    course = Course.objects.get(id = lesson.course.id)

    is_video = lesson.__nonzero__() # checks if there is a video.

    lessons = course.course.all().order_by("order") # getting lessons of particular course.
    context = {"lessons":lessons, "lesson":lesson, "is_video":is_video}
    return render(request, "courses/lesson.html", context)

@login_required
def profile_view(request, ID):
    user = User.objects.get(id = ID)
    total_courses = user.courses.count
    context = {"user":user, "total_courses":total_courses}
    return render(request, "courses/profile.html", context)

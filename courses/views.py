from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Course, Lesson
from accounts.models import User

def index(request):
    current_user = request.user
    #used only for optimization
    courses = Course.objects.filter(user = current_user).only("slug", "title","difficulty", "category", "img", )
    popular_courses = Course.objects.all().order_by('participants').reverse().only("slug", "title","difficulty", "category", "img")

    context = {"courses":courses, "popular_courses":popular_courses}
    return render(request, "courses/index.html", context)

def course_view(request, slug):
    course = Course.objects.get(slug = slug)

    current_user = request.user

    isEnrolled = course in current_user.courses.all()
    context = {"isEnrolled":isEnrolled, "course":course}

    return render(request, "courses/course.html", context)

def course_enroll(request, ID):
    course = Course.objects.get(id = ID)
    current_user = request.user

    current_user.courses.add(course)

    isEnrolled = course in current_user.courses.all()

    context = {"isEnrolled":isEnrolled, "course":course}
    return HttpResponseRedirect(reverse("courses:course_view", kwargs={"slug":course.slug}))

def course_lessons(request, ID):
    course = Course.objects.get(id = ID)
    lessons = course.course.all().order_by("order") # getting lessons of particular course.
    context = {"lessons": lessons}
    return render(request, "courses/course-lessons.html", context)

def text_lesson_view(request, ID):
    lesson = Lesson.objects.get(id = ID)
    course = Course.objects.get(id = lesson.course.id)
    lessons = course.course.all().order_by("order") # getting lessons of particular course.
    context = {"lessons":lessons, "lesson":lesson}
    return render(request, "courses/text-lesson.html", context)

def video_lesson_view(request, ID):
    context = {}
    return render(request, "courses/video-lesson.html", context)
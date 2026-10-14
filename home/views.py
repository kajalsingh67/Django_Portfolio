from django.shortcuts import render, redirect
from .models import Feedback


def home(request):
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        rating = request.POST.get("rating")
        message = request.POST.get("message", "").strip()

        if name and rating and message and rating in ["1", "2", "3", "4", "5"]:
            Feedback.objects.create(
                name=name,
                rating=int(rating),
                message=message
            )

        return redirect("/")

    feedbacks = Feedback.objects.order_by("-created_at")

    return render(request, "home.html", {
        "feedbacks": feedbacks
    })
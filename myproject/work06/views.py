from django.shortcuts import render
from .forms import ReiwaForm

def index(request):
    return render(request, "work06/index.html")

def reiwa_view(request):
    result = None  # 初期値
    if request.method == "POST":
        form = ReiwaForm(request.POST)
        if form.is_valid():
            reiwa_year = form.cleaned_data["reiwa_year"]
            seireki = reiwa_year + 2018
            result = f"令和{reiwa_year}年は西暦{seireki}年です。"
    else:
        form = ReiwaForm()  # GET時は空のフォームを表示

    return render(request, "work06/reiwa.html", {
        "form": form,
        "result": result,
    })

from django.shortcuts import render
from rag import ask_question

def home(request):
    answer = None
    question = None
    sources = []

    if request.method == "POST":
        question = request.POST.get("question")

        if question:
            answer, sources = ask_question(question)

    return render(
        request,
        "assistant/home.html",
        {
            "question": question,
            "answer": answer,
            "sources": sources
        }
    )
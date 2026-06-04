import os

from django.shortcuts import render
from django.conf import settings

from rag import ask_question


def home(request):
    answer = None
    sources = []
    question = None
    uploaded_file_name = None

    # 用户点击 Ask AI 后
    if request.method == "POST":

        # 取得用户问题
        question = request.POST.get("question")

        # 取得上传文件
        uploaded_file = request.FILES.get("document")

        # 如果用户上传了文件
        if uploaded_file:

            # uploads 文件夹路径
            upload_dir = os.path.join(settings.BASE_DIR, "uploads")

            # 如果 uploads 不存在，就自动创建
            os.makedirs(upload_dir, exist_ok=True)

            # 保存路径
            file_path = os.path.join(upload_dir, uploaded_file.name)

            # 保存文件
            with open(file_path, "wb+") as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)

            uploaded_file_name = uploaded_file.name

        # 如果用户输入了问题，就先返回测试回答
        if question:
            answer, sources = ask_question(question, "uploads")
            # 去重来源列表
            unique_sources = []
            for source in sources:
                if source not in unique_sources:
                    unique_sources.append(source)

    return render(
        request,
        "assistant/home.html",
        {
            "question": question,
            "answer": answer,
            "sources": unique_sources,
            "uploaded_file_name": uploaded_file_name
        }
    )
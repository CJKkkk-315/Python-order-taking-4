from django.shortcuts import render
from .chatbot import generate_response  # 从你的问答机器人代码中导入生成回答的函数
from django.http import JsonResponse
def index(request):
    if request.method == 'POST':
        input_text = request.POST['input_text']
        output_text = generate_response(input_text)  # 调用你的问答机器人函数生成回答
        return JsonResponse({'output_text': output_text})
    return render(request, 'index.html')
# Create your views here.

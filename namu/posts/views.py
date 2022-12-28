from django.shortcuts import render

# Create your views here.

def getdatatest(request):
    num1 = request.GET.get('var1')
    num2 = request.GET.get('var2')
    print(int(num1) + int(num2))

    get_context = { 'get_key' : int(num1) + int(num2) }

    # getdatatest = "GET 테스트 화면 출력 성공"
    return render(request, 'senddatapage.html', get_context)

def postdatatest(request):
    num1 = request.POST.get('var1')
    num2 = request.POST.get('var2')
    print(int(num1) + int(num2))

    post_context = { 'post_key' : int(num1) + int(num2) }

    # postdatatest = "POST 테스트 화면 출력 성공"
    return render(request, 'senddatapage.html', post_context)

def senddatapage(request):
    # num1 = request.GET.get('var1')
    # num2 = request.GET.get('var2')
    # print(int(num1) + int(num2))
    return render(request, 'senddatapage.html')
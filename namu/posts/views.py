from django.shortcuts import render, redirect
from posts.forms import PostForm

# Create your views here.

# def getdatatest(request):
#     num1 = request.GET.get('var1')
#     num2 = request.GET.get('var2')
#     print(int(num1) + int(num2))

#     get_context = { 'get_key' : int(num1) + int(num2) }

#     # getdatatest = "GET 테스트 화면 출력 성공"
#     return render(request, 'senddatapage.html', get_context)

# def postdatatest(request):
#     num1 = request.POST.get('var1')
#     num2 = request.POST.get('var2')
#     print(int(num1) + int(num2))

#     post_context = { 'post_key' : int(num1) + int(num2) }

#     # postdatatest = "POST 테스트 화면 출력 성공"
#     return render(request, 'senddatapage.html', post_context)

# def senddatapage(request):
#     num1 = request.GET.get('var1')
#     num2 = request.GET.get('var2')
#     print(int(num1) + int(num2))
#     return render(request, 'senddatapage.html')

def create(request):
    if request.method == 'GET':
        postForm = PostForm()
        context = {'postForm' : postForm}
        return render(request, 'board/create.html', context)
    elif request.method == 'POST':
        postForm = PostForm(request.POST)

        if postForm.is_valid():
            post = postForm.save(commit=False)
            post.save()            
        return redirect('/board/read/' + str(post.id))

def list(requst):
    posts = Post.objects.all().order_by('-id')
    context = {'posts' : posts}
    return render(requst, 'board/list.html', context)

def read(requst, bid):
    posts = Post.objects.get(id=bid)
    context = {'post' : post}
    return render(requst, 'board/list.html', context)

def delete(requst, bid):
    posts = Post.objects.get(id=bid)
    post.delete()
    return redirect('/board/list')

def update(requst, bid):
    posts = Post.objects.get(id=bid)
    if requst.method=="GET":
        postForm = PostForm(instance=post)
        context = {'postForm' : postForm}
        # create html 부분 수정해야함
        return render(requst, 'board/create.html', context)

    elif requst.method=="POST":
        postForm = PostForm(requst.POST, instance=post)
        if postForm.is_valid():
            post = postForm.save(commit=False)
            post.save()
        return redirect('/board/list')

# def edit(request, id):
#     if request.method == 'GET':
#         postForm = PostForm()
#         context = {'postForm' : postForm}
#         return render(request, 'board/read.html', context)

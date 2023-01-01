from django.shortcuts import render, redirect
from posts.forms import PostForm
from posts.models import Post

# Create your views here.
def create(request):
    # 데이터 입력 페이지
    if request.method == 'GET':
        postForm = PostForm()
        context = {'postForm' : postForm}

        return render(request, 'board/create.html', context)

    # 실제 데이터를 저장
    elif request.method == 'POST':
        postForm = PostForm(request.POST)

        # 빠진 값이 있는지 체크
        if postForm.is_valid():

            # 데이터 저장 하기전에 체크
            post = postForm.save(commit=False)
                # if로 데이터 저장 확인 추가 헐 곳
            # 최종 데이터 저장
            post.save()
        return redirect('/posts/read/' + str(post.id))

def list(request):
    # ORM으로 데이터 다 가져와서 id 역순으로 정렬
    posts = Post.objects.all().order_by('-id')
    context = {'posts' : posts}
    return render(request, 'board/list.html', context)

def read(request, bid):
    # bid로 게시글 번호 하나만 불러오기
    post = Post.objects.get(id=bid)
    context = {'post' : post}
    return render(request, 'board/read.html', context)

def delete(request, bid):
    # 게시글 하나 삭제 후 list로 이동
    post = Post.objects.get(id=bid)
    post.delete()
    return redirect('/posts/list')

def update(request, bid):
    post = Post.objects.get(id=bid)
    if request.method=="GET":
        # 기존 양식 불러오기(instance)
        postForm = PostForm(instance=post)
        context = {'postForm' : postForm}
        return render(request, 'board/update.html', context)

    elif request.method=="POST":
        # 수정된 내용 덮어씌우기(request -> instance)
        postForm = PostForm(request.POST, instance=post)
        # 값이 유효한지 체크
        if postForm.is_valid():
            post = postForm.save(commit=False)
            post.save()
        return redirect('/posts/read/' + str(post.id))

# def edit(request, id):
#     if request.method == 'GET':
#         postForm = PostForm()
#         context = {'postForm' : postForm}
#         return render(request, 'board/read.html', context)

from django.shortcuts import render # type: ignore

def hello_view(request):
    menu_items = [
        {"name": "Home", "url": "index", "active": True},
        {"name": "About", "url": "about", "active": False},
        {"name": "Classes", "url": "classes", "active": False},
        {"name": "Blog", "url": "blog", "active": False},
    ]
    return render(request, 'hello.html', {'menu_items': menu_items})

def copy_blog_fun(request):
    copy_blog = [
        {"img": "static/images/b1.jpg", "age": 17, "name": "Fed", "profi": "Boxer Joniya Daro", "active": True},
        {"img": "static/images/b2.jpg", "age": 27, "name": "Jun", "profi": "Boxer Joniya Daro", "active": True},
    ]
    return render(request, "hello.html", {"copy_blog": copy_blog})


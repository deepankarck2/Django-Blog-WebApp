from django.shortcuts import render
#from django.http import HttpResponse no longer needed

posts = [
    {
        'author': 'Deep',
        'title': 'Blog Post-1',
        'content': 'First Post Content',
        'date_posted': 'October 16th, 2022'
    },
    {
        'author': 'Latif',
        'title': 'Blog Post-2',
        'content': 'Second Post Content',
        'date_posted': 'October 17th, 2022'
    }
]

#This is how we want to handle when an uses goes to the home page.
def home(request):  #takes a request argument, http response that we landed on the mohe page
    context = {
        'post_data': posts
    }

   #return HttpResponse('<h1>Blog Home</h1>') #returns http element when called in the url file
    return render(request, 'blog/home.html', context) #passing the context dict, key will be accessible in template

def about(request):
    #return HttpResponse('<h1 style="color: red;">Blog About</h1>')
    return render(request, 'blog/about.html', {'title': 'About'}) #subdirectory inside template directory

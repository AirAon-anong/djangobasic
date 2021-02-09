from django.shortcuts import render
from django.http import HttpResponse,Http404,JsonResponse
from .models import Tweet

# Create your views here.
def home_view(request,*args,**kwargs):
    #print(args,kwargs)
    return HttpResponse("<h1>Hello World</h1>")

def tweet_detail_view1(request,tweet_id,*args,**kwargs):
    #print(args,kwargs)
    try:
        obj = Tweet.objects.get(id=tweet_id)
    except:
        raise Http404
    return HttpResponse(f"<h1>Hello {tweet_id} - {obj.content}</h1>")

def tweet_detail_view2(request,tweet_id,*args,**kwargs):
    #print(args,kwargs)
    """
    REST API VIEW
    Consume by JavaScript or Swift/Java/iOS/Andriod
    return json data
    """
    data = {
        "id": tweet_id,
    }
    status = 200
    try:
        obj = Tweet.objects.get(id=tweet_id)
        if tweet_id >1:
            data['content']= obj.content
        else:
            data['thatData']= obj.content
    except:
        #raise Http404
        data['message']= "Not Found"
        status = 404
        
    return JsonResponse(data,status=status)

def tweet_list_view(request):
    qs = Tweet.objects.all()
    tweet_list =[{"id": x.id,"content":x.content} for x in qs]
    data ={
        "response": tweet_list
    }
    return JsonResponse(data)

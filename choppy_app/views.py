from django.http       import JsonResponse
from django.views      import View
from .models           import SupportCompany,Album

class SupportCompanyListView(View):
    def get(self,request):
        support_companys = list(SupportCompany.objects.all().values('id','name','images_url'))
        return JsonResponse({"support_companys":support_companys},status=200)
    
class AlbumListView(View):
    def get(self,request):
        albums = list(Album.objects.all().values('id','name','singer','images_url','link_url'))
        return JsonResponse({"albums":albums},status=200)
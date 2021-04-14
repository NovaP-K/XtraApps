from .Channels import ZeeNews , NDTV , IndiaToday , TimesofIndia
from django.http import HttpResponse

if __name__ == "__main__":
    NDTV.NDTV()
    IndiaToday.IndiaToday()
    ZeeNews.ZeeNews()

def main(request):
    NDTV.NDTV()
    IndiaToday.IndiaToday()
    ZeeNews.ZeeNews()
    TimesofIndia.TOI()

    return HttpResponse(200)

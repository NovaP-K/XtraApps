from django.contrib import admin
from .models import NewsArticle
from .models import SportsNewsArticle
from .models import TechNewsArticle
from .models import ScienceNewsArticle
from .models import HealthNewsArticle
from .models import BusinessNewsArticle 
from .models import EntertainmentNewsArticle
# Register your models here.

admin.site.register(NewsArticle)
admin.site.register(SportsNewsArticle)
admin.site.register(TechNewsArticle)
admin.site.register(ScienceNewsArticle)
admin.site.register(HealthNewsArticle)
admin.site.register(BusinessNewsArticle)
admin.site.register(EntertainmentNewsArticle)
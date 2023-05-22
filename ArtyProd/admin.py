from django.contrib import admin
from .models import Personnel
from .models import Service
from .models import Projet
from .models import Equipe
from .models import Détail
from .models import Contact
from .models import Images_Projet
from .models import Temoignage
from .models import Contact_Information

# Register your models here.
admin.site.register(Personnel)
admin.site.register(Service)
admin.site.register(Projet)
admin.site.register(Equipe)
admin.site.register(Détail)
admin.site.register(Contact)
admin.site.register(Images_Projet)
admin.site.register(Temoignage)
admin.site.register(Contact_Information)
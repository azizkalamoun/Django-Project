from django.contrib.auth.models import User
from django.db import models
import datetime

class Personnel(models.Model):
    fonction = models.CharField(max_length=30,default='')
    nom = models.CharField(max_length=20)
    description = models.CharField(max_length=100,default='No description provided')
    fichier_CV = models.FileField(upload_to='pdf_files/',null=True)
    fichier_photo = models.ImageField(blank=True)
    lien_linkedln = models.CharField(max_length=100,default='https://www.linkedin.com/')
    lien_twitter = models.CharField(max_length=100,default='https://twitter.com/')
    lien_facebook = models.CharField(max_length=100,default='https://www.facebook.com/')
    lien_github = models.CharField(max_length=100,default='https://github.com/')

    def __str__(self):
        return f"{self.nom}, {self.fichier_CV.name}, {self.fichier_photo.name}, {self.lien_linkedln}"

class Contact_Information(models.Model):
    location = models.CharField(max_length=100)
    number = models.CharField(max_length=20)
    email = models.EmailField()
    lien_linkedln = models.CharField(max_length=100,default='https://www.linkedin.com/')
    lien_twitter = models.CharField(max_length=100,default='https://twitter.com/')
    lien_facebook = models.CharField(max_length=100,default='https://www.facebook.com/')
    intagram = models.CharField(max_length=100,default='https://www.facebook.com/')
    def __str__(self):
        return self.location

class Service(models.Model):
    SERVICE_CHOICES = (
        ('graphic_design', 'Graphic Design'),
        ('audiovisual_production', 'Audiovisual Production'),
        ('three_d_conception', '3D Conception'),
    )

    icon=models.CharField(null=True,max_length=50)
    name = models.CharField(null=True,max_length=100)
    description = models.TextField()
    service_type = models.CharField(null=True,max_length=50, choices=SERVICE_CHOICES)

    def __str__(self):
        return self.name if self.name else ""

class Projet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    libellé = models.CharField(max_length=50)
    description = models.TextField()
    date_debut = models.DateField(null=True, default=datetime.date.today)
    date_fin = models.DateField(null=True, default=datetime.date.today)
    achevé = models.BooleanField(default=False)
    services = models.ManyToManyField(Service)
    images = models.ManyToManyField('Images_Projet', blank=True)

    def __str__(self):
        return f"{self.libellé}, {self.description}, {self.date_debut}, {self.date_fin}, {self.achevé}"

class Images_Projet(models.Model):
    project = models.ForeignKey(Projet, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='project_images/')

    def __str__(self):
        return self.image.name

class Equipe(models.Model):
    projet = models.ForeignKey(Projet, on_delete=models.CASCADE)
    membres = models.ManyToManyField(Personnel)

    def __str__(self):
        return f"{self.projet.libellé}, {', '.join([m.nom for m in self.membres.all()])}"

class Détail(models.Model):
    projet = models.ForeignKey(Projet, on_delete=models.CASCADE)
    membres = models.ManyToManyField(Personnel)
    detail_Project = models.FileField(upload_to='pdf_files/',null=True)

    def __str__(self):
        return f"{self.projet.libellé}, {', '.join([m.nom for m in self.membres.all()])}"

class Contact(models.Model):
    username = models.CharField(null=True,max_length=50,default='')
    objet = models.CharField(null=True,max_length=255)
    message = models.TextField(null=True)
    def __str__(self):
        return self.objet

class Temoignage(models.Model):
    nom = models.CharField(max_length=255)
    texte = models.TextField()
    image = models.ImageField(null=True,upload_to='temoignage-images/')

    def __str__(self):
        return self.nom

        
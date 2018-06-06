from django.db import models

# Create your models here.
class Editor(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()

    def __str__(self):
        return self.first_name

    def save_editor(self):
        self.save()
    def display_editor(self):
        self.objects.all()
    def update_editor(self):
        self.objects.update()
    def delete_editor(self):
        self.objects.delete()
    class Meta:
        ordering = ['first_name']

class Projects(models.Model):
    title = models.CharField(max_length =60)
    project = models.TextField()
    link = models.CharField(null = True,max_length =500)
    editor = models.ForeignKey(Editor)
    pub_date = models.DateTimeField(auto_now_add=True)
    article_image = models.ImageField(upload_to = 'projects/',blank = True)
    @classmethod
    def project_list(cls):
        
        projects = cls.objects.all()
        return projects
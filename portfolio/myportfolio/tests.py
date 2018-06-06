from django.test import TestCase
from .models import Editor,Projects
# Create your tests here.
class EditorTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.james= Editor(first_name = 'James', last_name ='Muriuki', email ='james@moringaschool.com')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.james,Editor))
    
    # Testing Save Method
    def test_save_method(self):
        self.james.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)

    def test_display_method(self):
        self.james.display_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)

    def test_update_method(self):
        self.james.update_editor()
        editors = Editor.objects.update()
        self.assertTrue(len(editors) > 0)

    def test_delete_method(self):
        self.james.delete_editor()
        editors = Editor.objects.delete()
        self.assertTrue(len(editors) > 0)

class ProjectsTestClass(TestCase):

    def setUp(self):
        # Creating a new editor and saving it
        self.james= Editor(first_name = 'James', last_name ='Muriuki', email ='james@moringaschool.com')
        self.james.save_editor()


        self.new_project= Projects(title = 'Test Article',post = 'This is a random test Post',editor = self.james)
        self.new_project.save()


    def tearDown(self):
        Editor.objects.all().delete()
        Projects.objects.all().delete()

    def test_get_project_list(self):
        project_list = Projects.project_list()
        self.assertTrue(len(project_list)>0)
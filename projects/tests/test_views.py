from django.urls import reverse
from django.contrib.auth import get_user_model

from rest_framework.test import APITestCase

from projects.models import Project

User = get_user_model()

class ProjectsAPIViewsTests(APITestCase):

    def test_project_destroy_api_view_is_owner_only(self):
        user1 = User.objects.create_user(email='user1@email.com', password='secret1234')
        user2 = User.objects.create_user(email='user2@email.com', password='secret1234')
        project = Project.objects.create(owner=user1, name='My project')
        url = reverse('projects:project_delete_api_view', kwargs={'pk': project.pk})
        self.client.force_authenticate(user=user2)
        response = self.client.delete(url)
        self.assertEquals(response.status_code, 403)

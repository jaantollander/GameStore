from django.test import TestCase


class TestViews(TestCase):
    def test_index(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'gamestore/index.html')

    def test_profile(self):
        response = self.client.get('/accounts/profile')

        # If user is not logged in
        self.assertEquals(response.status_code, 302)

        # TODO: User logged in
        # self.assertEquals(response.status_code, 200)
        # self.assertTemplateUsed(response, 'accounts/profile.html')

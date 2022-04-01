from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from testdemos.web.models import Profile
from testdemos.web.views import PetListView

UserModel = get_user_model()


class ProfilesListViewTests(TestCase):
    def test_get__expect_correct_template(self):
        response = self.client.get(reverse('list profiles'))
        self.assertTemplateUsed(response, 'profiles/list.html')

    def test_get__when_two_profiles__expect_context_to_contain_two_profiles(self):
        # Arrange
        profiles_to_create = (
            Profile(first_name='Ivo', last_name='ivov', age=14),
            Profile(first_name='Ivov', last_name='ivovv', age=15),

        )
        Profile.objects.bulk_create(profiles_to_create)
        # with bulk_create you imitate db fills

        # Act
        response = self.client.get(reverse('list profiles'))

        profiles = response.context['object_list']

        # check for actual profiles
        self.assertEqual(len(profiles), 2)

    def test_get__when_logged_in_user__expect_context_user_to_be_username(self):
        user_data = {
            'username': 'doncho',
            'password': 'doncho123'
        }
        UserModel.objects.create_user(**user_data)
        self.client.login(**user_data)
        response = self.client.get(reverse('list profiles'))

        self.assertEqual(
            user_data['username'],
            response.context[SOMEOBJECT.context_user_key]  # context_user_key is already defined in the class

        )

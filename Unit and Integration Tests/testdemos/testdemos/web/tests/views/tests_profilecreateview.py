from django.test import TestCase
from django.urls import reverse


class ProfileCreateViewTests(TestCase):
    def test_create_profile_when_all_valid__expect_to_create(self):
        profile_data = {
            'first_name':'doncho',
            'last_name':'minkov',
            'age': 14
        }

        self.client.post(reverse('create profile'),
                         data=profile_data,)

        profile = Profile.objects.first()
        self.assertIsNotNone(profile)
        self.assertEqual(profile_data['first_name'],profile.first_name)
        self.assertEqual(profile_data['last_name'],profile.last_name)
        self.assertEqual(profile_data['age'],profile.age)

from unittest import TestCase

from django.core.exceptions import ValidationError
from django.test import TestCase as DTestCase

from testdemos.web.models import Profile


class ProfileTests(TestCase):
    VALID_USER_DATA = {
        'first_name': 'Ivo',
        'last_name': 'Ivanov',
        'age': 15
    }

    def test_profile_create__when_first_name_contains_only_letters__expect_success(self):
        profile = Profile(**self.VALID_USER_DATA)
        profile.save()
        # self.assertIsNotNone(profile.pk)

    def test_profile_create__when_first_name_contains_a_digit__expect_to_fail(self):
        first_name = 'Ivo1'
        profile = Profile(
            first_name=first_name,
            last_name=self.VALID_USER_DATA['last_name'],
            age=self.VALID_USER_DATA['age'],
        )
        with self.assertRaises(ValidationError) as context:
            profile.full_clean()  # This is called in ModelForms implicitly
            profile.save()

        self.assertIsNotNone(context.exception)

    def test_profile_create__when_first_name_contains_a_dollar_sign__expect_to_fail(self):
        first_name = 'Ivo$'
        profile = Profile(
            first_name=first_name,
            last_name=self.VALID_USER_DATA['last_name'],
            age=self.VALID_USER_DATA['age'],
        )
        with self.assertRaises(ValidationError) as context:
            profile.full_clean()  # This is called in ModelForms implicitly
            profile.save()

        self.assertIsNotNone(context.exception)
    def test_profile_create__when_first_name_contains_a_space__expect_to_fail(self):
        first_name = 'Iv o'
        profile = Profile(
            first_name=first_name,
            last_name=self.VALID_USER_DATA['last_name'],
            age=self.VALID_USER_DATA['age'],
        )
        with self.assertRaises(ValidationError) as context:
            profile.full_clean()  # This is called in ModelForms implicitly
            profile.save()

        self.assertIsNotNone(context.exception)

    def test_profile_full_name__when_valid__expect_correct_full_name(self):
        pass

from unittest import TestCase

from unit_tests.main import let_this_user_in


class LetUsersTests(TestCase):
    def test_let_a_user_from_the_list(self):
        username = 'Alice'

        result = let_this_user_in(username)

        self.assertTrue(result)

    def test_let_another_user_from_the_list(self):
        username = 'Bob'

        result = let_this_user_in(username)

        self.assertTrue(result)

    def test_let_another_user_from_the_list_case_insensitive(self):
        username = 'BoB'

        result = let_this_user_in(username)

        self.assertTrue(result)

    def test_do_not_let_the_user_out_of_the_list(self):
        username = 'Charlie'

        result = let_this_user_in(username)

        self.assertFalse(result)

    # # this is a failing test
    # def test_do_not_let_the_user_which_is_not_a_string(self):
    #     username = 1
    #
    #     result = let_this_user_in(username)
    #
    #     self.assertFalse(result)
    #
    #     # if not isinstance(username, str):
    #     #     return False


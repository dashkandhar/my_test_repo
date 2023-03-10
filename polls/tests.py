from django.test import TestCase

from .models import Poll


class PollTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.poll_1 = Poll.objects.create(
            title="What's your name ?", text="tell us about your origin"
        )
        super(PollTestCase, cls).setUpClass()

    @classmethod
    def tearDownClass(cls) -> None:
        return super().tearDownClass()

    def test_poll_text(self):
        self.assertEqual(self.poll_1.text, "tell us about your origin")

    def test_poll_title(self):
        self.assertEqual(self.poll_1.title, "What's your name ?")

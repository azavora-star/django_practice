from django.test import TestCase
from polls.models import Question

class QuestionTest(TestCase):
    def setUp(self):
        Question.objects.create(question_text="Test Question", pub_date="2023-09-16 07:36:29")
        
    def test_orm(self):
        TestObject = Question.objects.filter(pub_date="2023-09-16 07:36:29").first()
        text = TestObject.question_text
        self.assertEqual("Test Question", text)
# if __name__ == "__main__":
#     unittest.main()
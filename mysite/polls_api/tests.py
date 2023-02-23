from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from polls.models import Question
from polls_api.serializers import QuestionSerializer


class QuestionListTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass'
        )
        self.client.force_authenticate(user=self.user)
        # self.client.enforce_csrf_checks = True
        self.question = Question.objects.create(
            question_text='Test question',
            owner=self.user
        )
        self.url = reverse('question-list')

    def test_question_list_authenticated(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        question_data = response.data[0]
        self.assertEqual(question_data['question_text'], self.question.question_text)

    def test_question_list_unauthenticated(self):
        self.client.logout()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        question_data = response.data[0]
        self.assertEqual(question_data['question_text'], self.question.question_text)

    def test_create_question_authenticated(self):
        response = self.client.get(self.url)
        print(f'#####Cookies: {response.cookies}')
        csrftoken = response.cookies['csrftoken'].value
        
        data = {'question_text': 'New question'}
        response = self.client.post(self.url, data, headers={'X-CSRFToken': csrftoken})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Question.objects.count(), 2)

    def test_create_question_unauthenticated(self):
        self.client.logout()
        data = {'question_text': 'New question'}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Question.objects.count(), 1)


class QuestionDetailTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass'
        )
        self.client.force_authenticate(user=self.user)
        self.question = Question.objects.create(
            question_text='Test question',
            owner=self.user
        )
        self.url = reverse('question-detail', args=[self.question.id])

    def test_question_detail_authenticated(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['question_text'], self.question.question_text)

    def test_question_detail_unauthenticated(self):
        self.client.logout()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['question_text'], self.question.question_text)

    def test_update_question_authenticated(self):
        data = {'question_text': 'Updated question'}
        response = self.client.put(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.question.refresh_from_db()
        self.assertEqual(self.question.question_text, 'Updated question')

    def test_update_question_unauthenticated(self):
        self.client.logout()
        data = {'question_text': 'Updated question'}
        response = self.client.put(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.question.refresh_from_db()
        self.assertEqual(self.question.question_text, 'Test question')

    def test_delete_question_authenticated(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Question.objects.count(), 0)

    def test_delete_question_unauthenticated(self):
        self.client.logout()
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

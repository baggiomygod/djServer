from django.test import TestCase

# Create your tests here.
import datetime

from django.urls import reverse
from django.utils import timezone
from django.test import TestCase
from .models import Question


# 测试数据模型
class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        """
         未来时间
        """
        time = timezone.now() + datetime.timedelta(days=30)
        now = timezone.now()
        start = now - datetime.timedelta(days=1)
        print(start, time, now)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """
        过去时间
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        符合要求的时间
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)


# 创建测试
def create_question(question_text, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


# index 列表页面的测试
class QuestionIndexViewTests(TestCase):
    def test_no_question(self):
        """
        if no questions exist, an appropriate message is displayed
        """
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        # 检查返回的网页上有没有"No polls are available."
        self.assertContains(response, 'No polls are available.')
        # latest_question_list是否为空
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_past_question(self):
        """
        Question with a pub_date in the past are displayed on the index page
        """
        question = create_question(question_text="Past question", days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            [question]
        )

    def test_future_question(self):
        """
        Question with a pub_date in the future aren't displayed on the index page
        """
        create_question(question_text="Future question", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, "No polls are available.")  # 包含“No polls are available.”
        self.assertQuerysetEqual(response.context['latest_question_list'], [])  # 断言一个查询集 qs 与一个特定的可迭代对象 values 的值匹配。

    def test_future_question_and_past_question(self):
        """
        Even if both past and future question exist, only past displayed.
        """
        question = create_question(question_text="Past Question.", days=-30)
        create_question(question_text="Future question.", days=30)

        response = self.client.get(reverse('polls:index'))

        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            [question]
        )

    def test_two_past_questions(self):
        question1 = create_question(question_text="Past question 1.", days=-30)
        question2 = create_question(question_text="Past question 2.", days=-5)

        response = self.client.get(reverse('polls:index'))
        # 列表是时间排序，近的在前面
        self.assertQuerysetEqual(response.context['latest_question_list'], [question2, question1]),


# 测试详情页
class QuestionDetailViewTests(TestCase):
    def test_future_question(self):
        future_question = create_question(question_text="Future question.", days=5)
        # 访问详情的url地址
        url = reverse('polls:detail', args=(future_question.id,))
        # 客户端请求获取响应
        response = self.client.get(url)
        # 返回应该是404
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        past_question = create_question(question_text="Past question.", days=-5)
        url = reverse('polls:detail', args=(past_question.id,))
        response = self.client.get(url)
        # 过去时间的question有响应数据，并且包含question_text字段
        self.assertContains(response, past_question.question_text)


# 结果测试
class QuestionResultViewTests(TestCase):
    def test_success_result(self):
        """
            success result page
        """

        success_question = create_question(question_text="Success Result.", days=-5)
        url = reverse('polls:results', args=(success_question.id,))
        response = self.client.get(url)
        self.assertContains(response, success_question.question_text)

# 测试投票
# class ChoiceVotesTests(TestCase):
#     def test_not_select_choice(self):
#         question = create_question(question_text="vote Question", days=-1)
#         response = self.client.post()

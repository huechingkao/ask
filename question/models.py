from django.db import models

class Question(models.Model):
    subject = models.CharField(max_length=200, verbose_name='問題')
    publication_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.subject          

class Answer(models.Model):
    question = models.ForeignKey(Question,on_delete=models.SET_NULL, null=True, verbose_name='問題')
    content = models.TextField(verbose_name='答案')

    def __str__(self):
        return self.content
      
    def get_absolute_url(self):
        return '/question/q/' + str(self.question.id)
from django.views import generic
from .models import Question, Answer
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse

class QuestionListView(generic.ListView):
    model = Question
    
class QuestionDetailView(generic.DetailView):
    model = Question    

class QuestionCreate(CreateView):
    model = Question
    fields = ['subject']
    success_url = "/"   
    template_name = 'form.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = '新增問題'
        context['backpath'] = "/"
        return context

class QuestionUpdate(UpdateView):
    model = Question
    fields = '__all__'   
    success_url = "/"   
    template_name = 'form.html'   

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = '修改問題'
        context['backpath'] = "/"
        return context

class QuestionDelete(DeleteView):
    model = Question
    success_url = "/"
    template_name = 'confirm_delete.html'        

class AnswerCreate(CreateView):
    model = Answer
    fields = ['content'] 
    template_name = 'form.html'     
    
    def form_valid(self, form):        
        form.instance.question = Question.objects.get(id=self.kwargs['q'])
        return super(AnswerCreate, self).form_valid(form)    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = '新增答案'
        context['backpath'] = "/question/q/"+str(self.kwargs['q'])
        return context
      
class AnswerUpdate(UpdateView):
    model = Answer
    fields = ['content']
    template_name = 'form.html'   

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = '修改答案'
        context['backpath'] = "/question/q/"+str(self.kwargs['q'])
        return context

class AnswerDelete(DeleteView):
    model = Answer
    template_name = 'confirm_delete.html'        
    
    def get_success_url(self):
        return reverse('question_detail', kwargs={'pk': self.kwargs['q']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['backpath'] = "/question/q/"+str(self.kwargs['q'])
        return context
    
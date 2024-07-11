from django.shortcuts import render
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import MathQuestion, TCGQuestion, MathComment, TCGComment
from django.urls import reverse_lazy
from .forms import MathCommentForm, TCGCommentForm

def index(request):
    return render(request, 'learning/base.html')

def community_home(request):
    return render(request, 'community/community.html')

def math_forum(request):
    return render(request, 'community/math_forum.html')

def tcg_forum(request):
    return render(request, 'community/tcg_forum.html')

class MathQuestionListView(ListView):
    model = MathQuestion
    template_name = 'community/math_forum.html'
    context_object_name ='questions'
    ordering = ['-date_created']

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        search_input = self.request.GET.get('search-area') or ""
        if search_input:
            context['questions'] = context['questions'].filter(title__icontains = search_input)
            context['search_input'] = search_input
        return context

class TCGQuestionListView(ListView):
    model = TCGQuestion
    template_name = 'community/tcg_forum.html'
    context_object_name ='questions'
    ordering = ['-date_created']

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        search_input = self.request.GET.get('search-area') or ""
        if search_input:
            context['questions'] = context['questions'].filter(title__icontains = search_input)
            context['search_input'] = search_input
        return context

class MathQuestionDetailView(DetailView):
    model = MathQuestion

class TCGQuestionDetailView(DetailView):
    model = TCGQuestion

class MathQuestionCreateView(LoginRequiredMixin, CreateView):
    model = MathQuestion
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('community:math_question_details', kwargs={'pk': self.object.pk})

class TCGQuestionCreateView(LoginRequiredMixin, CreateView):
    model = TCGQuestion
    fields = ['title', 'content']
    success_url = reverse_lazy('community:tcg_forum')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('community:tcg_question_details', kwargs={'pk': self.object.pk})
    
class MathQuestionUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = MathQuestion
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        question = self.get_object()
        if self.request.user == question.user:
            return True
        return False
    
class TCGQuestionUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = TCGQuestion
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        question = self.get_object()
        if self.request.user == question.user:
            return True
        return False
    
class MathQuestionDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = MathQuestion
    context_object_name =  'question'
    success_url = reverse_lazy('community:math_forum')

    def test_func(self):
        question = self.get_object()
        if self.request.user == question.user:
            return True
        return False

class TCGQuestionDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = TCGQuestion
    context_object_name =  'question'
    success_url = reverse_lazy('community:tcg_forum')

    def test_func(self):
        question = self.get_object()
        if self.request.user == question.user:
            return True
        return False 
    
class MathCommentDetailView(CreateView):
    model = MathComment
    form_class = MathCommentForm
    template_name = 'community/mathquestion_detail.html'

    def form_valid(self, form):
        form.instance.question_id = self.kwargs['pk']
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('community:math_question_details', kwargs={'pk': self.kwargs['pk']})

class TCGCommentDetailView(CreateView):
    model = TCGComment
    form_class = TCGCommentForm
    template_name = 'community/tcgquestion_detail.html'

    def form_valid(self, form):
        form.instance.question_id = self.kwargs['pk']
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('community:tcg_question_details', kwargs={'pk': self.kwargs['pk']})

class AddMathCommentView(CreateView):
    model = MathComment
    form_class = MathCommentForm
    template_name = 'community/mathquestion_answer.html'

    def form_valid(self, form):
        form.instance.question_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('community:math_question_details', kwargs={'pk': self.kwargs['pk']})

class AddTCGCommentView(CreateView):
    model = TCGComment
    form_class = TCGCommentForm
    template_name = 'community/tcgquestion_answer.html'

    def form_valid(self, form):
        form.instance.question_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('community:tcg_question_details', kwargs={'pk': self.kwargs['pk']})
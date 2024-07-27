from django.shortcuts import render
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import MathQuestion, TCGQuestion, MathComment, TCGComment
from learning.models import Badge, CompletedBadge
from django.urls import reverse_lazy
from .forms import MathCommentForm, TCGCommentForm
from django.contrib import messages

# website homepage
def index(request):
    return render(request, 'learning/base.html')

# community page
def community_home(request):
    return render(request, 'community/community.html')

# math forum
def math_forum(request):
    return render(request, 'community/math_forum.html')

# tcg forum
def tcg_forum(request):
    return render(request, 'community/tcg_forum.html')

# list of math posts
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

# list of tcg posts
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

# math post details
class MathQuestionDetailView(DetailView):
    model = MathQuestion

# tcg post details
class TCGQuestionDetailView(DetailView):
    model = TCGQuestion

# create math question
class MathQuestionCreateView(LoginRequiredMixin, CreateView):
    model = MathQuestion
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.user = self.request.user
        response = super().form_valid(form)
        
        user = self.request.user

        # check for Factorial Badge (creation of first math forum post)
        if not CompletedBadge.objects.filter(student=user, badge__name='Factorial Badge').exists():
            if MathQuestion.objects.filter(user=user).count() == 1:
                badge = Badge.objects.get(name='Factorial Badge')
                CompletedBadge.objects.create(student=user, badge=badge)
                messages.success(self.request, "Congratulations! You've earned the Factorial Badge!")
        
        return response

    def get_success_url(self):
        return reverse_lazy('community:math_question_details', kwargs={'pk': self.object.pk})

# create tcg question
class TCGQuestionCreateView(LoginRequiredMixin, CreateView):
    model = TCGQuestion
    fields = ['title', 'content']
    success_url = reverse_lazy('community:tcg_forum')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('community:tcg_question_details', kwargs={'pk': self.object.pk})

# update a math question    
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
    
    def get_success_url(self):
        return reverse_lazy('community:math_question_details', kwargs={'pk': self.object.pk})

# update a tcg question    
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
    
    def get_success_url(self):
        return reverse_lazy('community:tcg_question_details', kwargs={'pk': self.object.pk})

# delete a math question    
class MathQuestionDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = MathQuestion
    context_object_name =  'question'
    success_url = reverse_lazy('community:math_forum')

    def test_func(self):
        question = self.get_object()
        if self.request.user == question.user:
            return True
        return False

# delete a tcg question    
class TCGQuestionDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = TCGQuestion
    context_object_name =  'question'
    success_url = reverse_lazy('community:tcg_forum')

    def test_func(self):
        question = self.get_object()
        if self.request.user == question.user:
            return True
        return False 

# math comment details    
class MathCommentDetailView(CreateView):
    model = MathComment
    form_class = MathCommentForm
    template_name = 'community/mathquestion_detail.html'

    def form_valid(self, form):
        form.instance.question_id = self.kwargs['pk']
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('community:math_question_details', kwargs={'pk': self.kwargs['pk']})

# tcg comment details    
class TCGCommentDetailView(CreateView):
    model = TCGComment
    form_class = TCGCommentForm
    template_name = 'community/tcgquestion_detail.html'

    def form_valid(self, form):
        form.instance.question_id = self.kwargs['pk']
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('community:tcg_question_details', kwargs={'pk': self.kwargs['pk']})

# comment on a math post
class AddMathCommentView(LoginRequiredMixin, CreateView):
    model = MathComment
    form_class = MathCommentForm
    template_name = 'community/mathquestion_answer.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.question_id = self.kwargs['pk']
        response = super().form_valid(form)
        
        user = self.request.user

        # check for Sigma Badge (creation of first math forum comment)
        if not CompletedBadge.objects.filter(student=user, badge__name='Sigma Badge').exists():
            if MathComment.objects.filter(user=user).count() == 1:
                badge = Badge.objects.get(name='Sigma Badge')
                CompletedBadge.objects.create(student=user, badge=badge)
                messages.success(self.request, "Congratulations! You've earned the Sigma Badge!")
        
        return response

    def get_success_url(self):
        return reverse_lazy('community:math_question_details', kwargs={'pk': self.kwargs['pk']})

# comment on a tcg post
class AddTCGCommentView(LoginRequiredMixin, CreateView):
    model = TCGComment
    form_class = TCGCommentForm
    template_name = 'community/tcgquestion_answer.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.question_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('community:tcg_question_details', kwargs={'pk': self.kwargs['pk']})
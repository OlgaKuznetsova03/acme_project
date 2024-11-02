# birthday/views.py 
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .forms import BirthdayForm
# Импортируем из utils.py функцию для подсчёта дней.
from .utils import calculate_birthday_countdown
from .models import Birthday


class BirthdayDeleteView(DeleteView):
    model = Birthday
    template_name = 'birthday/birthday.html'
    success_url = reverse_lazy('birthday:list')


class BirthdayMixin:
    model = Birthday
    form_class = BirthdayForm
    template_name = 'birthday/birthday.html'
    success_url = reverse_lazy('birthday:list')


# Добавляем миксин первым по списку родительских классов.
class BirthdayCreateView(BirthdayMixin, CreateView):
    # Не нужно описывать атрибуты: все они унаследованы от BirthdayMixin.
    pass


class BirthdayUpdateView(BirthdayMixin, UpdateView):
    # И здесь все атрибуты наследуются от BirthdayMixin.
    pass  

class BirthdayListView(ListView):
    # Указываем модель, с которой работает CBV...
    model = Birthday
    # ...сортировку, которая будет применена при выводе списка объектов:
    ordering = 'id'
    # ...и даже настройки пагинации:
    paginate_by = 10 

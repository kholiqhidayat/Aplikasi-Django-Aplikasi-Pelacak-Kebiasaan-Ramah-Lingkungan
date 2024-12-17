from django.shortcuts import render, get_object_or_404, redirect
from .models import Habit
from .forms import HabitForm

def home(request):
    habits = Habit.objects.all()
    return render(request, 'tracker/home.html', {'habits': habits})

def add_habit(request):
    if request.method == 'POST':
        form = HabitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = HabitForm()
    return render(request, 'tracker/add_habit.html', {'form': form})

def update_habit(request, habit_id):
    habit = get_object_or_404(Habit, id=habit_id)  # Memastikan habit ada
    if request.method == 'POST':
        form = HabitForm(request.POST, instance=habit)  # Mengisi form dengan data habit
        if form.is_valid():
            form.save()  # Menyimpan data yang sudah diperbarui
            return redirect('home')
    else:
        form = HabitForm(instance=habit)  # Menampilkan form dengan data habit yang ada
    return render(request, 'tracker/update_habit.html', {'form': form})

def delete_habit(request, habit_id):
    habit = get_object_or_404(Habit, pk=habit_id)  # Menemukan habit berdasarkan ID
    habit.delete()  # Menghapus habit dari database
    return redirect('home')  # Mengarahkan kembali ke halaman utama setelah penghapusan

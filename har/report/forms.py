from django.shortcuts import render, redirect, get_object_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import ConnectionForm, ReportForm
from .models import Report

def render_connection_view(request):
    error_message = None
    if request.method == 'POST':
        form = ConnectionForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            # Check if user exists (using email as username)
            user = authenticate(request, username=email, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('reports_list')
            else:
                # If user doesn't exist, create one. If password mismatch, show error.
                if not User.objects.filter(username=email).exists():
                    user = User.objects.create_user(username=email, email=email, password=password)
                    login(request, user)
                    return redirect('reports_list')
                else:
                    error_message = "Invalid password for this account."
    else:
        form = ConnectionForm()
    
    return render(request, 'connection.html', {'form': form, 'error': error_message})

@login_required
def render_reports_view(request):
    reports = Report.objects.filter(user=request.user).order_by('creation_time')
    return render(request, 'reports.html', {'reports': reports})

@login_required
def render_report_creation_view(request):
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.user = request.user
            report.save()
            return redirect('reports_list')
    else:
        form = ReportForm()
    return render(request, 'report_creation.html', {'form': form})

@login_required
def render_report_update_view(request, id):
    report = get_object_or_404(Report, id=id, user=request.user)
    if request.method == 'POST':
        form = ReportForm(request.POST, instance=report)
        if form.is_valid():
            form.save()
            return redirect('reports_list')
    else:
        form = ReportForm(instance=report)
    return render(request, 'report_update.html', {'form': form, 'report': report})

@login_required
def render_report_deletion_view(request, id):
    report = get_object_or_404(Report, id=id, user=request.user)
    report.delete()
    return redirect('reports_list')

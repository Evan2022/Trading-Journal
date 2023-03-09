from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from core.forms import CustomLoginForm, CustomSignupForm
from . models import Journal, Trade
from . forms import JournalForm, TradeForm


def login_view(request):
    form = CustomLoginForm()
    context = {'form': form}
    return render(request, 'login.html', context)


def signup_view(request):
    form = CustomSignupForm()
    context = {'form': form}
    return render(request, 'signup.html', context)


@login_required
def deleteJournal(request):
    if request.method == 'POST':
        journal_id = request.POST.get('journal_id')
        journal = Journal.objects.get(id=journal_id)
        journal.delete()
    journals = Journal.objects.filter(user=request.user).order_by('date_created')
    context = {'journals': journals}
    return render(request, 'journals.html', context)


def jform(request):
    form = JournalForm()
    if request.method == 'POST':
        form = JournalForm(request.POST)
        if form.is_valid():
            form.save(request.user)
            return redirect('journals')
    context = {'form': form}
    return render(request, 'jform.html', context)


def updateJournal(request, journal_id):
    journal = Journal.objects.get(id=journal_id)
    form = JournalForm(instance=journal)
    if request.method == 'POST':
        form = JournalForm(request.POST, instance=journal)
        if form.is_valid():
            form.save(request.user)
            return redirect('journals')
    context = {'form': form}
    return render(request, 'jform.html', context)


@login_required
def deleteTrade(request, journal_id):
    journal = Journal.objects.get(id=journal_id, user=request.user)
    if request.method == 'POST':
        trade_id = request.POST.get('trade_id')
        trade = Trade.objects.get(id=trade_id, journal=journal)
        trade.delete()
    trades = Trade.objects.filter(journal=journal)
    context = {'journal': journal,'trades': trades, }
    return render(request, 'trades.html', context)


def tform(request, journal_id):
    form = TradeForm()
    journal = Journal.objects.get(id=journal_id, user=request.user)
    trades = Trade.objects.filter(journal=journal)
    if request.method == 'POST':
        form = TradeForm(request.POST)
        if form.is_valid():
            trade = form.save(commit=False)
            trade.journal = journal
            trade.save()
            return redirect('trades', journal_id)
    context = {'form': form}
    return render(request, 'tform.html', context)


@login_required
def updateTrade(request, journal_id, trade_id):
    journal = Journal.objects.get(id=journal_id, user=request.user)
    trade = Trade.objects.get(id=trade_id, journal=journal)
    form = TradeForm(instance=trade)
    if request.method == 'POST':
        form = TradeForm(request.POST, instance=trade)
        if form.is_valid():
            trade = form.save(commit=False)
            trade.journal = journal
            trade.save()
            return redirect('trades', journal_id)
    context = {'form': form}
    return render(request, 'tform.html', context)
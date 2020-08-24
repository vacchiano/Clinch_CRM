from django.shortcuts import render, HttpResponse, redirect
from .forms import ContactForm, NoteForm, PartyForm
from .models import Contact, Note, Party
from django.contrib.auth.decorators import login_required
from django.utils import timezone

# Create your views here.
@login_required
def index(request):
    #query all the contacts for this logged in user
    #pass them into context
    contacts = request.user.contacts.all()

    #query all the parties for this logged in user
    #pass them into context
    parties = request.user.parties.all()

    context = {
        'contacts':contacts,
        'parties':parties
    }

    return render(request, 'customer_sys/index.html', context)

def newContact(request):
    form = ContactForm
    context = {
        'form':form
    }
    return render(request, 'customer_sys/addCustomer.html', context)

def createCustomer(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.consultant = request.user
            contact.created_at = timezone.now()
            contact.updated_at = timezone.now()
            contact.save()
            return redirect('/app/')
        return render(request, 'customer_sys/addCustomer.html', {'form':ContactForm(request.POST)})
    return render(request, 'customer_sys/addCustomer.html', {'form':ContactForm()})

def customerPage(request, cust_id):
    contact = Contact.objects.get(id=cust_id)
    if contact not in request.user.contacts.all():
        return redirect('/app/')

    else:
        notes = contact.notes.all().order_by('-created_at')
        parties_hosted = contact.parties_hosting.all()
        parties_attending = contact.parties_attending.all()
        note_form = NoteForm()
        context = {
            "contact":contact,
            "parties_hosted":parties_hosted,
            "parties_attended":parties_attending,
            "notes":notes,
            "note_form":note_form,
        }
        return render(request, 'customer_sys/customerPage.html', context)

def customerEdit(request, cust_id):
    contact = Contact.objects.get(id=cust_id)

    if request.method == "POST":
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.updated_at = timezone.now()
            contact.save()
            return redirect('customerPage', cust_id=cust_id)

    # form = ContactForm(initial={
    #     'first_name':contact.first_name,
    #     'last_name':contact.last_name,
    #     'email':contact.email,
    #     'phone':contact.phone,
    #     'address':contact.address,
    #     'status':contact.status,
    #     'last_contact':contact.last_contact,
    #     'bg_info':contact.bg_info,
    #     })
    form = ContactForm(instance=contact)
    context = {
        "form":form,
        "contact":contact,
    }
    return render(request, 'customer_sys/customerEdit.html', context)

def customerDelete(request, cust_id):
    contact = Contact.objects.get(id=cust_id)
    if contact.consultant == request.user:
        contact.delete()
        return redirect('/app/')
    else:
        return redirect('/app/')

def newParty(request):
    form = PartyForm(user=request.user)
    context = {
        'form':form
    }
    return render(request, 'customer_sys/addParty.html', context)

def createParty(request):
    if request.method == "POST":
        form = PartyForm(user=request.user, data=request.POST)
        if form.is_valid():
            party = form.save(commit=False)
            party.consultant = request.user
            party.created_at = timezone.now()
            party.updated_at = timezone.now()
            #print ("Host: " + party.host)
            party.save()
            form.save_m2m() #saves the many to many relationship
            return redirect('/app/')
        return render(request, 'customer_sys/addParty.html', {'form':PartyForm(request.POST)})
    return render(request, 'customer_sys/addParty.html', {'form':PartyForm()})

def partyPage(request, party_id):
    party = Party.objects.get(id=party_id)
    guests = party.guest.all()
    context = {
        "party":party,
        "guests":guests
    }
    return render(request, 'customer_sys/partyPage.html', context)

def partyEdit(request, party_id):
    party = Party.objects.get(id=party_id)

    if request.method == "POST":
        form = PartyForm(request.user, data=request.POST, instance=party)
        if form.is_valid():
            thisParty = form.save(commit=False)
            thisParty.updated_at = timezone.now()
            thisParty.save()
            form.save_m2m() #saves the many to many relationship
            return redirect('partyPage', party_id=party.id)

    # form = ContactForm(initial={
    #     'first_name':contact.first_name,
    #     'last_name':contact.last_name,
    #     'email':contact.email,
    #     'phone':contact.phone,
    #     'address':contact.address,
    #     'status':contact.status,
    #     'last_contact':contact.last_contact,
    #     'bg_info':contact.bg_info,
    #     })
    form = PartyForm(instance=party, user=request.user)
    context = {
        "form":form,
        "party":party,
    }
    return render(request, 'customer_sys/partyEdit.html', context)

def deleteParty(request, party_id):
    party = Party.objects.get(id=party_id)
    if party.consultant == request.user:
        party.delete()
        return redirect('/app/')
    else:
        return redirect('/app/')

def addNote(request):
    if request.method == "POST":
        form = NoteForm(data=request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.contact = Contact.objects.get(id=request.POST['contact'])
            note.created_at = timezone.now()
            note.updated_at = timezone.now()
            note.save()
            return redirect('customerPage', cust_id=request.POST['contact'])

def deleteNote(request, note_id, cust_id):
    note = Note.objects.get(id=note_id)
    note.delete()
    return redirect('customerPage', cust_id=cust_id)
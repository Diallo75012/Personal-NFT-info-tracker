from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import NftRegistration
from .forms import NftInfoForm



# Create your views here.
def nfts(request):
    comingup = "We are going to show and record user nfts details" # just context testing
    form = NftInfoForm
    NftInfoTable = NftRegistration.objects.all()
    if request.method == 'POST':
        form = NftInfoForm(request.POST or None)
        if form.is_valid():
            data = form.cleaned_data
            collection = data.get('collection')
            price = data.get('price')
            max_supply = data.get('max_supply')
            nbr_minted  = data.get('nbr_minted')
            nbr_of_holders = data.get('nbr_of_holders')
            total_number_of_followers = data.get('total_number_of_followers')
            new_nft_info = NftRegistration(collection=collection, \
                price=price,\
                max_supply=max_supply, \
                nbr_minted=nbr_minted, \
                nbr_of_holders=nbr_of_holders,\
                total_number_of_followers=total_number_of_followers)
            new_nft_info.save()
            list(messages.get_messages(request))
            messages.success(request, "NFT CREATED SUCCESSFULLY!")
            return render(request, 'files/nfts.html', {"comingup": comingup,\
                 "form": form, "NftInfoTable": NftInfoTable})

    return render(request, 'files/nfts.html', {"comingup": comingup, \
        "form": form, "NftInfoTable": NftInfoTable})

def nfts_update(request, pk):
    NftUpdated = NftRegistration.objects.get(id=pk)
    form = NftInfoForm(instance=NftUpdated)
    if request.method == 'POST':
        form = NftInfoForm(request.POST, instance=NftUpdated)
        if form.is_valid():
            form.save()
            list(messages.get_messages(request))
            messages.success(request, "NFT UPDATED SUCCESSFULLY!")
            return redirect('files:nfts')
    else:
        form = NftInfoForm(instance=NftUpdated)
        return render(request, 'files/nfts_update.html', {'form': form})

def nfts_delete(request, pk):
    NftToDelete = NftRegistration.objects.get(id=pk)
    if request.method == 'POST':
        NftToDelete.delete()
        # we need to clear messages before being able to show them
        list(messages.get_messages(request))
        messages.success(request, "NFT DELETED SUCCESSFULLY!")
        return redirect('files:nfts')
    messages.error(request, "NFT NOT DELETED ERROR!")
    return render(request, 'files/nfts_to_delete.html', {"Nft_To_Delete": NftToDelete})
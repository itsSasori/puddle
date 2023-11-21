from django.http import HttpResponseNotFound
from django.shortcuts import redirect, render
from Items.models import *
from .models import *
from .forms import *

# Create your views here.
def new_conversation(request,pk):
    item = Item.objects.get(id=pk)

    conversation = Conversation.objects.filter(item=item, members__in=[request.user.id])

    if conversation:
        return redirect('conversation-detail', pk=conversation[0].id)

    if request.method == "POST":
        form = ConversationMessageForm(request.POST)
        if form.is_valid():
            conversation = Conversation.objects.create(item=item)
            conversation.members.add(request.user)
            conversation.members.add(item.created_by)
            conversation.save()

            message = form.save(commit=False)
            message.conversation = conversation
            message.created_by = request.user
            message.save()
            return redirect('inbox')
    else:
        form = ConversationMessageForm()
    context = {
            'form': form,
    }
    return render(request,'conversation/new_conversation.html',context)


def inbox(request):
    conversations = Conversation.objects.filter(members__in=[request.user.id])
    context={'conversations':conversations}
    return render(request,'conversation/inbox.html',context)


def conversation_detail(request,pk):
    try:
        conversations = Conversation.objects.filter(members__in=[request.user.id]).get(id=pk)
    except Conversation.DoesNotExist:
        return HttpResponseNotFound('No Conversation Found')

    if request.method == "POST":
        form = ConversationMessageForm(request.POST)
        if form.is_valid():

            message = form.save(commit=False)
            message.conversation = conversations
            message.created_by = request.user
            message.save()

            conversations.save()
            return redirect('conversation-detail',pk=conversations.id)
    else:
        form = ConversationMessageForm()
    context={'conversations':conversations,'form':form}
    return render(request,'conversation/conversation_detail.html',context)



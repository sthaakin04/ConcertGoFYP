from itertools import chain
from django.shortcuts import redirect, render
from .models import Order,Ticket,Profile
from django.http import JsonResponse

# Create your views here.
def orderTicket(request,pk):
    pks = pk
    tickets = Ticket.objects.filter(pk=pks)
    bb = request.GET.get('quantity')
    for a in tickets:#calculating total price
        print(a.price)
        tot = int(a.price) * int(bb)
    print(tot)
    
    return render(request, 'order/order.html',{'tickets':tickets,'a':a,'tot':tot,'quantity':bb})

def increment(request):
    
    quan = request.GET['increase']
    print(quan)

    data={
        'bool': quan
    }
    return JsonResponse(data)

def decrement(request):
    quan = request.GET['increase']
    print(quan)

    data={
        'bool': quan
    }
    return JsonResponse(data)

def paymentDone(request):
    bb = request.GET.get('tquan')
    cc =request.GET.get('ticketid')
    cd = Ticket.objects.filter(id=cc)
    print(cd)

    for cd in cd:
        if int(bb)<cd.quantity: #checking if the ticket is in stock
            use = request.user.profile
            print(cd.quantity)
            cd.quantity=cd.quantity-int(bb)
            cd.save()
            Order(buyer=use,ticket=cd,quantity=bb).save()
            
        return redirect('/mytickets')
    else:
        return redirect('/ticket')

    
    

def myTicketPage(request):
    profile = Profile.objects.get(user=request.user)
    tickets = []
    ts = None

    my_tickets = profile.profile_myTickets()

    tickets.append(my_tickets)
    # sort and chain querys and unpack the tickets list
    if len(tickets)>0:
        ts = sorted(chain(*tickets), reverse=True, key=lambda obj: obj.date_purchased)
    return render(request,'order/my_tickets.html',{'profile':profile,'tickets':ts})


def myTicketSales(request):
    order = Order.objects.all()
    return render(request, 'order/ticketSales.html', {'orders': order})
from django.shortcuts import render

# Create your views here.
def home(request):
    Dishes={
        "dish1":{
        "img":"static/core/images/cooked-food.jpg",
        "title":"Paneer Butter Masala",
        "desc":"Creamy and rich, with a delightful blend of spices, and perfect with naan or rice",
        },
        "dish2":{
            "img":"static/core/images/Salmon Fish.jpg",
            "title":"Grilled Salmon",
            "desc":"Perfectly grilled with a hint of lemon and herbs, served with a side of vegetables or salad",
        },
        "dish3":{
            "img":"static/core/images/Butter Chicken.jpg",
            "title":"Butter Chicken",
            "desc":"Tender chicken pieces cooked in a creamy tomato-based sauce, best enjoyed with naan or rice",
        },}
    return render(request,'core/home.html',{'Dishes': Dishes})

def menu(request):
    return render(request,'core/menu.html')

def tracking(request):
    return render(request,'core/tracking.html')

def reservation(request):
    return render(request,'core/reservation.html')
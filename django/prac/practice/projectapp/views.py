from django.shortcuts import render

# View for single user data
def index(request):
    name = "vishal"
    age = 25
    gender = "male"
    city = "Mumbai"
    country = "India"
    hobby = "reading"

    my_dict = {
        "name": name,
        "age": age,
        "gender": gender,
        "city": city,
        "country": country,
        "hobby": hobby
    }

    return render(request, "index.html", my_dict)  # ✅ This was missing

# View for employee list
def emp_list_view(request):
    emplist = [
        {"ename": "vishal", "esal": "100000", "eadd": "india"},
        {"ename": "prashant", "esal": "200000", "eadd": "india"},
        {"ename": "rahul", "esal": "300000", "eadd": "india"},
        {"ename": "ashish", "esal": "400000", "eadd": "india"},
        {"ename": "deepak", "esal": "500000", "eadd": "india"},
        {"ename": "vijay", "esal": "600000", "eadd": "india"},
        {"ename": "ankit", "esal": "700000", "eadd": "india"},
        {"ename": "shivam", "esal": "800000", "eadd": "india"},
    ]

    return render(request, "emp_list.html", {"emplist": emplist})  # ✅ Only one return here

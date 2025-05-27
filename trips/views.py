# في ملف trips/views.py
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, get_object_or_404,redirect
from.models import Trip ,UserInput ,Category


# from django.contrib import messages
# from datetime import datetime
#######################################################################################
# trips/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Trip, UserInput # استيراد الموديلات
from datetime import datetime # لاستيراد دالة تحويل التاريخ

def trip_form(request, trip_id):
    # جلب بيانات الرحلة الأساسية للعرض أو للحفظ
    trip = get_object_or_404(Trip, id=trip_id)

    if request.method == 'POST':
        # استقبال بيانات المستخدم من النموذج
        name = request.POST.get('nameField')
        email = request.POST.get('emailField')
        phone = request.POST.get('phoneField')
        address = request.POST.get('addressField')
        date_time_str = request.POST.get('dateTimeField') # السلسلة النصية من النموذج

        # --- التحقق الأساسي ---
        if not all([name, email, phone, address, date_time_str]):
            messages.error(request, 'يرجى ملء جميع حقول بيانات المستخدم المطلوبة.')
            # أعد عرض النموذج مع بيانات الرحلة والخطأ
            return render(request, 'trips/form_page.html', {'trip': trip})

        # --- تحويل التاريخ والوقت ---
        try:
            # datetime-local يرسل تنسيق يشبه ISO 8601، يمكن لـ fromisoformat التعامل معه
            parsed_datetime = datetime.fromisoformat(date_time_str)
        except ValueError:
            messages.error(request, 'تنسيق التاريخ والوقت غير صحيح.')
            # أعد عرض النموذج مع بيانات الرحلة والخطأ
            return render(request, 'trips/form_page.html', {'trip': trip})

        # --- الحفظ في قاعدة بيانات Django (موديل UserInput) ---
        try:
            booking = UserInput(
                # بيانات المستخدم
                name=name,
                email=email,
                phone=phone,
                address=address,
                date_time=parsed_datetime, # استخدم الكائن المحول

                # بيانات الرحلة (نسخة منها وقت الحجز)
                trip_name=trip.title,
                trip_location=trip.location,
                trip_phone=trip.responsible_phone, # لاحظ اسم الحقل في Trip
                trip_details=trip.description
            )
            booking.save() # احفظ سجل الحجز

            messages.success(request, f'شكراً لك, {name}! تم استلام طلب حجزك لرحلة "{trip.title}" بنجاح.')

            # --- إعادة التوجيه بعد نجاح POST ---
            # افترض أن لديك مسار URL باسم 'trips_list' لعرض قائمة الرحلات
            return redirect('trips_list')

        except Exception as e:
            # التعامل مع أي أخطاء أخرى أثناء الحفظ
            print(f"Error saving booking: {e}") # سجل الخطأ للتصحيح
            messages.error(request, 'حدث خطأ غير متوقع أثناء حفظ الحجز. يرجى المحاولة مرة أخرى.')
            # أعد عرض النموذج مع الخطأ
            return render(request, 'trips/form_page.html', {'trip': trip})

    else: # GET request
        # عرض النموذج فارغًا مع بيانات الرحلة
        return render(request, 'trips/form_page.html', {'trip': trip})

# تأكد من وجود view وقالب لعرض قائمة الرحلات (مثال)
def trips_list_view(request):
    trips = Trip.objects.filter(actve=True).order_by('-date') # عرض الرحلات المفعلة والأحدث أولاً
    # يمكنك إضافة UserInput هنا إذا أردت عرض الحجوزات أيضاً
    # user_bookings = UserInput.objects.all() # أو قم بتصفيتها حسب المستخدم الحالي إذا كان مسجلاً دخوله
    context = {'trips': trips}
    return render(request, 'trips/trips_list.html', context) # افترض وجود قالب trips_list.html

########################################################################################

# def get_data(request):
#     name = request.POST.get('nameField')
#     email = request.POST.get('emailField')
#     phone = request.POST.get('phoneField')
#     address = request.POST.get('addressField')
#     date_time = request.POST.get('dateTimeField')
#     booking = UserInput(
#             name=name,
#             email=email,
#             phone=phone,
#             address=address,
#             trip_datetime=date_time
#     )
#     booking.save()

#     return render(request, 'trips/form_page.html')

#######################################################################################

def index(request):
    trips = Trip.objects.all().order_by('-date')  # أحدث 3 رحلات للصفحة الرئيسية
    categories = Category.objects.all()  # جميع التصنيفات

    return render(request, 'trips/home.html', {
        'trips': trips,
        'categories': categories
    })

def trips_by_category(request, category_id):
    # جلب التصنيف المطلوب
    category = get_object_or_404(Category, id=category_id)
    # جلب الرحلات المرتبطة بهذا التصنيف
    trips = Trip.objects.filter(category=category).order_by('-date')

    return render(request, 'trips/trips_by_category.html', {
        'category': category,
        'trips': trips
    })

def trips_list(request):
    all_trips = Trip.objects.all().order_by('-date')
    return render(request,'trips/trips.html', {'all_trips': all_trips})
########################################################################################
# def trip_form(request, trip_id):
#     trip = get_object_or_404(Trip, id=trip_id)  # جلب بيانات الرحلة
#     return render(request, 'trips/form_page.html', {'trip': trip})

#     return render(request, 'trips/form_page.html', {'trip_id': trip_id})
###########################################################################################


# Goservice.com
its is service web application which provides services to the customers.


A web application that allows customers to book services such as plumbers, electricians, gardeners, and other professionals. Customers can select a service, book for a specific time period, make payments, and track the service providers.

---

## **Features**

- Browse available services (Plumbers, Electricians, Gardeners, etc.)
- Book a service instantly for a specific date and time
- Secure payment integration (simulate or integrate your preferred gateway)
- Track booked services
- User-friendly interface with dynamic interactions

---

## **Technologies Used**

- **Backend:** Django, Python  
- **Frontend:** HTML, CSS, JavaScript  
- **Database:** SQLite (default Django database, can be changed)  

---

## **Screenshots**

Here you can add screenshots to show how the project looks:

![Homepage](masterclass/images/1.png)  
![Booking Page](masterclass/images/2.png)  
![Payment Page](masterclass/images/3.png)  
![Confirmation](masterclass/images/4.png)  

*(Make sure the images are placed in `masterclass/images/` folder in your repo.)*

---

## **Installation & Execution**

Follow these steps to run the project locally:

1. **Clone the repository**

git clone https://github.com/Munu07/my-django-project.git
cd my-django-project
Create a virtual environment

python -m venv venv


2 Activate the virtual environment

Windows:

venv\Scripts\activate


Mac/Linux:

source venv/bin/activate


3 Install dependencies

pip install -r requirements.txt


(If requirements.txt doesn’t exist yet, generate it with pip freeze > requirements.txt.)

4 Apply migrations

python manage.py makemigrations
python manage.py migrate


5 Run the development server

python manage.py runserver


6 Open in browser

Navigate to http://127.0.0.1:8000/ to see the application.

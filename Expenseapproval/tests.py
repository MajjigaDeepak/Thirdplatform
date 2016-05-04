from django.test import TestCase,Client
from .models import *
from .views import *
from django.core.urlresolvers import reverse
from .forms import *
from django.core.urlresolvers import resolve
# Create your tests here.

class Signin_test(TestCase):

    def create_user(self):
         return Users.objects.create(username="deepak",password="deepak")

    def test_createuser(self):#User model test
        w=self.create_user()
        self.assertTrue(isinstance(w,Users))
        self.assertEquals(w.__str__(),w.username)

    def test_valid_userform(self):#User Form test--Positive test case
        w=Users.objects.create(username='deepak',password='deepak')
        form=UserForm(data={'username':w.username,'password':w.password})
        self.assertTrue(form.is_valid())

    def test_invalid_userform(self):#User Form test--Negative test case
        w=Users.objects.create(username='deepak',password='')
        form=UserForm(data={'username':w.username,'password':w.password})
        self.assertFalse(form.is_valid())

    #def test_user_view(self):
        #w=self.create_user()
        #url=reverse("login")
        #response=self.client.get(url)
        #self.assertEqual(response.status_code,200)
        #self.assertIn(w.username,response.content)


class add_expenses_test(TestCase):#Expense model test

    def create_expense(self):
        return Expenses.objects.create(employee_Name='Deepak',Category='Food',Date='2016-05-04',Ammount='500')

    def test_createexpense(self):
        x=self.create_expense()
        self.assertTrue(isinstance(x,Expenses))
        self.assertEquals(x.__str__(),x.employee_Name)

    def test_valid_expenseform(self):#Expenses Form test--Positive test case
        x=Expenses.objects.create(employee_Name='Deepak',Category='Food',Date='2016-05-04',Ammount='500')
        form=ExpenseForm(data={'employee_Name':x.employee_Name,'Category':x.Category,'Date':x.Date,'Ammount':x.Ammount})
        self.assertTrue(form.is_valid())

    #def test_expense_view(self):
        #x=self.create_expense()
        #url=reverse("addExpense")
        #response=self.client.get(url)
        #self.assertEqual(response.status_code,200)
        #self.assertIn(w.username,response.content)

    #def test_approver_view(self):
        #x=self.create_expense()
        #url=reverse("index")
        #response=self.client.get(url)
        #self.assertEqual(response.status_code,200)
        #self.assertIn(x.username,response.content)

class Loginpage(TestCase):

    def test_loginpage_response(self):
        found=resolve('/')
        self.assertEqual(found.func,login)

    def test_Signin_page(self):
        found=resolve('/adduser/')
        self.assertEqual(found.func,signin)

    def test_Expenseform_page(self):
        found=resolve('/Expenseform/')
        self.assertEqual(found.func,addExpense)

    def test_Approveform_page(self):
        found=resolve('/Approve/')
        self.assertEqual(found.func,index)









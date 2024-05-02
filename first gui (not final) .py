
import tkinter as tk
from tkinter import messagebox

class GUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Event Management System")
        self.geometry("400x300")

        self.label_employee = tk.Label(self, text="Add Employee")
        self.label_employee.pack()

        self.frame_employee = tk.Frame(self)
        self.frame_employee.pack()

        self.label_employee_name = tk.Label(self.frame_employee, text="Name:")
        self.label_employee_name.grid(row=0, column=0)
        self.entry_employee_name = tk.Entry(self.frame_employee)
        self.entry_employee_name.grid(row=0, column=1)

        self.label_employee_id = tk.Label(self.frame_employee, text="Employee ID:")
        self.label_employee_id.grid(row=1, column=0)
        self.entry_employee_id = tk.Entry(self.frame_employee)
        self.entry_employee_id.grid(row=1, column=1)

        self.label_department = tk.Label(self.frame_employee, text="Department:")
        self.label_department.grid(row=2, column=0)
        self.entry_department = tk.Entry(self.frame_employee)
        self.entry_department.grid(row=2, column=1)

        self.label_job_title = tk.Label(self.frame_employee, text="Job Title:")
        self.label_job_title.grid(row=3, column=0)
        self.entry_job_title = tk.Entry(self.frame_employee)
        self.entry_job_title.grid(row=3, column=1)

        self.label_basic_salary = tk.Label(self.frame_employee, text="Basic Salary:")
        self.label_basic_salary.grid(row=4, column=0)
        self.entry_basic_salary = tk.Entry(self.frame_employee)
        self.entry_basic_salary.grid(row=4, column=1)

        self.label_age = tk.Label(self.frame_employee, text="Age:")
        self.label_age.grid(row=5, column=0)
        self.entry_age = tk.Entry(self.frame_employee)
        self.entry_age.grid(row=5, column=1)

        self.label_date_of_birth = tk.Label(self.frame_employee, text="Date of Birth:")
        self.label_date_of_birth.grid(row=6, column=0)
        self.entry_date_of_birth = tk.Entry(self.frame_employee)
        self.entry_date_of_birth.grid(row=6, column=1)

        self.label_passport_details = tk.Label(self.frame_employee, text="Passport Details:")
        self.label_passport_details.grid(row=7, column=0)
        self.entry_passport_details = tk.Entry(self.frame_employee)
        self.entry_passport_details.grid(row=7, column=1)

        self.button_add_employee = tk.Button(self, text="Add Employee", command=self.add_employee)
        self.button_add_employee.pack()

        self.label_client = tk.Label(self, text="Add Client")
        self.label_client.pack()

        self.frame_client = tk.Frame(self)
        self.frame_client.pack()

        self.label_client_name = tk.Label(self.frame_client, text="Name:")
        self.label_client_name.grid(row=0, column=0)
        self.entry_client_name = tk.Entry(self.frame_client)
        self.entry_client_name.grid(row=0, column=1)

        self.label_client_id = tk.Label(self.frame_client, text="Client ID:")
        self.label_client_id.grid(row=1, column=0)
        self.entry_client_id = tk.Entry(self.frame_client)
        self.entry_client_id.grid(row=1, column=1)

        self.label_client_address = tk.Label(self.frame_client, text="Address:")
        self.label_client_address.grid(row=2, column=0)
        self.entry_client_address = tk.Entry(self.frame_client)
        self.entry_client_address.grid(row=2, column=1)

        self.label_client_contact = tk.Label(self.frame_client, text="Contact Details:")
        self.label_client_contact.grid(row=3, column=0)
        self.entry_client_contact = tk.Entry(self.frame_client)
        self.entry_client_contact.grid(row=3, column=1)

        self.label_client_budget = tk.Label(self.frame_client, text="Budget:")
        self.label_client_budget.grid(row=4, column=0)
        self.entry_client_budget = tk.Entry(self.frame_client)
        self.entry_client_budget.grid(row=4, column=1)

        self.button_add_client = tk.Button(self, text="Add Client", command=self.add_client)
        self.button_add_client.pack()

    def add_employee(self):
        name = self.entry_employee_name.get()
        employee_id = int(self.entry_employee_id.get())
        department = self.entry_department.get()
        job_title = self.entry_job_title.get()
        basic_salary = float(self.entry_basic_salary.get())
        age = int(self.entry_age.get())
        date_of_birth = self.entry_date_of_birth.get()
        passport_details = self.entry_passport_details.get()

        # Now you have all the input values, you can create an Employee object or perform further actions
        # For now, let's just print the details
        print("Employee Details:")
        print("Name:", name)
        print("Employee ID:", employee_id)
        print("Department:", department)
        print("Job Title:", job_title)
        print("Basic Salary:", basic_salary)
        print("Age:", age)
        print("Date of Birth:", date_of_birth)
        print("Passport Details:", passport_details)

        # Optionally, you can clear the entry fields after adding an employee
        self.clear_employee_entries()

    def clear_employee_entries(self):
        # Clear all the entry fields related to adding an employee
        self.entry_employee_name.delete(0, tk.END)
        self.entry_employee_id.delete(0, tk.END)
        self.entry_department.delete(0, tk.END)
        self.entry_job_title.delete(0, tk.END)
        self.entry_basic_salary.delete(0, tk.END)
        self.entry_age.delete(0, tk.END)
        self.entry_date_of_birth.delete(0, tk.END)
        self.entry_passport_details.delete(0, tk.END)

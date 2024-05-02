import pickle
# Define Employee class
class Employee:
    def __init__(self, name, employee_id, department, job_title, basic_salary, age, date_of_birth, passport_details, manager=None):
        assert isinstance(name, str), "Name must be a string"
        assert isinstance(employee_id, int), "Employee ID must be an integer"
        assert isinstance(department, str), "Department must be a string"
        self.name = name
        self.employee_id = employee_id
        self.department = department
        self.job_title = job_title
        self.basic_salary = basic_salary
        self.age = age
        self.date_of_birth = date_of_birth
        self.passport_details = passport_details
        self.manager = manager

    def calculate_salary(self):
        # Calculate salary based on specific rules for each type of employee
        raise NotImplementedError("Subclass must implement abstract method")

    def display_details(self):
        print("Employee ID:", self.employee_id)
        print("Name:", self.name)
        print("Department:", self.department)
        print("Job Title:", self.job_title)
        print("Basic Salary:", self.basic_salary)
        print("Age:", self.age)
        print("Date of Birth:", self.date_of_birth)
        print("Passport Details:", self.passport_details)
        if self.manager:
            print("Manager:", self.manager.name)

class SalesManager(Employee):
    def __init__(self, name, employee_id, department, job_title, basic_salary, age, date_of_birth, passport_details, sales_target):
        super().__init__(name, employee_id, department, job_title, basic_salary, age, date_of_birth, passport_details)
        self.sales_target = sales_target

    def calculate_salary(self):
        # Calculate salary for a Sales Manager
        # Example: Basic Salary + Commission based on achieving sales target
        pass

class Salesperson(Employee):
    def __init__(self, name, employee_id, department, job_title, basic_salary, age, date_of_birth, passport_details, sales_performance):
        super().__init__(name, employee_id, department, job_title, basic_salary, age, date_of_birth, passport_details)
        self.sales_performance = sales_performance

    def calculate_salary(self):
        # Calculate salary for a Salesperson
        # Example: Basic Salary + Commission based on sales performance
        pass

class MarketingManager(Employee):
    def __init__(self, name, employee_id, department, job_title, basic_salary, age, date_of_birth, passport_details, marketing_strategy):
        super().__init__(name, employee_id, department, job_title, basic_salary, age, date_of_birth, passport_details)
        self.marketing_strategy = marketing_strategy

class Marketer(Employee):
    def __init__(self, name, employee_id, department, job_title, basic_salary, age, date_of_birth, passport_details, marketing_campaign):
        super().__init__(name, employee_id, department, job_title, basic_salary, age, date_of_birth, passport_details)
        self.marketing_campaign = marketing_campaign

class Accountant(Employee):
    def __init__(self, name, employee_id, department, job_title, basic_salary, age, date_of_birth, passport_details, certifications):
        super().__init__(name, employee_id, department, job_title, basic_salary, age, date_of_birth, passport_details)
        self.certifications = certifications

class Designer(Employee):
    def __init__(self, name, employee_id, department, job_title, basic_salary, age, date_of_birth, passport_details, design_specialization):
        super().__init__(name, employee_id, department, job_title, basic_salary, age, date_of_birth, passport_details)
        self.design_specialization = design_specialization

class Handyman(Employee):
    def __init__(self, name, employee_id, department, job_title, basic_salary, age, date_of_birth, passport_details, skills):
        super().__init__(name, employee_id, department, job_title, basic_salary, age, date_of_birth, passport_details)
        self.skills = skills


# Define Client class
class Client:
    def __init__(self, client_id, name, address, contact_details, budget):
        self.client_id = client_id
        self.name = name
        self.address = address
        self.contact_details = contact_details
        self.budget = budget

    def display_details(self):
        print("Client ID:", self.client_id)
        print("Name:", self.name)
        print("Address:", self.address)
        print("Contact Details:", self.contact_details)
        print("Budget:", self.budget)

# Define Guest class
class Guest:
    def __init__(self, guest_id, name, address, contact_details):
        self.guest_id = guest_id
        self.name = name
        self.address = address
        self.contact_details = contact_details

    def display_details(self):
        print("Guest ID:", self.guest_id)
        print("Name:", self.name)
        print("Address:", self.address)
        print("Contact Details:", self.contact_details)


# Define Venue class
class Venue:
    def __init__(self, venue_id, name, address, contact, min_guests, max_guests):
        self.venue_id = venue_id
        self.name = name
        self.address = address
        self.contact = contact
        self.min_guests = min_guests
        self.max_guests = max_guests

    def display_details(self):
        print("Venue ID:", self.venue_id)
        print("Name:", self.name)
        print("Address:", self.address)
        print("Contact:", self.contact)
        print("Minimum Guests:", self.min_guests)
        print("Maximum Guests:", self.max_guests)

    def book_venue(self):
        pass

# Define Supplier class
class Supplier:
    def __init__(self, supplier_id, name, address, contact_details):
        self.supplier_id = supplier_id
        self.name = name
        self.address = address
        self.contact_details = contact_details

    def display_details(self):
        print("Supplier ID:", self.supplier_id)
        print("Name:", self.name)
        print("Address:", self.address)
        print("Contact Details:", self.contact_details)

# Define Event class
class Event:
    def __init__(self, event_id, type, theme, date, time, duration, venue, client, guests, catering_company,
                 cleaning_company, decorations_company, entertainment_company, furniture_company, invoice):
        self.event_id = event_id
        self.type = type
        self.theme = theme
        self.date = date
        self.time = time
        self.duration = duration
        self.venue = venue
        self.client = client
        self.guests = guests
        self.catering_company = catering_company
        self.cleaning_company = cleaning_company
        self.decorations_company = decorations_company
        self.entertainment_company = entertainment_company
        self.furniture_company = furniture_company
        self.invoice = invoice

    def display_details(self):
        print("Event ID:", self.event_id)
        print("Type:", self.type)
        print("Theme:", self.theme)
        print("Date:", self.date)
        print("Time:", self.time)
        print("Duration:", self.duration)
        print("Venue:", self.venue.name)  # Assuming Venue object has a 'name' attribute
        print("Client:", self.client.name)  # Assuming Client object has a 'name' attribute
        print("Guests:")
        for guest in self.guests:
            print(" -", guest.name)  # Assuming Guest object has a 'name' attribute
        print("Catering Company:", self.catering_company.name)  # Assuming Supplier object has a 'name' attribute
        print("Cleaning Company:", self.cleaning_company.name)  # Assuming Supplier object has a 'name' attribute
        print("Decorations Company:", self.decorations_company.name)  # Assuming Supplier object has a 'name' attribute
        if self.entertainment_company is not None:
            print("Entertainment Company:", self.entertainment_company.name)  # Assuming Supplier object has a 'name' attribute
        else:
            print("Entertainment Company: None")
        print("Furniture Company:", self.furniture_company.name)  # Assuming Supplier object has a 'name' attribute
        print("Invoice:", self.invoice)


# Create objects for Employee class
susan = SalesManager("Susan Meyers",47899, "Sales", "Manager", 37500, 40, "1984-05-15", "AB123456", sales_target=None)
shyam = Salesperson("Shyam Sundar", 11234, "Sales", "Salesperson", 20000, 30, "1992-10-20", "CD789012", susan)
salma = Salesperson("Salma J Sam", 98637, "Sales", "Salesperson", 20000, 28, "1994-03-25", "EF345678", susan)
# Create objects for Employee class
joy = MarketingManager("Joy Rogers", 81774, "sales", "Manager", 24000, 35, "1989-08-10", "GH901234", marketing_strategy=None)
mariam = Marketer("Mariam Khalid", 98394, "sales", "salesperson", 20000, 27, "1995-12-05", "IJ567890", joy)

# Create objects for Client class
client1 = Client(1, "ABC Corporation", "123 Main St", "123-456-7890", 5000.00)
client2 = Client(2, "XYZ Enterprises", "456 Oak Ave", "987-654-3210", 8000.00)

# Create objects for Guest class
guest1 = Guest(1, "shaikha", "789 Elm St", "456-789-0123")
guest2 = Guest(2, "meera", "567 Maple Ave", "789-012-3456")

# Create objects for Venue class
venue1 = Venue(1, "Grand Ballroom", "789 Elm St", "123-456-7890", 100, 500)
venue2 = Venue(2, "Garden Pavilion", "456 Oak Ave", "987-654-3210", 50, 200)

# Create objects for Supplier class
caterer = Supplier(1, "Delicious Catering", "111 Catering St", "111-222-3333")
cleaner = Supplier(2, "Sparkling Cleaners", "222 Cleaning Ave", "444-555-6666")
decorator = Supplier(3, "Fantastic Decor", "333 Decor Dr", "777-888-9999")

entertainment_company = Supplier(4, "Entertainment Co.", "444 Entertainment St", "555-666-7777")
furniture_company = Supplier(5, "Furniture Co.", "555 Furniture Ave", "888-999-0000")

event1 = Event(1, "Wedding", "Romantic", "2024-05-15", "18:00", 4, venue1, client1, [guest1, guest2], caterer, cleaner, decorator, entertainment_company, furniture_company, 10000.00)
event2 = Event(2, "Birthday", "Fun", "2024-06-20", "15:00", 3, venue2, client2, [guest1], caterer, cleaner, decorator, entertainment_company, furniture_company, 8000.00)

with open("employee_data.pkl", "wb") as file:
    pickle.dump([susan, shyam, salma, joy, mariam], file)

# Save client details to a binary file
with open("client_data.pkl", "wb") as file:
    pickle.dump([client1, client2], file)

# Save guest details to a binary file
with open("guest_data.pkl", "wb") as file:
    pickle.dump([guest1, guest2], file)

# Save venue details to a binary file
with open("venue_data.pkl", "wb") as file:
    pickle.dump([venue1, venue2], file)

# Save supplier details to a binary file
with open("supplier_data.pkl", "wb") as file:
    pickle.dump([caterer, cleaner, decorator, entertainment_company, furniture_company], file)

# Save event details to a binary file
with open("event_data.pkl", "wb") as file:
    pickle.dump([event1, event2], file)

# Print details of Employee objects
print("--- Employee Details ---")
susan.display_details()
shyam.display_details()
salma.display_details()
joy.display_details()
mariam.display_details()

# Print details of Client objects
print("\n--- Client Details ---")
client1.display_details()
client2.display_details()

# Print details of Guest objects
print("\n--- Guest Details ---")
guest1.display_details()
guest2.display_details()

# Print details of Venue objects
print("\n--- Venue Details ---")
venue1.display_details()
venue2.display_details()

# Print details of Supplier objects
print("\n--- Supplier Details ---")
caterer.display_details()
cleaner.display_details()
decorator.display_details()

# Print details of Event objects
print("\n--- Event Details ---")
event1.display_details()
event2.display_details()



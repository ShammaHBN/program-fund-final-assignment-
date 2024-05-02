import tkinter as tk

class EmployeeManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee Management System")

        # Tabs/Sections
        self.tabs = ["Employees", "Events", "Clients", "Guests", "Suppliers", "Venues"]
        self.current_tab = tk.StringVar(value=self.tabs[0])

        self.create_widgets()

    def create_widgets(self):
        # Tab Selection
        tab_frame = tk.Frame(self.root)
        tab_frame.pack()
        for tab in self.tabs:
            tk.Radiobutton(tab_frame, text=tab, variable=self.current_tab, value=tab).pack(side=tk.LEFT)

        # ID Input Field
        id_frame = tk.Frame(self.root)
        id_frame.pack()
        tk.Label(id_frame, text="ID Number:").pack(side=tk.LEFT)
        self.id_entry = tk.Entry(id_frame)
        self.id_entry.pack(side=tk.LEFT)

        # Buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack()
        actions = ["Add", "Delete", "Modify", "Display"]
        for action in actions:
            tk.Button(button_frame, text=action, command=lambda a=action.lower(): self.perform_action(a)).pack(side=tk.LEFT)

        # Display Area
        self.display_area = tk.Text(self.root, height=10, width=50)
        self.display_area.pack()

    def perform_action(self, action):
        current_tab = self.current_tab.get()
        id_number = self.id_entry.get()

        if action == "add":
            self.display_area.insert(tk.END, f"Adding {current_tab} with ID {id_number}\n")
            # Add functionality goes here

        elif action == "delete":
            self.display_area.insert(tk.END, f"Deleting {current_tab} with ID {id_number}\n")
            # Delete functionality goes here

        elif action == "modify":
            self.display_area.insert(tk.END, f"Modifying {current_tab} with ID {id_number}\n")
            # Modify functionality goes here

        elif action == "display":
            self.display_area.insert(tk.END, f"Displaying details of {current_tab} with ID {id_number}\n")
            # Display functionality goes here
            # You can display the details in the text area or in a separate window

if __name__ == "__main__":
    root = tk.Tk()
    app = EmployeeManagementApp(root)
    root.mainloop()

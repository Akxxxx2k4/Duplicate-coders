import time
import winsound
import tkinter as tk
from tkinter import messagebox

def set_medicine_reminder(reminder_time, medicine_name):
    while True:
        current_time = time.strftime("%H:%M")
        if current_time == reminder_time:
            messagebox.showinfo("Medicine Reminder", f"It's time to take your {medicine_name}!")
            winsound.Beep(1000, 2000)  # Beep sound
            break
        time.sleep(10)  # Check every minute

def set_appointment_reminder(appointment_time, doctor_name):
    while True:
        current_time = time.strftime("%H:%M")
        if current_time == appointment_time:
            messagebox.showinfo("Appointment Reminder", f"It's time for your appointment with Dr. {doctor_name}!")
            winsound.Beep(1000, 2000)  # Beep sound
            break
        time.sleep(10)  # Check every minute

def set_reminders():
    medicine_reminders = {}
    appointment_reminders = {}

    num_medicines = int(num_medicines_entry.get())
    for i in range(num_medicines):
        medicine_name = medicine_entries[i].get()
        reminder_time = reminder_entries[i].get()
        medicine_reminders[medicine_name] = reminder_time

    num_appointments = int(num_appointments_entry.get())
    for i in range(num_appointments):
        doctor_name = doctor_entries[i].get()
        appointment_time = appointment_entries[i].get()
        appointment_reminders[doctor_name] = appointment_time

    for medicine, time_value in medicine_reminders.items():
        set_medicine_reminder(time_value, medicine)

    for doctor, time_value in appointment_reminders.items():
        set_appointment_reminder(time_value, doctor)

# UI Setup
root = tk.Tk()
root.title("Reminder App")

# Styling
root.geometry("500x300")
root.configure(bg="#f0f0f0")

# Medicine Reminders Section
medicine_frame = tk.Frame(root, bg="#e0e0e0", padx=10, pady=10)
medicine_frame.pack(pady=10, fill="both", expand=True)

num_medicines_label = tk.Label(medicine_frame, text="Number of medicines:", bg="#e0e0e0")
num_medicines_label.grid(row=0, column=0)

num_medicines_entry = tk.Entry(medicine_frame)
num_medicines_entry.grid(row=0, column=1)

medicine_entries = []
reminder_entries = []

def add_medicine_fields():
    num = int(num_medicines_entry.get())
    for i in range(num):
        medicine_label = tk.Label(medicine_frame, text=f"Medicine {i+1}:", bg="#e0e0e0")
        medicine_label.grid(row=i+1, column=0)

        medicine_entry = tk.Entry(medicine_frame)
        medicine_entry.grid(row=i+1, column=1)
        medicine_entries.append(medicine_entry)

        reminder_label = tk.Label(medicine_frame, text="Reminder Time (HH:MM):", bg="#e0e0e0")
        reminder_label.grid(row=i+1, column=2)

        reminder_entry = tk.Entry(medicine_frame)
        reminder_entry.grid(row=i+1, column=3)
        reminder_entries.append(reminder_entry)

add_medicine_button = tk.Button(medicine_frame, text="Add Medicines", command=add_medicine_fields)
add_medicine_button.grid(row=0, column=2)

# Appointment Reminders Section
appointment_frame = tk.Frame(root, bg="#e0e0e0", padx=10, pady=10)
appointment_frame.pack(pady=10, fill="both", expand=True)

num_appointments_label = tk.Label(appointment_frame, text="Number of appointments:", bg="#e0e0e0")
num_appointments_label.grid(row=0, column=0)

num_appointments_entry = tk.Entry(appointment_frame)
num_appointments_entry.grid(row=0, column=1)

doctor_entries = []
appointment_entries = []

def add_appointment_fields():
    num = int(num_appointments_entry.get())
    for i in range(num):
        doctor_label = tk.Label(appointment_frame, text=f"Doctor {i+1}:", bg="#e0e0e0")
        doctor_label.grid(row=i+1, column=0)

        doctor_entry = tk.Entry(appointment_frame)
        doctor_entry.grid(row=i+1, column=1)
        doctor_entries.append(doctor_entry)

        appointment_label = tk.Label(appointment_frame, text="Appointment Time (HH:MM):", bg="#e0e0e0")
        appointment_label.grid(row=i+1, column=2)

        appointment_entry = tk.Entry(appointment_frame)
        appointment_entry.grid(row=i+1, column=3)
        appointment_entries.append(appointment_entry)

add_appointment_button = tk.Button(appointment_frame, text="Add Appointments", command=add_appointment_fields)
add_appointment_button.grid(row=0, column=2)

# Start Button
start_button = tk.Button(root, text="Start Reminders", command=set_reminders, bg="#4caf50", fg="white", padx=10, pady=5)
start_button.pack(pady=10)

root.mainloop()

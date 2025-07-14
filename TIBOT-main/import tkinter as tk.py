import tkinter as tk
from tkinter import messagebox
from customtkinter import CTk, CTkButton, CTkCheckBox, CTkLabel, CTkFrame, CTkEntry, set_appearance_mode, set_default_color_theme
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Función para iniciar sesión y abrir TikTok Live
def open_tiktok_live(account, password):
    driver = webdriver.Chrome()  # Asegúrate de tener el driver de Chrome instalado
    driver.get("https://www.tiktok.com/login")

    time.sleep(2)

    # Iniciar sesión
    username_input = driver.find_element(By.NAME, "username")
    password_input = driver.find_element(By.NAME, "password")
    username_input.send_keys(account)
    password_input.send_keys(password)
    password_input.send_keys(Keys.RETURN)

    time.sleep(5)

    # Abrir TikTok Live
    driver.get("https://www.tiktok.com/@" + account + "/live")

    time.sleep(5)

    # Recolectar monedas (esto puede variar dependiendo de la estructura de la página)
    try:
        coin_button = driver.find_element(By.XPATH, '//button[@aria-label="Coin"]')
        coin_button.click()
        messagebox.showinfo("Éxito", f"Monedas recolectadas para {account}")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudieron recolectar monedas para {account}: {e}")

    driver.quit()

# Función para manejar la selección de cuentas
def select_accounts():
    accounts = []
    passwords = []
    for i in range(len(account_entries)):
        account = account_entries[i].get()
        password = password_entries[i].get()
        if account and password:
            accounts.append(account)
            passwords.append(password)
    if not accounts:
        messagebox.showwarning("Advertencia", "Por favor, ingresa al menos una cuenta.")
        return

    for account, password in zip(accounts, passwords):
        open_tiktok_live(account, password)

# Crear la interfaz gráfica
set_appearance_mode("dark")  # Modo oscuro
set_default_color_theme("blue")  # Tema azul

app = CTk()
app.title("Seleccionar Cuentas de TikTok")
app.geometry("400x500")

frame = CTkFrame(master=app)
frame.pack(pady=20, padx=20, fill="both", expand=True)

account_entries = []
password_entries = []

for i in range(5):  # Permitimos hasta 5 cuentas
    account_label = CTkLabel(master=frame, text=f"Cuenta {i+1}:")
    account_label.grid(row=i*2, column=0, sticky="w", pady=5)
    account_entry = CTkEntry(master=frame)
    account_entry.grid(row=i*2, column=1, pady=5)
    account_entries.append(account_entry)

    password_label = CTkLabel(master=frame, text=f"Contraseña {i+1}:")
    password_label.grid(row=i*2+1, column=0, sticky="w", pady=5)
    password_entry = CTkEntry(master=frame, show="*")
    password_entry.grid(row=i*2+1, column=1, pady=5)
    password_entries.append(password_entry)

start_button = CTkButton(master=frame, text="Iniciar", command=select_accounts)
start_button.grid(row=11, column=0, columnspan=2, pady=20)

app.mainloop()
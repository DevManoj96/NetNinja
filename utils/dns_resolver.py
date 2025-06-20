# dns_resolver.py

import socket
import threading
import tkinter as tk
from tkinter import messagebox, scrolledtext
from theme.theme import DARK_THEME

def launch_dns_resolver():
    dns_win = tk.Toplevel()
    dns_win.title("DNS Resolver")
    dns_win.geometry("550x550")
    
    dns_win.config(bg=DARK_THEME["bg"])

    tk.Label(dns_win, text="Enter Domain or IP:", font=("Arial", 12), bg=DARK_THEME["bg"], fg=DARK_THEME["fg"]).pack(pady=5)
    
    input_entry = tk.Entry(dns_win, font=("Arial", 12), width=40, bg=DARK_THEME["button_bg"], fg=DARK_THEME["entry_fg"], insertbackground=DARK_THEME["highlight"])
    input_entry.pack(pady=5)

    result_box = scrolledtext.ScrolledText(dns_win, font=("Consolas", 11), width=70, height=15, bg=DARK_THEME["entry_bg"], fg=DARK_THEME["entry_fg"], insertbackground=DARK_THEME["highlight"], selectbackground="#404040")
    result_box.pack(pady=10)
    result_box.config(state='disabled')




    
    def resolve():
        value = input_entry.get().strip()
        result_box.delete(1.0, tk.END)

        if not value:
            messagebox.showerror("Error", "Please enter a domain or IP.")
            return

        try:
            result_box.config(state='normal')
            if all(c.isdigit() or c == '.' for c in value):
                # IP address → domain
                domain = socket.gethostbyaddr(value)
                result_box.insert(tk.END, f"🧠 Reverse DNS:\n{domain}\n")
            else:
                # Domain → IP
                ip = socket.gethostbyname(value)
                result_box.insert(tk.END, f"🌐 IP Address:\n{ip}\n")

                result_box.config(state='disabled')
        except Exception as e:
            messagebox.showerror("Error", f"DNS resolution failed:\n{e}")

    def start_dns_resolver_thread():
        threading.Thread(target=resolve).start()

    tk.Button(dns_win, text="Resolve", font=("Arial", 12), command=start_dns_resolver_thread, width=10, height=1, bg=DARK_THEME["button_bg"], fg=DARK_THEME["button_fg"], activebackground="#3d3d3d", activeforeground=DARK_THEME["highlight"]).pack(pady=5)

    tk.Button(dns_win, text="Done", font=("Arial", 12), command=dns_win.destroy, width=10, height=1, bg=DARK_THEME["button_bg"], fg=DARK_THEME["button_fg"], activebackground="#3d3d3d", activeforeground=DARK_THEME["highlight"]).pack(pady=5)


import threading
import whois
import tkinter as tk
from tkinter import messagebox, scrolledtext
from theme.theme import DARK_THEME

def launch_whois_lookup():
    whois_win = tk.Toplevel()
    whois_win.title("Whois Lookup")
    whois_win.geometry("550x550")

    whois_win.config(bg=DARK_THEME["bg"])

    tk.Label(whois_win, text="Enter Domain (e.g., google.com):", font=("Arial", 12), bg=DARK_THEME["bg"], fg=DARK_THEME["fg"]).pack(pady=5)

    domain_entry = tk.Entry(whois_win, font=("Arial", 12), width=40, bg=DARK_THEME["button_bg"], fg=DARK_THEME["entry_fg"], insertbackground=DARK_THEME["highlight"])
    domain_entry.pack(pady=5)

    result_box = scrolledtext.ScrolledText(whois_win, font=("Consolas", 11), width=70, height=20, bg=DARK_THEME["entry_bg"], fg=DARK_THEME["entry_fg"], insertbackground=DARK_THEME["highlight"], selectbackground="#404040")
    result_box.pack(pady=10)
    result_box.config(state='disabled')

    def lookup():
        domain = domain_entry.get().strip()
        result_box.delete(1.0, tk.END)

        if not domain:
            messagebox.showerror("Error", "Please enter a domain.")
            return

        try:
            result_box.config(state='normal')
            info = whois.whois(domain)
            result_box.insert(tk.END, f"Domain: {domain}\n")
            
            for key, value in info.items():
                result_box.insert(tk.END, f"{key}: {value}\n")
                
            result_box.config(state='disabled')
            
        except Exception as e:
            messagebox.showerror("Error", f"Whois lookup failed:\n{e}")

    def start_whois_lookup_thread():
        threading.Thread(target=lookup).start()
        
    tk.Button(whois_win, text="Lookup", font=("Arial", 12), command=start_whois_lookup_thread, width=10, height=1, bg=DARK_THEME["button_bg"], fg=DARK_THEME["button_fg"], activebackground="#3d3d3d", activeforeground=DARK_THEME["highlight"]).pack(pady=5)

    tk.Button(whois_win, text="Done", font=("Arial", 12), command=whois_win.destroy, width=10, height=1, bg=DARK_THEME["button_bg"], fg=DARK_THEME["button_fg"], activebackground="#3d3d3d", activeforeground=DARK_THEME["highlight"]).pack(pady=5)


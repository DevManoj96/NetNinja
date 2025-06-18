# ip_geo_lookup.py

import threading
import requests
import tkinter as tk
from tkinter import messagebox, scrolledtext
from theme.theme import DARK_THEME

def launch_ip_geo_lookup():
    ip_geo_win = tk.Toplevel()
    ip_geo_win.title("IP Geolocation Lookup")
    ip_geo_win.geometry("550x550")

    ip_geo_win.config(bg=DARK_THEME["bg"])

    tk.Label(ip_geo_win, text="Enter IP or Domain:", font=("Arial", 12), bg=DARK_THEME["bg"], fg=DARK_THEME["fg"]).pack(pady=5)
    ip_entry = tk.Entry(ip_geo_win, font=("Arial", 12), width=40, bg=DARK_THEME["button_bg"], fg=DARK_THEME["entry_fg"], insertbackground=DARK_THEME["highlight"])
    ip_entry.pack(pady=5)

    result_box = scrolledtext.ScrolledText(ip_geo_win, font=("Consolas", 11), width=70, height=18, bg=DARK_THEME["entry_bg"], fg=DARK_THEME["entry_fg"], insertbackground=DARK_THEME["highlight"], selectbackground="#404040")
    result_box.pack(pady=10)
    result_box.config(state='disabled')

    def lookup():
        ip = ip_entry.get().strip()
        result_box.delete(1.0, tk.END)

        if not ip:
            messagebox.showerror("Error", "Please enter an IP address or domain.")
            return

        try:
            result_box.config(state='normal')
            response = requests.get(f"http://ip-api.com/json/{ip}")
            data = response.json()

            if data['status'] == 'fail':
                result_box.insert(tk.END, f"❌ Error: {data['message']}")
                return

            result = f"""
🛰️ IP Geolocation Lookup

IP: {data.get('query')}
ISP: {data.get('isp')}
Org: {data.get('org')}
Country: {data.get('country')}
Region: {data.get('regionName')}
City: {data.get('city')}
Timezone: {data.get('timezone')}
Latitude: {data.get('lat')}
Longitude: {data.get('lon')}
        """.strip()

            result_box.insert(tk.END, result)
            result_box.config(state='disabled')

        except Exception as e:
            messagebox.showerror("Error", f"Request failed:\n{e}")

    def start_ip_geo_thread():
        threading.Thread(target=lookup).start()

    tk.Button(ip_geo_win, text="Lookup", font=("Arial", 12), command=start_ip_geo_thread, width=10, height=1, bg=DARK_THEME["button_bg"], fg=DARK_THEME["button_fg"], activebackground="#3d3d3d", activeforeground=DARK_THEME["highlight"]).pack(pady=5)

    tk.Button(ip_geo_win, text="Done", font=("Arial", 12), command=ip_geo_win.destroy, width=10, height=1,  bg=DARK_THEME["button_bg"], fg=DARK_THEME["button_fg"], activebackground="#3d3d3d", activeforeground=DARK_THEME["highlight"]).pack(pady=5)



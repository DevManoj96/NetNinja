import socket
import threading
import tkinter as tk
from tkinter import messagebox, scrolledtext
from tkinter import font
from utils.theme import DARK_THEME

def launch_port_scanner():
    scanner_win = tk.Toplevel()
    scanner_win.title("Port Scanner")
    scanner_win.geometry("550x550")

    scanner_win.config(bg=DARK_THEME["bg"])

    tk.Label(scanner_win, text="Target Host:", font=("Arial", 12), bg=DARK_THEME["bg"], fg=DARK_THEME["fg"]).pack(pady=5)

    host_entry = tk.Entry(scanner_win, font=("Arial", 12), bg=DARK_THEME["button_bg"], fg=DARK_THEME["entry_fg"], insertbackground=DARK_THEME["highlight"])
    host_entry.pack(pady=5)
    host_entry.insert(0, "127.0.0.1")

    tk.Label(scanner_win, text="Start Port:", font=("Arial", 12), bg=DARK_THEME["bg"], fg=DARK_THEME["fg"]).pack(pady=5)

    start_port_entry = tk.Entry(scanner_win, font=("Arial", 12), bg=DARK_THEME["button_bg"], fg=DARK_THEME["entry_fg"], insertbackground=DARK_THEME["highlight"])
    start_port_entry.pack(pady=5)
    start_port_entry.insert(0, "1")

    tk.Label(scanner_win, text="End Port:", font=("Arial", 12), bg=DARK_THEME["bg"], fg=DARK_THEME["fg"]).pack(pady=5)

    end_port_entry = tk.Entry(scanner_win, font=("Arial", 12), bg=DARK_THEME["button_bg"], fg=DARK_THEME["entry_fg"], insertbackground=DARK_THEME["highlight"])
    end_port_entry.pack(pady=5)
    end_port_entry.insert(0, "1000")

    result_box = scrolledtext.ScrolledText(scanner_win, width=70, height=12, bg=DARK_THEME["entry_bg"], fg=DARK_THEME["entry_fg"], insertbackground=DARK_THEME["highlight"], selectbackground="#404040", font=("Consolas", 11))
    result_box.pack(pady=10)
    result_box.config(state='disabled')
    

    def scanner():
        target = host_entry.get().strip()
        try:
            start_port = int(start_port_entry.get().strip())
            end_port = int(end_port_entry.get().strip())
        except ValueError:
            messagebox.showerror("Error", "Invalid port range.")
            return

        if not target:
            messagebox.showerror("Error", "Host cannot be empty.")
            return

        result_box.config(state='normal')
        result_box.delete(1.0, tk.END)
        result_box.insert(tk.END, f"🔍 Scanning {target} from port {start_port} to {end_port}...\n")

        for port in range(start_port, end_port + 1):
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(0.5)
                result = s.connect_ex((target, port))
                if result == 0:
                    result_box.insert(tk.END, f"[+] Port {port} is OPEN\n")
                s.close()
            except Exception as e:
                result_box.insert(tk.END, f"[!] Error on port {port}: {e}\n")

        result_box.insert(tk.END, "\n✅ Scan complete.")
        result_box.config(state='disabled')

    def start_port_scanner_thread():
        threading.Thread(target=scanner).start()


    tk.Button(scanner_win, text="Scan", font=("Arial", 12), command=start_port_scanner_thread, width=10, height=1, bg=DARK_THEME["button_bg"], fg=DARK_THEME["button_fg"], activebackground="#3d3d3d", activeforeground=DARK_THEME["highlight"]).pack(pady=5)

    tk.Button(scanner_win, text="Done", font=("Arial", 12), command=scanner_win.destroy, width=10, height=1, bg=DARK_THEME["button_bg"], fg=DARK_THEME["button_fg"], activebackground="#3d3d3d", activeforeground=DARK_THEME["highlight"]).pack(pady=5)



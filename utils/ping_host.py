import subprocess
import threading
import tkinter as tk
from tkinter import messagebox
import platform
from utils.theme import DARK_THEME


def launch_ping_host():
    ping_win = tk.Toplevel()
    ping_win.title("--- Ping Host ---")
    ping_win.geometry("550x550")

    ping_win.config(bg=DARK_THEME["bg"])

    tk.Label(ping_win, text="Enter Host/IP:", font=("Arial", 12), bg=DARK_THEME["bg"], fg=DARK_THEME["fg"]).pack(pady=5)

    host_input = tk.Entry(ping_win, font=("Arial", 12), bg=DARK_THEME["button_bg"], fg=DARK_THEME["entry_fg"], insertbackground=DARK_THEME["highlight"])
    host_input.pack(pady=5)
    host_input.insert(0, "127.0.0.1")

    ping_label = tk.Label(ping_win, text="", font=("Arial", 12), bg=DARK_THEME["bg"], fg=DARK_THEME["fg"])
    ping_label.pack(pady=5)

    listbox = tk.Listbox(ping_win, width=60, height=15, bg=DARK_THEME["entry_bg"], fg=DARK_THEME["entry_fg"], selectbackground="#404040", selectforeground=DARK_THEME["highlight"], highlightbackground=DARK_THEME["bg"], highlightcolor=DARK_THEME["highlight"], activestyle='none', font=("Consolas", 11))
    listbox.pack(pady=5)
        
    def run_ping():
        host = host_input.get().strip()
        listbox.delete(0, tk.END)

        if not host:
            messagebox.showinfo("Ping", "⚠️  Host cannot be empty.")
            return

        param = "-n" if platform.system().lower() == "windows" else "-c"
        ping_label.config(text=f"📡 Pinging {host}...\n")

        try:
            result = subprocess.run(
                ["ping", param, "4", host],
                capture_output=True,
                text=True
            )

            output_lines = result.stdout.splitlines()
                
            def update_gui():
                listbox.delete(0, tk.END)
                for line in output_lines:
                    listbox.insert(tk.END, line)
                ping_label.config(text=f"📡 Done Pinging.")
                
                listbox.bind("<Button-1>", lambda e: "break")  
                listbox.bind("<Key>", lambda e: "break")


            ping_win.after(0, update_gui)

        except Exception as e:
            messagebox.showerror("Error", f"❌ {e}")
            
    def start_ping_thread():
        threading.Thread(target=run_ping).start()    
    

    tk.Button(ping_win, text="Ping", command=start_ping_thread, font=("Arial", 12), width=10, height=1, bg=DARK_THEME["button_bg"], fg=DARK_THEME["button_fg"], activebackground="#3d3d3d", activeforeground=DARK_THEME["highlight"]).pack(pady=5)

    tk.Button(ping_win, text="Done", command=ping_win.destroy, font=("Arial", 12), width=10, height=1, bg=DARK_THEME["button_bg"], fg=DARK_THEME["button_fg"], activebackground="#3d3d3d", activeforeground=DARK_THEME["highlight"]).pack(pady=5)



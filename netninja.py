import tkinter as tk
from tkinter import messagebox

from theme.theme import DARK_THEME
from utils.port_scanner import launch_port_scanner
from utils.whois_lookup import launch_whois_lookup
from utils.dns_resolver import launch_dns_resolver
from utils.ip_geo_lookup import launch_ip_geo_lookup
from utils.ping_host import launch_ping_host


class NetToolKit:
    def __init__(self, root):

        self.root = root
        self.root.title("--- NetNinja ---")
        self.root.geometry('640x480')
        self.root.resizable(True, True)


        self.open_windows = []

        self.menubar = tk.Menu(self.root)

        filemenu = tk.Menu(self.menubar, tearoff=0)

        filemenu.add_command(label="About", command=self.show_about)

        self.menubar.add_cascade(label="Options", menu=filemenu)

        self.root.config(menu=self.menubar)

        self.root.config(bg=DARK_THEME["bg"])

        buttons_frame = tk.Frame(self.root, padx=50, pady=50, bg=DARK_THEME["bg"])
        buttons_frame.pack()

        ping_btn = tk.Button(buttons_frame, text="Ping Host", command=self.ping_host, font=("Arial", 12), width=20, height=2, bg=DARK_THEME["button_bg"], fg=DARK_THEME["button_fg"], activebackground="#3d3d3d", activeforeground=DARK_THEME["highlight"])
        ping_btn.grid(row=0, column=0, pady=5)

        port_scn_btn = tk.Button(buttons_frame, text="Port Scanner", command=self.port_scanner, font=("Arial", 12), width=20, height=2, bg=DARK_THEME["button_bg"], fg=DARK_THEME["button_fg"], activebackground="#3d3d3d", activeforeground=DARK_THEME["highlight"])
        port_scn_btn.grid(row=1, column=0, pady=5)

        whois_lkup_btn = tk.Button(buttons_frame, text="Whois Lookup", command=self.whois_lookup, font=("Arial", 12), width=20, height=2, bg=DARK_THEME["button_bg"], fg=DARK_THEME["button_fg"], activebackground="#3d3d3d", activeforeground=DARK_THEME["highlight"])
        whois_lkup_btn.grid(row=2, column=0, pady=5)

        dns_reslv_btn = tk.Button(buttons_frame, text="DNS Resolver", command=self.dns_resolver, font=("Arial", 12), width=20, height=2, bg=DARK_THEME["button_bg"], fg=DARK_THEME["button_fg"], activebackground="#3d3d3d", activeforeground=DARK_THEME["highlight"])
        dns_reslv_btn.grid(row=3, column=0, pady=5)

        ip_geo_lkup_btn = tk.Button(buttons_frame, text="IP Geo Lookup", command=self.ip_geo_lookup, font=("Arial", 12), width=20, height=2, bg=DARK_THEME["button_bg"], fg=DARK_THEME["button_fg"], activebackground="#3d3d3d", activeforeground=DARK_THEME["highlight"])
        ip_geo_lkup_btn.grid(row=4, column=0, pady=5)

        exit_btn = tk.Button(buttons_frame, text="Exit", command=self.root.quit, font=("Arial", 12), width=20, height=2, bg=DARK_THEME["button_bg"], fg=DARK_THEME["button_fg"], activebackground="#3d3d3d", activeforeground=DARK_THEME["highlight"])
        exit_btn.grid(row=5, column=0, pady=5)

    def ping_host(self):
        launch_ping_host()

    def port_scanner(self):
        launch_port_scanner()


    def whois_lookup(self):
        launch_whois_lookup()


    def dns_resolver(self):
        launch_dns_resolver()


    def ip_geo_lookup(self):
        launch_ip_geo_lookup()

    def show_about(self):
        
        about_text = """NetNinja v1.0

    A comprehensive network toolkit for network administrators, security professionals, and IT enthusiasts.

    Features:
    • Ping Host - Test network connectivity and response times
    • Port Scanner - Discover open ports and services on target hosts
    • Whois Lookup - Retrieve domain registration and ownership information
    • DNS Resolver - Resolve domain names to IP addresses and vice versa
    • IP Geo Lookup - Determine geographical location of IP addresses

    Technical Details:
    • Built with Python & Tkinter GUI framework
    • Cross-platform compatibility (Windows, macOS, Linux)
    • Dark theme interface for reduced eye strain
    • Modular architecture for easy maintenance and updates

    Usage:
    Perfect for network troubleshooting, security assessments, and general network administration tasks. Each tool opens in its own window for simultaneous use.

    Developed with Python & Tkinter
    © 2025 NetNinja - Network Security Toolkit"""

        messagebox.showinfo("About NetNinja", about_text)


if __name__ == '__main__':
    root = tk.Tk()
    app = NetToolKit(root)
    root.mainloop()
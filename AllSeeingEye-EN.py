import socket
import tkinter as tk
from tkinter import messagebox

def scan_ports(target):
    result_text.delete(1.0, tk.END)  
    result_text.insert(tk.END, f"Scanning ports on {target}...\n")
    
    open_ports = []  
    
    for port in range(1, 1025):  
        scanning_message = f"Scanning port {port}..."
        result_text.insert(tk.END, scanning_message)
        root.update()  
        
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  
        result = sock.connect_ex((target, port))
        
        result_text.delete(1.0, tk.END)  
        result_text.insert(tk.END, f"Scanning ports on {target}...\n")  
        
        if result == 0:
            open_ports.append(port)
            open_ports_text.insert(tk.END, f"Port {port}: OPEN\n")  
        sock.close()
        
    if open_ports:
        result_text.insert(tk.END, "Scan complete.\n")
    else:
        result_text.insert(tk.END, "No open ports found.\n")
    

def start_scan():
    target_ip = entry.get()
    if target_ip:
        open_ports_text.delete(1.0, tk.END)  
        scan_ports(target_ip)
    else:
        messagebox.showwarning("Input Error", "Please enter a valid IP address.")

# Configuração da interface gráfica
root = tk.Tk()
root.title("All Seeing Eye")

tk.Label(root, text="Enter IP Address or Domain:").pack(pady=10)
entry = tk.Entry(root, width=30)
entry.pack(pady=5)

scan_button = tk.Button(root, text="Start Scan", command=start_scan)
scan_button.pack(pady=10)

result_text = tk.Text(root, height=10, width=50)
result_text.pack(pady=10)

tk.Label(root, text="Open Ports Found:").pack(pady=10)
open_ports_text = tk.Text(root, height=10, width=50)
open_ports_text.pack(pady=10)

root.mainloop()

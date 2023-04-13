import tkinter as tk
import subprocess

def run_command(command):
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output = result.stdout.decode().strip()
    if output:
        output_area.insert(tk.END, output + "\n")
    error = result.stderr.decode().strip()
    if error:
        output_area.insert(tk.END, error + "\n", "error")

# Create GUI
root = tk.Tk()
root.title("WinTerm")
root.configure(bg="black")

# Create input area
input_area = tk.Entry(root, bg="white", fg="black", insertbackground="white")
input_area.grid(row=0, column=0, sticky="we", padx=5, pady=5)

# Create output area
output_area = tk.Text(root, bg="black", fg="white")
output_area.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
output_area.tag_config("error", foreground="red")

# Bind Enter key to run command
def on_enter(event):
    command = input_area.get().strip()
    input_area.delete(0, tk.END)
    output_area.insert(tk.END, f"$ {command}\n", "command")
    run_command(command)

root.bind("<Return>", on_enter)

# Set focus to input area
input_area.focus()

root.mainloop()

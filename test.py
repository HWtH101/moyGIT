import tkinter as tk

def main():
 
 root = tk.Tk()
 root.geometry("400x300") 

 
 label = tk.Label(root, text="Введи ключ и нажми ctrl+c")
 label.pack(pady=50)

 
 entry = tk.Entry(root)
 entry.pack(pady=50)

 
 root.mainloop()

if __name__ == "__main__":
 main()

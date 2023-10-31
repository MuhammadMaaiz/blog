import tkinter as tk
from tkinter import ttk, scrolledtext

blogs = []

root = tk.Tk()
root.title("Blog Application")
root.geometry("5000x5000")
root.configure(bg="light pink")

def add_blog():
    date = date_entry.get()
    title = title_entry.get()
    author = author_entry.get()
    content = content_text.get("1.0", tk.END)

    if not date or not title or not author or not content:
        return

    # Check if the content already exists in blogs
    content_exists = any(blog["Content"] == content for blog in blogs)

    if not content_exists:
        blog = {
            "Date": date,
            "Title": title,
            "Author": author,
            "Content": content
        }

        blogs.append(blog)
        clear_fields()
        update_second_page_content()

def clear_fields():
    date_entry.delete(0, tk.END)
    title_entry.delete(0, tk.END)
    author_entry.delete(0, tk.END)
    content_text.delete("1.0", tk.END)

def update_second_page_content():
    second_text.config(state=tk.NORMAL)
    second_text.delete(1.0, tk.END)
    
    for blog in blogs:
        second_text.insert(tk.END, f"Date: {blog['Date']} | ")
        second_text.insert(tk.END, f"Title: {blog['Title']} | ")
        second_text.insert(tk.END, f"Author: {blog['Author']}\n")
        second_text.insert(tk.END, "Content:\n")
        second_text.insert(tk.END, blog['Content'])
        second_text.insert(tk.END, "\n\n")
    
    second_text.config(state=tk.DISABLED)

notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both")

input_frame = tk.Frame(notebook, bg="light pink")
notebook.add(input_frame, text="Add Blog")

font_style = ("Arial", 20)
label_font = ("Arial", 20)
entry_font = ("Arial", 16)

date_label = tk.Label(input_frame, text="Date", font=label_font)
date_label.pack()
date_entry = tk.Entry(input_frame, font=entry_font)
date_entry.pack(padx=5, pady=5)
date_entry.config(fg="black")

title_label = tk.Label(input_frame, text="Title", font=label_font)
title_label.pack()
title_entry = tk.Entry(input_frame, font=entry_font)
title_entry.pack(padx=5, pady=5)
title_entry.config(fg="black")

author_label = tk.Label(input_frame, text="Author", font=label_font)
author_label.pack()
author_entry = tk.Entry(input_frame, font=entry_font)
author_entry.pack(padx=5, pady=5)
author_entry.config(fg="black")

content_label = tk.Label(input_frame, text="Content", font=label_font)
content_label.pack()
content_text = scrolledtext.ScrolledText(input_frame, wrap=tk.WORD, width=100, height=15, font=entry_font)
content_text.pack(padx=5, pady=5)
content_text.config(fg="black")

add_blog_button = tk.Button(input_frame, text="Add Blog", command=add_blog, font=("Arial", 14))
add_blog_button.pack()

second_page = ttk.Frame(notebook)
notebook.add(second_page, text="Second Page")

second_text = scrolledtext.ScrolledText(second_page, wrap=tk.WORD, width=100, height=20, font=entry_font)
second_text.pack(fill=tk.BOTH, expand=True)
second_text.config(state=tk.DISABLED)

root.mainloop()

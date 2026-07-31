from tkinter import * 
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

def main() -> None:
    paths: dict = {'file1': None, 'file2': None}

    root = Tk()
    root.title("JustMerge")
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    ttk.Button(frm, text="Choose file 1", command=lambda: choose_file(paths, 'file1')).grid(column=0, row=0)
    ttk.Button(frm, text="Choose file 2", command=lambda: choose_file(paths, 'file2')).grid(column=1, row=0)
    ttk.Button(frm, text="Merge", command=lambda: process(paths=paths)).grid(column=0, row=1)
    root.mainloop()

def choose_file(container: dict, name: str) -> None:
    path = filedialog.askopenfilename(
        title="Choose file",
        filetypes=[
            ("Text files", ".txt"),
        ],
        initialdir="/"
    )
    if path:
        container[name] = path

def handle_file(fp) -> list:
    try:
        with open(fp, "r") as f:
            return f.readlines()
    except ( FileNotFoundError, PermissionError, UnicodeDecodeError) as e:
        print(f"File handle error: {e}")
        return []

def process(paths: dict) -> None:
    if paths['file1'] is None or paths['file2'] is None:
        print("Except files_paths isn't exsist")
        result = messagebox.showinfo(title="Warning!", message="You don't choose all files paths.")
    else:
        f1 = list(dict.fromkeys(handle_file(paths["file1"])))
        f2 = list(dict.fromkeys(handle_file(paths["file2"])))
        if not f1:
            messagebox.showinfo(title="Warning!", message="File 1 is empty")
            return
        if not f2:
            messagebox.showinfo(title="Warning!", message="File 2 is empty")
            return
        result = merge(f1 = f1, f2 = f2)
        try: 
            with open("merged_file.txt", "w") as f:
                f.write(result)
        except (FileExistsError, PermissionError, UnicodeDecodeError) as e:
            print(f"File merge error: ")

def merge(f1: list, f2: list):
    f1[len(f1)-1] = f1[len(f1)-1] + "\n"
    f2[len(f2)-1] = f2[len(f2)-1] + "\n"
    return "".join(list(dict.fromkeys(list(f1 + f2))))

if __name__ == "__main__":
    main()
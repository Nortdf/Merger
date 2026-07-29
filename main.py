from tkinter import * 
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

files_paths: list = []

def main() -> None:
    root = Tk()
    root.title("JustMerge")
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    ttk.Button(frm, text="Choose file", command=choose_file).grid(column=0, row=0)
    ttk.Button(frm, text="Choose file", command=choose_file).grid(column=1, row=0)
    ttk.Button(frm, text="Merge", command=process).grid(column=0, row=1)
    root.mainloop()

def choose_file() -> str:
    files_paths.append(filedialog.askopenfilename(
        title="Choose file",
        filetypes=[
            ("Text files", ".txt"),
        ],
        initialdir="/"
    ))

def handle_file(fp) -> list:
    try:
        with open(fp, "r") as f:
            return f.readlines()
    except ( FileNotFoundError, PermissionError, UnicodeDecodeError) as e:
        print(f"File handle error: {e}")
        return []

def process():
    if len(files_paths) != 2:
        print("Except files_paths isn't exsist")
        result = messagebox.showinfo(title="Warning!", message="You don't choose all files paths.")
    else:
        result = merge(f1 = list(dict.fromkeys(handle_file(files_paths[0]))), f2 = list(dict.fromkeys(handle_file(files_paths[1]))))
        try: 
            with open("merged_file.txt", "w") as f:
                f.write(result)
        except (FileExistsError, PermissionError, UnicodeDecodeError) as e:
            print(f"File merge error: ")

def merge(f1: list, f2: list) -> str:
    f1[len(f1)-1] = f1[len(f1)-1] + "\n"
    f2[len(f2)-1] = f2[len(f2)-1] + "\n"
    return "".join(list(dict.fromkeys(list(f1 + f2))))

if __name__ == "__main__":
    main()
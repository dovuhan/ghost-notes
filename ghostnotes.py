import tkinter as tk
from tkinter import ttk, messagebox
import json
from pathlib import Path
from ttkthemes import ThemedTk

DATA_FILE = Path("notes.json")

if not DATA_FILE.exists():
    DATA_FILE.write_text("[]")

def load_notes():
    return json.loads(DATA_FILE.read_text())

def save_notes(notes):
    DATA_FILE.write_text(json.dumps(notes, indent=2))

class GhostNotesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("👻 GhostNotes")
        self.notes = load_notes()
        self.selected_index = None

        self.setup_ui()

    def setup_ui(self):
        self.root.geometry("700x400")
        self.root.configure(bg="#1e1e1e")

        # Sol Panel: Not Listesi
        self.left_frame = ttk.Frame(self.root)
        self.left_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

        self.notes_listbox = tk.Listbox(self.left_frame, bg="#111", fg="#0f0", width=30)
        self.notes_listbox.pack(fill=tk.BOTH, expand=True)
        self.notes_listbox.bind("<<ListboxSelect>>", self.on_note_select)

        # Sağ Panel: Not İçeriği
        self.right_frame = ttk.Frame(self.root)
        self.right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.text = tk.Text(self.right_frame, bg="#111", fg="#0f0", insertbackground="#0f0")
        self.text.pack(fill=tk.BOTH, expand=True)

        # Butonlar
        btn_frame = ttk.Frame(self.root)
        btn_frame.pack(side=tk.BOTTOM, pady=5)

        ttk.Button(btn_frame, text="Yeni Not", command=self.new_note).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Sil", command=self.delete_note).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Kaydet", command=self.save_note).pack(side=tk.LEFT, padx=5)

        self.refresh_notes()

    def refresh_notes(self):
        self.notes_listbox.delete(0, tk.END)
        for note in self.notes:
            title = note.split("\n")[0][:30]
            self.notes_listbox.insert(tk.END, title)

    def new_note(self):
        self.notes.append("")
        self.refresh_notes()
        self.notes_listbox.select_set(tk.END)
        self.on_note_select()

    def delete_note(self):
        if self.selected_index is not None:
            del self.notes[self.selected_index]
            self.selected_index = None
            self.refresh_notes()
            self.text.delete("1.0", tk.END)
            save_notes(self.notes)

    def save_note(self):
        if self.selected_index is not None:
            self.notes[self.selected_index] = self.text.get("1.0", tk.END).strip()
            save_notes(self.notes)
            self.refresh_notes()

    def on_note_select(self, event=None):
        try:
            index = self.notes_listbox.curselection()[0]
            self.selected_index = index
            note = self.notes[index]
            self.text.delete("1.0", tk.END)
            self.text.insert(tk.END, note)
        except IndexError:
            pass

if __name__ == "__main__":
    root = ThemedTk(theme="black")
    app = GhostNotesApp(root)
    root.mainloop()


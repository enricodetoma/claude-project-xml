import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import xml.etree.ElementTree as ET
from tkinterdnd2 import DND_FILES, TkinterDnD
from typing import Set
import os
from pathlib import Path

class ProjectManager(TkinterDnD.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Project XML Manager")
        self.geometry("600x400")
        
        # Store unique file paths
        self.file_paths: Set[str] = set()
        
        self.setup_ui()
        
    def setup_ui(self):
        # Main frame
        main_frame = ttk.Frame(self)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Buttons frame
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill=tk.X, pady=(0, 10))
        
        # Add file button
        add_btn = ttk.Button(button_frame, text="+ Add Files", command=self.add_files)
        add_btn.pack(side=tk.LEFT, padx=5)
        
        # Save XML button
        save_btn = ttk.Button(button_frame, text="Save XML", command=self.save_xml)
        save_btn.pack(side=tk.LEFT, padx=5)
        
        # Open XML button
        open_btn = ttk.Button(button_frame, text="Open XML", command=self.open_xml)
        open_btn.pack(side=tk.LEFT, padx=5)
        
        # Clear button
        clear_btn = ttk.Button(button_frame, text="Clear All", command=self.clear_files)
        clear_btn.pack(side=tk.LEFT, padx=5)
        
        # Listbox frame with scrollbar
        list_frame = ttk.Frame(main_frame)
        list_frame.pack(fill=tk.BOTH, expand=True)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Listbox for files
        self.file_list = tk.Listbox(list_frame)
        self.file_list.pack(fill=tk.BOTH, expand=True)
        
        # Configure scrollbar
        self.file_list.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.file_list.yview)
        
        # Configure drag and drop
        self.file_list.drop_target_register(DND_FILES)
        self.file_list.dnd_bind('<<Drop>>', self.drop_files)
        
        # Status label
        self.status_label = ttk.Label(main_frame, text="Drag and drop files here or use + button")
        self.status_label.pack(fill=tk.X, pady=(10, 0))
    
    def add_files(self):
        """Add files using file dialog"""
        files = filedialog.askopenfilenames(title="Select files")
        self.process_files(files)
    
    def process_files(self, files):
        """Process list of files and add them if not already present"""
        added = 0
        for file in files:
            if file not in self.file_paths:
                self.file_paths.add(file)
                self.file_list.insert(tk.END, file)
                added += 1
        
        self.update_status(f"Added {added} new file(s)")
    
    def drop_files(self, event):
        """Handle drag and drop files"""
        files = self.tk.splitlist(event.data)
        self.process_files(files)
    
    def clear_files(self):
        """Clear all files from the list"""
        self.file_paths.clear()
        self.file_list.delete(0, tk.END)
        self.update_status("All files cleared")
    
    def update_status(self, message):
        """Update status label"""
        self.status_label.config(text=message)
    
    def save_xml(self):
        """Save files list to XML"""
        if not self.file_paths:
            messagebox.showwarning("Warning", "No files to save!")
            return
            
        filename = filedialog.asksaveasfilename(
            defaultextension=".xml",
            filetypes=[("XML files", "*.xml")],
            initialfile="project.xml"
        )
        
        if not filename:
            return
            
        try:
            root = ET.Element("project")
            
            for file_path in self.file_paths:
                doc = ET.SubElement(root, "document")
                source = ET.SubElement(doc, "source")
                source.text = file_path
                
                # Only add content if file is text and not too large
                try:
                    file_size = os.path.getsize(file_path)
                    if file_size < 1024 * 1024:  # 1MB limit
                        with open(file_path, 'r', encoding='utf-8') as f:
                            content = ET.SubElement(doc, "document_content")
                            content.text = f.read()
                except (UnicodeDecodeError, IOError):
                    # Skip content if file is binary or can't be read
                    pass
            
            tree = ET.ElementTree(root)
            tree.write(filename, encoding='utf-8', xml_declaration=True)
            
            self.update_status(f"Saved XML to {filename}")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save XML: {str(e)}")
    
    def open_xml(self):
        """Open XML and load files list"""
        filename = filedialog.askopenfilename(
            filetypes=[("XML files", "*.xml")]
        )
        
        if not filename:
            return
            
        try:
            tree = ET.parse(filename)
            root = tree.getroot()
            
            # Clear current files
            self.clear_files()
            
            # Add files from XML
            for doc in root.findall('document'):
                source = doc.find('source')
                if source is not None and source.text:
                    self.file_paths.add(source.text)
                    self.file_list.insert(tk.END, source.text)
            
            self.update_status(f"Loaded {len(self.file_paths)} files from {filename}")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open XML: {str(e)}")

if __name__ == "__main__":
    app = ProjectManager()
    app.mainloop()

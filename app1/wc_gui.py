import tkinter as tk
from tkinter import filedialog, messagebox
import logging

# Configure logging
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

def count_file(file):
    """
    Count the number of lines, words, and characters in a file object.
    
    Args:
        file: A file object to read from.
    
    Returns:
        A tuple containing (lines, words, chars).
    """
    lines = words = chars = 0
    for line in file:
        lines += 1
        words += len(line.split())
        chars += len(line)
    return (lines, words, chars)

class WCApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Word Count Tool")
        self.root.geometry("600x400")

        # Frame for buttons
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=10)

        # Button to select files
        self.select_button = tk.Button(
            self.button_frame, 
            text="Select Files", 
            command=self.select_files
        )
        self.select_button.pack(side=tk.LEFT, padx=5)

        # Button to clear results
        self.clear_button = tk.Button(
            self.button_frame, 
            text="Clear Results", 
            command=self.clear_results
        )
        self.clear_button.pack(side=tk.LEFT, padx=5)

        # Text widget to display results
        self.results_text = tk.Text(root, wrap=tk.WORD)
        self.results_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    def select_files(self):
        """Open a file dialog to select files and display their word counts."""
        filepaths = filedialog.askopenfilenames(
            title="Select Files",
            filetypes=[("All Files", "*.*")]
        )
        if not filepaths:
            return

        counts_list = []
        total_lines = total_words = total_chars = 0

        for filepath in filepaths:
            try:
                with open(filepath, 'r') as f:
                    lines, words, chars = count_file(f)
                    counts_list.append((lines, words, chars, filepath))
                    total_lines += lines
                    total_words += words
                    total_chars += chars
            except FileNotFoundError:
                logging.error(f"File not found: {filepath}")
                self.results_text.insert(
                    tk.END, 
                    f"Error: File not found - {filepath}\n"
                )
            except PermissionError:
                logging.error(f"Permission denied: {filepath}")
                self.results_text.insert(
                    tk.END, 
                    f"Error: Permission denied - {filepath}\n"
                )
            except IOError as e:
                logging.error(f"IO error occurred: {e}")
                self.results_text.insert(
                    tk.END, 
                    f"Error: {e} - {filepath}\n"
                )
            except Exception as e:
                logging.error(f"Unexpected error: {e}")
                self.results_text.insert(
                    tk.END, 
                    f"Error: An unexpected error occurred - {filepath}\n"
                )

        # Display individual file counts
        for lines, words, chars, filepath in counts_list:
            self.results_text.insert(
                tk.END,
                f"Lines: {lines:<8} Words: {words:<8} Characters: {chars:<8} File: {filepath}\n"
            )

        # Display total counts if multiple files
        if len(counts_list) > 1:
            self.results_text.insert(
                tk.END,
                f"\nTotal Lines: {total_lines:<8} Total Words: {total_words:<8} Total Characters: {total_chars:<8}\n"
            )

    def clear_results(self):
        """Clear the results text widget."""
        self.results_text.delete(1.0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = WCApp(root)
    root.mainloop()
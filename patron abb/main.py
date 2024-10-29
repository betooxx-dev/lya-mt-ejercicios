import tkinter as tk
from tkinter import ttk

class TuringMachine:
    def __init__(self):
        self.tape = []
        self.head = 0
        self.state = 'q0'
        self.transition_table = {
            'q0': {
                'a': ('a', 'R', 'q1')
            },
            'q1': {
                'b': ('b', 'R', 'q2')
            },
            'q2': {
                'b': ('b', 'R', 'q3')
            },
            'q3': {
                'a': ('a', 'R', 'q1')
            }
        }
    
    def run(self, input_string):
        self.tape = list(input_string) + [' ']
        self.head = 0
        self.state = 'q0'
        
        while self.head < len(self.tape):
            current_symbol = self.tape[self.head]
            if current_symbol == ' ':
                break
            if self.state in self.transition_table and current_symbol in self.transition_table[self.state]:
                write_symbol, move, next_state = self.transition_table[self.state][current_symbol]
                self.tape[self.head] = write_symbol
                if move == 'R':
                    self.head += 1
                self.state = next_state
            else:
                break
        return self.state == 'q3', ''.join(self.tape).rstrip('B')

class ModernTuringGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Validador de Patrón 'abb'")
        self.root.geometry("900x600")
        
        self.colors = {
            'bg': '#2E3B4E',            # Fondo principal
            'secondary': '#3E4C63',      # Fondo secundario
            'accent': '#4CAF50',         # Color de acento
            'text': '#FFFFFF',           # Texto principal
            'subtext': '#B0B9C6',        # Texto secundario
            'button': '#4CAF50',         # Botones
            'button_hover': '#45a049',   # Hover de botones
            'success': '#4CAF50',        # Éxito
            'error': '#FF5252',          # Error
            'cell': '#5C6B7F',           # Celdas de la cinta
            'head': '#4CAF50'            # Cabezal
        }
        
        self.root.configure(bg=self.colors['bg'])
        self.setup_styles()
        self.create_widgets()
        self.turing_machine = TuringMachine()
        
    def setup_styles(self):
        self.style = ttk.Style()
        self.style.configure('TFrame', background=self.colors['bg'])
        self.style.configure('TLabel', 
                           background=self.colors['bg'], 
                           foreground=self.colors['text'],
                           font=('Helvetica', 10))
        self.style.configure('Header.TLabel',
                           background=self.colors['bg'],
                           foreground=self.colors['text'],
                           font=('Helvetica', 24, 'bold'))
        self.style.configure('SubHeader.TLabel',
                           background=self.colors['bg'],
                           foreground=self.colors['subtext'],
                           font=('Helvetica', 12))
        
    def create_widgets(self):
        main_frame = ttk.Frame(self.root, style='TFrame')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Header
        ttk.Label(main_frame,
                 text="Validador de Patrón 'abb'",
                 style='Header.TLabel').pack(pady=(0,5))
        
        ttk.Label(main_frame,
                 text="Ingrese una cadena de a's y b's para validar",
                 style='SubHeader.TLabel').pack(pady=(0,20))
        
        # Input section
        input_frame = ttk.Frame(main_frame, style='TFrame')
        input_frame.pack(fill=tk.X, padx=20, pady=10)
        
        self.entry = tk.Entry(
            input_frame,
            font=('Helvetica', 14),
            bg=self.colors['secondary'],
            fg=self.colors['text'],
            insertbackground=self.colors['text'],
            relief='flat',
            width=40
        )
        self.entry.pack(side=tk.LEFT, padx=10)
        self.entry.bind("<KeyRelease>", self.validate_input)
        
        self.run_button = tk.Button(
            input_frame,
            text="Validar",
            command=self.run_turing_machine,
            font=('Helvetica', 12, 'bold'),
            bg=self.colors['button'],
            fg=self.colors['text'],
            activebackground=self.colors['button_hover'],
            activeforeground=self.colors['text'],
            relief='flat',
            padx=20,
            pady=10,
            state='disabled'
        )
        self.run_button.pack(side=tk.LEFT, padx=10)
        
        # Error label
        self.error_label = ttk.Label(
            main_frame,
            text="",
            style='TLabel'
        )
        self.error_label.pack(pady=10)
        
        # Tape frame
        tape_frame = ttk.Frame(main_frame, style='TFrame')
        tape_frame.pack(fill=tk.BOTH, expand=True, pady=20)
        
        ttk.Label(tape_frame,
                 text="Estado de la Cinta",
                 style='SubHeader.TLabel').pack(pady=(0,10))
        
        self.tape_canvas = tk.Canvas(
            tape_frame,
            bg=self.colors['secondary'],
            height=100,
            highlightthickness=0
        )
        self.tape_canvas.pack(fill=tk.X, padx=20)
        
        # Result label
        self.result_label = ttk.Label(
            main_frame,
            text="",
            font=('Helvetica', 14, 'bold'),
            style='TLabel'
        )
        self.result_label.pack(pady=10)
        
    def update_tape_display(self, tape, head_pos):
        self.tape_canvas.delete('all')
        
        cell_width = 40
        cell_height = 40
        x_start = 20
        y_start = 30
        
        for i, symbol in enumerate(tape):
            x = x_start + (i * cell_width)
            cell_color = self.colors['head'] if i == head_pos else self.colors['cell']
            
            # Cell
            self.tape_canvas.create_rectangle(
                x, y_start,
                x + cell_width, y_start + cell_height,
                fill=cell_color,
                outline=self.colors['text'],
                width=2
            )
            
            # Symbol
            self.tape_canvas.create_text(
                x + cell_width/2,
                y_start + cell_height/2,
                text=symbol,
                fill=self.colors['text'],
                font=('TkFixedFont', 12)
            )
    
    def validate_input(self, event=None):
        input_string = self.entry.get()
        if not all(c in 'ab' for c in input_string):
            self.error_label.configure(text="La entrada debe contener solo 'a' y 'b'", foreground=self.colors['error'])
            self.run_button.config(state='disabled')
        else:
            self.error_label.configure(text="")
            self.run_button.config(state='normal')
    
    def run_turing_machine(self):
        input_string = self.entry.get()
        is_accepted, result = self.turing_machine.run(input_string)
        
        self.update_tape_display(self.turing_machine.tape, self.turing_machine.head)
        
        if is_accepted:
            message = f"La cadena '{input_string}' es válida (mantiene el patrón 'abb')"
            color = self.colors['success']
        else:
            message = f"La cadena '{input_string}' no es válida (no mantiene el patrón 'abb')"
            color = self.colors['error']
            
        self.result_label.configure(text=message, foreground=color)

if __name__ == "__main__":
    app = ModernTuringGUI()
    app.root.mainloop()
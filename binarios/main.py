import tkinter as tk
from tkinter import ttk

class BinaryTuringMachine:
    def __init__(self):
        self.tape = []
        self.head_position = 0
        self.current_state = 'q0'
        self.transitions = self.initialize_transitions()
        
    def initialize_transitions(self):
        transitions = {}
        
        # Estado inicial q0 - Validación del primer "1"
        transitions[('q0', '1')] = ('q1', '1', 'R')
        
        # Estado q1 - Validación del "0"
        transitions[('q1', '0')] = ('q2', '0', 'R')
        
        # Estado q2 - Validación del "+"
        transitions[('q2', '+')] = ('q3', '+', 'R')
        
        # Estado q3 - Procesamiento de dígitos binarios después del +
        transitions[('q3', '0')] = ('q3', '0', 'R')
        transitions[('q3', '1')] = ('q3', '1', 'R')
        transitions[('q3', '=')] = ('q4', '=', 'R')
        
        # Estado q4 - Estado final
        transitions[('q4', '')] = ('q5', '', 'S')  # S = Stop
        
        return transitions
        
    def step(self):
        if self.head_position >= len(self.tape):
            self.tape.append('')
            
        current_symbol = self.tape[self.head_position]
        transition_key = (self.current_state, current_symbol)
        
        if transition_key not in self.transitions:
            return False
            
        new_state, write_symbol, movement = self.transitions[transition_key]
        self.tape[self.head_position] = write_symbol
        self.current_state = new_state
        
        if movement == 'R':
            self.head_position += 1
            
        return True
    
    def extract_numbers(self):
        tape_string = ''.join(self.tape)
        try:
            parts = tape_string.split('+')
            if len(parts) != 2:
                return None, None
                
            num1 = parts[0].strip()
            num2 = parts[1].split('=')[0].strip()
            
            return int(num1, 2), int(num2, 2)
        except:
            return None, None
            
    def calculate_sum(self):
        num1, num2 = self.extract_numbers()
        if num1 is None or num2 is None:
            return None
        return bin(num1 + num2)[2:]  # Elimina el prefijo '0b'
    
    def run(self, input_string):
        self.tape = list(input_string)
        self.head_position = 0
        self.current_state = 'q0'
        
        while self.step():
            if self.current_state == 'q5':
                return True
                
        return False

class ModernBinaryTuringGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Máquina de Turing - Suma Binaria")
        self.root.geometry("900x600")
        self.root.configure(bg="#2E3B4E")
        
        self.setup_styles()
        self.turing_machine = BinaryTuringMachine()
        self.create_widgets()
        
    def setup_styles(self):
        self.style = ttk.Style()
        self.style.configure('TFrame', background='#2E3B4E')
        self.style.configure('TLabel', 
                           background='#2E3B4E', 
                           foreground='white',
                           font=('Helvetica', 10))
        self.style.configure('Header.TLabel',
                           background='#2E3B4E',
                           foreground='white',
                           font=('Helvetica', 24, 'bold'))
        self.style.configure('SubHeader.TLabel',
                           background='#2E3B4E',
                           foreground='#B0B9C6',
                           font=('Helvetica', 12))
        
    def create_widgets(self):
        # Frame principal
        self.main_frame = ttk.Frame(self.root, style='TFrame')
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Header
        ttk.Label(self.main_frame,
                 text="Sumador Binario",
                 style='Header.TLabel').pack(pady=(0,5))
        
        ttk.Label(self.main_frame,
                 text="Formato: 10+1= (números binarios)",
                 style='SubHeader.TLabel').pack(pady=(0,20))
        
        # Frame de entrada
        input_frame = ttk.Frame(self.main_frame, style='TFrame')
        input_frame.pack(fill=tk.X, padx=20, pady=10)
        
        # Entrada
        self.input_var = tk.StringVar()
        entry = tk.Entry(
            input_frame,
            textvariable=self.input_var,
            font=('Helvetica', 14),
            bg='#3E4C63',
            fg='white',
            insertbackground='white',
            width=40
        )
        entry.pack(side=tk.LEFT, padx=10)
        
        # Botón de cálculo
        calculate_button = tk.Button(
            input_frame,
            text="Calcular",
            command=self.run_machine,
            font=('Helvetica', 12, 'bold'),
            bg='#4CAF50',
            fg='white',
            activebackground='#45a049',
            activeforeground='white',
            relief=tk.FLAT,
            padx=20,
            pady=10
        )
        calculate_button.pack(side=tk.LEFT, padx=10)
        
        # Frame para la cinta
        self.tape_frame = ttk.Frame(self.main_frame, style='TFrame')
        self.tape_frame.pack(fill=tk.BOTH, expand=True, pady=20)
        
        ttk.Label(self.tape_frame,
                 text="Estado de la Cinta",
                 style='SubHeader.TLabel').pack(pady=(0,10))
        
        # Canvas para la cinta
        self.tape_canvas = tk.Canvas(
            self.tape_frame,
            bg='#3E4C63',
            height=100,
            highlightthickness=0
        )
        self.tape_canvas.pack(fill=tk.X, padx=20)
        
        # Estado actual
        self.state_var = tk.StringVar(value="Estado actual: q0")
        self.state_label = ttk.Label(
            self.main_frame,
            textvariable=self.state_var,
            style='TLabel'
        )
        self.state_label.pack(pady=10)
        
        # Resultado
        self.result_var = tk.StringVar()
        self.result_label = ttk.Label(
            self.main_frame,
            textvariable=self.result_var,
            style='TLabel'
        )
        self.result_label.pack(pady=10)
        
    def update_tape_display(self):
        self.tape_canvas.delete("all")
        
        cell_width = 40
        cell_height = 40
        x_start = 20
        y_start = 30
        
        for i, symbol in enumerate(self.turing_machine.tape):
            x = x_start + (i * cell_width)
            cell_color = "#4CAF50" if i == self.turing_machine.head_position else "#5C6B7F"
            
            self.tape_canvas.create_rectangle(
                x, y_start,
                x + cell_width, y_start + cell_height,
                fill=cell_color,
                outline="white",
                width=2
            )
            
            self.tape_canvas.create_text(
                x + cell_width/2,
                y_start + cell_height/2,
                text=symbol,
                fill="white",
                font=('TkFixedFont', 12)
            )
    
    def run_machine(self):
        input_string = self.input_var.get()
        if not input_string:
            self.show_error("Por favor ingrese una expresión binaria")
            return
            
        try:
            is_valid = self.turing_machine.run(input_string)
            self.update_tape_display()
            self.state_var.set(f"Estado actual: {self.turing_machine.current_state}")
            
            if is_valid:
                result = self.turing_machine.calculate_sum()
                if result:
                    self.show_success(f"Resultado: {result} (binario) = {int(result, 2)} (decimal)")
                else:
                    self.show_error("Error al calcular la suma")
            else:
                self.show_error("Expresión binaria inválida")
                
        except Exception as e:
            self.show_error(f"Error: {str(e)}")
    
    def show_error(self, message):
        self.result_var.set(message)
        self.result_label.configure(foreground="#FF5252")
        
    def show_success(self, message):
        self.result_var.set(message)
        self.result_label.configure(foreground="#4CAF50")

if __name__ == "__main__":
    app = ModernBinaryTuringGUI()
    app.root.mainloop()
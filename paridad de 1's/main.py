import tkinter as tk
from tkinter import messagebox

class TuringMachine:
    def __init__(self):
        self.tape = []
        self.head = 0
        self.state = 'q0'
        
        # Definición de la tabla de transiciones
        self.transition_table = {
            'q0': {
                '0': ('0', 'R', 'q0'),
                '1': ('1', 'R', 'q1'),
                'B': ('0', 'S', 'qf')
            },
            'q1': {
                '0': ('0', 'R', 'q1'),
                '1': ('1', 'R', 'q0'),
                'B': ('1', 'S', 'qf')
            }
        }

    def run(self, input_string):
        self.tape = list(input_string) + ['B']  # B represents blank
        self.head = 0
        self.state = 'q0'

        while self.state != 'qf':
            current_symbol = self.tape[self.head]
            if self.state in self.transition_table and current_symbol in self.transition_table[self.state]:
                write_symbol, move, next_state = self.transition_table[self.state][current_symbol]
                self.tape[self.head] = write_symbol
                if move == 'R':
                    self.head += 1
                self.state = next_state
            else:
                break  # No transition defined, halt the machine

        return ''.join(self.tape).rstrip('B')

class TuringMachineGUI:
    def __init__(self, master):
        self.master = master
        master.title("Máquina de Turing - Paridad de 1's")

        # Frame para entrada
        input_frame = tk.Frame(master, pady=10)
        input_frame.pack()

        self.label = tk.Label(input_frame, text="Ingrese una cadena binaria:", font=("Arial", 12))
        self.label.grid(row=0, column=0, padx=5, pady=5)

        self.entry = tk.Entry(input_frame, font=("Arial", 12), width=25)
        self.entry.grid(row=0, column=1, padx=5, pady=5)
        self.entry.bind("<KeyRelease>", self.validate_input)

        # Mensaje de error dinámico
        self.error_label = tk.Label(input_frame, text="", fg="red", font=("Arial", 10))
        self.error_label.grid(row=1, columnspan=2, pady=5)

        # Botón de ejecución
        self.run_button = tk.Button(master, text="Ejecutar", command=self.run_turing_machine, font=("Arial", 12), width=15)
        self.run_button.pack(pady=10)

        # Label para el resultado
        self.result_label = tk.Label(master, text="", font=("Arial", 12))
        self.result_label.pack(pady=10)

    def validate_input(self, event=None):
        input_string = self.entry.get()
        if not all(c in '01' for c in input_string):
            self.error_label.config(text="La entrada debe ser binaria (solo 0s y 1s)")
            self.run_button.config(state=tk.DISABLED)
        else:
            self.error_label.config(text="")
            self.run_button.config(state=tk.NORMAL)

    def run_turing_machine(self):
        input_string = self.entry.get()
        tm = TuringMachine()
        result = tm.run(input_string)
        parity = "par" if result[-1] == '0' else "impar"
        color = "green" if parity == "par" else "blue"
        self.result_label.config(text=f"Resultado: {result}\nLa cantidad de 1's es {parity}", fg=color)

# Inicializa la ventana
root = tk.Tk()
gui = TuringMachineGUI(root)
root.mainloop()
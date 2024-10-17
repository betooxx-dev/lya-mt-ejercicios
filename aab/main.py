import tkinter as tk
from tkinter import messagebox

class TuringMachine:
    def __init__(self):
        self.tape = []
        self.head = 0
        self.state = 'q0'
        
        self.transition_table = {
            'q0': {
                'a': ('a', 'R', 'q1'),
                'b': ('b', 'R', 'q0')  
            },
            'q1': {
                'b': ('b', 'R', 'q2'),
                'a': ('a', 'R', 'q1')  
            },
            'q2': {
                'b': ('b', 'R', 'q3'),
                'a': ('a', 'R', 'q1')  
            },
            'q3': {
                'a': ('a', 'R', 'q1'),
                'b': ('b', 'R', 'q0')
            }
        }

    def run(self, input_string):
        self.tape = list(input_string) + ['B']  
        self.head = 0
        self.state = 'q0'

        while self.head < len(self.tape):
            current_symbol = self.tape[self.head]
            if current_symbol == 'B':
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

class TuringMachineGUI:
    def __init__(self, master):
        self.master = master
        master.title("Máquina de Turing - Validador de patrón 'abb'")

        # Frame para entrada
        input_frame = tk.Frame(master, pady=10)
        input_frame.pack()

        self.label = tk.Label(input_frame, text="Ingrese una cadena de a's y b's:", font=("Arial", 12))
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
        if not all(c in 'ab' for c in input_string):
            self.error_label.config(text="La entrada debe contener solo 'a' y 'b'")
            self.run_button.config(state=tk.DISABLED)
        else:
            self.error_label.config(text="")
            self.run_button.config(state=tk.NORMAL)

    def run_turing_machine(self):
        input_string = self.entry.get()
        tm = TuringMachine()
        is_accepted, result = tm.run(input_string)
        if is_accepted:
            message = f"La cadena '{input_string}' es válida (termina en el patrón 'abb')"
            color = "green"
        else:
            message = f"La cadena '{input_string}' no es válida (no termina en el patrón 'abb')"
            color = "red"
        self.result_label.config(text=message, fg=color)

root = tk.Tk()
gui = TuringMachineGUI(root)
root.mainloop()
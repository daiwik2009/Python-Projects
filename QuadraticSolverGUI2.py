import tkinter as tk

def solve():
   
    a = textbox.get()
    
   
    b = a.replace(" ", "")
    
    
    if b.find('-') != -1:
        c = b.replace("-", "+-")
        d = c.split('+')
    else:
        d = b.split('+')

    
    l = [i for i in d if i != '']

    try:
        
        if len(l) == 3:
            
            if l[0] == 'x^2': A = 1
            elif l[0] == '-x^2': A = -1
            else: A = int(l[0].replace('x^2', ''))
            
         
            if l[1] == 'x': B = 1
            elif l[1] == '-x': B = -1
            else: B = int(l[1].replace('x', ''))
            
          
            C = int(l[2])

            D = B**2 - 4*A*C

            if D > 0:
                x1 = ((-B) + D**0.5) / (2*A)
                x2 = ((-B) - D**0.5) / (2*A)
                label2.config(text=f'Roots are Real & Different: x1={x1:.2f}, x2={x2:.2f}')
            elif D == 0:
                x = (-B) / (2*A)
                label2.config(text=f'Roots are Real & Equal: x={x}')
            else:
                label2.config(text='Roots are Complex')

    
        elif len(l) == 2:
            if 'x' not in l[1]:
                if l[0] == 'x^2': A = 1
                elif l[0] == '-x^2': A = -1
                else: A = int(l[0].replace('x^2', ''))
                
                B = 0
                C = int(l[1])

                D = B**2 - 4*A*C

                if D > 0:
                    x1 = ((-B) + D**0.5) / (2*A)
                    x2 = ((-B) - D**0.5) / (2*A)
                    label2.config(text=f'Roots are Real & Different: x1={x1:.2f}, x2={x2:.2f}')
                elif D == 0:
                    x = (-B) / (2*A)
                    label2.config(text=f'Roots are Real & Equal: x={x}')
                else:
                    label2.config(text='Roots are Complex')
            else:
                label2.config(text='Root is 0 (Incomplete Equation)')
        else:
            label2.config(text="Please enter a valid quadratic (e.g. 1x^2-5x+6)")

    except ValueError:
        label2.config(text="Error: Make sure to include 'x^2' and 'x'")


root = tk.Tk()
root.geometry('450x250')
root.title("Quadratic Solver")


label = tk.Label(root, text='Quadratic Equation Solver', font=('Arial', 16, 'bold'))
label.pack(pady=10)


instr = tk.Label(root, text="Format: ax^2+bx+c", font=('Arial', 9))
instr.pack()


textbox = tk.Entry(root, font=('Arial', 12), width=30)
textbox.pack(pady=10)



btn = tk.Button(root, text='Solve Equation', height=1, width=15, command=solve, bg='#4CAF50', fg='white')
btn.pack(pady=5)

label2 = tk.Label(root, text="Your Result: ", font=("Arial", 10, "italic"), fg="blue")
label2.pack(pady=20)

root.mainloop()
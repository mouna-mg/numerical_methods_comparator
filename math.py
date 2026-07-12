import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import csv
import time

x = sp.Symbol("x")


class NumericalComparator:

    def __init__(self, root):
        self.root = root
        self.root.title("Numerical Methods Comparator")
        self.root.geometry("1200x780")
        self.root.configure(bg="#1e1e1e")

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview",
                        background="#2b2b2b",
                        foreground="white",
                        fieldbackground="#2b2b2b",
                        rowheight=25)
        style.configure("Treeview.Heading",
                        background="#444",
                        foreground="white")

        self.func = None
        self.dfunc = None
        self.expr = None
        self.intervals = []

        self.create_widgets()

    def parse_function(self):
        eq = self.eq_entry.get().strip()
        eq = eq.replace("^", "**")
        eq = eq.replace("e**", "E**")

        if "x" not in eq:
            raise ValueError("Equation must contain x.")

        self.expr = sp.sympify(eq)

        derivative = sp.diff(self.expr, x)

        self.func = sp.lambdify(x, self.expr, "numpy")
        self.dfunc = sp.lambdify(x, derivative, "numpy")

        self.derivative_label.config(
        
            text=f"Derivative : {derivative}"
        )

    def search_intervals(self):

        self.intervals = []

        def scan(limit):
            vals = np.arange(-limit, limit, 0.5)

            for i in range(len(vals) - 1):
                a = vals[i]
                b = vals[i + 1]

                try:
                    fa = self.func(a)
                    fb = self.func(b)

                    if np.isnan(fa) or np.isnan(fb):
                        continue

                    if fa * fb < 0:
                        self.intervals.append((a, b))

                except:
                    pass

        scan(100)

        if not self.intervals:
            scan(500)

        self.interval_box["values"] = [
            f"{a:.2f} , {b:.2f}" for a, b in self.intervals
        ]

        if self.intervals:
            self.interval_box.current(0)
        else:
            raise ValueError("No valid interval found.")

    def bisection(self, a, b, tol=1e-6, max_iter=100):

        start = time.perf_counter()

        fa = self.func(a)
        fb = self.func(b)

        for i in range(max_iter):
            c = (a + b) / 2
            fc = self.func(c)

            if abs(fc) < tol:
                break

            if fa * fc < 0:
                b = c
                fb = fc
            else:
                a = c
                fa = fc

        end = time.perf_counter()

        return c, i + 1, abs(fc), end - start

    def regula_falsi(self, a, b, tol=1e-6, max_iter=100):

        start = time.perf_counter()

        fa = self.func(a)
        fb = self.func(b)

        for i in range(max_iter):

            c = (a * fb - b * fa) / (fb - fa)
            fc = self.func(c)

            if abs(fc) < tol:
                break

            if fa * fc < 0:
                b = c
                fb = fc
            else:
                a = c
                fa = fc

        end = time.perf_counter()

        return c, i + 1, abs(fc), end - start
    def secant(self, a, b, tol=1e-6, max_iter=100):

        start = time.perf_counter()

        x0 = a
        x1 = b

        for i in range(max_iter):

            f0 = self.func(x0)
            f1 = self.func(x1)

            if abs(f1 - f0) < 1e-12:
                break

            x2 = x1 - f1 * (x1 - x0) / (f1 - f0)

            if abs(self.func(x2)) < tol:
                x1 = x2
                break

            x0 = x1
            x1 = x2

        end = time.perf_counter()

        return x1, i + 1, abs(self.func(x1)), end - start

    def newton(self, guess, tol=1e-6, max_iter=100):

        start = time.perf_counter()

        xn = guess

        for i in range(max_iter):

            fx = self.func(xn)
            dfx = self.dfunc(xn)

            if abs(dfx) < 1e-12:
                break

            xn1 = xn - fx / dfx

            if abs(self.func(xn1)) < tol:
                xn = xn1
                break

            xn = xn1

        end = time.perf_counter()

        return xn, i + 1, abs(self.func(xn)), end - start


    def export_csv(self):

        file = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV File", "*.csv")]
        )

        if not file:
            return

        with open(file, "w", newline="") as f:

            writer = csv.writer(f)

            writer.writerow(
                ["Method", "Root", "Iterations", "Final Error", "Time"])

            for row in self.tree.get_children():
                writer.writerow(self.tree.item(row)["values"])

        messagebox.showinfo("Success", "CSV exported successfully.")

    def create_widgets(self):

        top = tk.Frame(self.root, bg="#1e1e1e")
        top.pack(fill="x", pady=10)

        tk.Label(
            top,
            text="f(x) = ",
            fg="white",
            bg="#1e1e1e",
            font=("Arial", 15, "bold")
        ).pack(side="left", padx=5)

        self.eq_entry = tk.Entry(
            top,
            width=35,
            bg="#2b2b2b",
            fg="white",
            insertbackground="white",
            font=("Arial", 14)
        )

        self.eq_entry.pack(side="left")

        tk.Button(
            top,
            text="Find Intervals",
            command=self.find_intervals,
            font=("Arial", 11, "bold"),
            padx=8,
            pady=3
        ).pack(side="left", padx=8)

        self.interval_box = ttk.Combobox(
            top,
            width=18,
            state="readonly",
            font=("Arial", 12)
        )
        self.interval_box.pack(side="left", padx=8)

        tk.Button(
            top,
            text="Compare Methods",
            command=self.compare,
            font=("Arial", 11, "bold"),
            padx=8,
            pady=3
        ).pack(side="left", padx=5)

        tk.Button(
            top,
            text="Export CSV",
            command=self.export_csv,
            font=("Arial", 11, "bold"),
            padx=8,
            pady=3
        ).pack(side="left", padx=5)

        tk.Button(
            top,
            text="Reset",
            command=self.reset,
            font=("Arial", 11, "bold"),
            padx=8,
            pady=3
        ).pack(side="left", padx=5)

        columns = ("Method", "Root", "Iterations", "Error", "Time (s)")


        style = ttk.Style()

        style.theme_use("clam")

        style.configure(
            "Treeview",
            background="#2b2b2b",
            foreground="white",
            fieldbackground="#2b2b2b",
            rowheight=32,
            font=("Arial", 12)
        )

        style.configure(
            "Treeview.Heading",
            font=("Arial", 13, "bold")
        )

        self.tree = ttk.Treeview(self.root,
                                 columns=columns,
                                 show="headings",
                                 height=4)

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=170, anchor="center")

        self.tree.pack(fill="x", padx=10, pady=5)

        self.derivative_label = tk.Label(
            self.root,
            text="Derivative : ",
            fg="cyan",
            bg="#1e1e1e",
            font=("Arial", 13, "bold")
        )
        self.derivative_label.pack(pady=1)
        
 

        self.result_label = tk.Label(
            self.root,
            text="Recommendation will appear here.",
            fg="#00ff99",
            bg="#1e1e1e",
            font=("Arial", 12, "bold"),
            justify="left"
        )
        self.result_label.pack(pady=2)

        fig = plt.Figure(figsize=(9, 6), dpi=100)
        self.ax = fig.add_subplot(111)

        self.canvas = FigureCanvasTkAgg(fig, master=self.root)
        self.canvas.get_tk_widget().pack(fill="both",
                                         expand=True,
                                         padx=10,
                                         pady=2)

    def find_intervals(self):

        try:
            self.parse_function()
            self.search_intervals()

            messagebox.showinfo(
                "Success",
                f"{len(self.intervals)} interval(s) found."
            )

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def compare(self):

        try:

            if not self.intervals:
                self.find_intervals()

            index = self.interval_box.current()

            if index == -1:
                raise ValueError("Please select an interval.")

            a, b = self.intervals[index]

            midpoint = (a + b) / 2

            methods = {
                "Bisection": self.bisection(a, b),
                "Regula Falsi": self.regula_falsi(a, b),
                "Secant": self.secant(a, b),
                "Newton-Raphson": self.newton(midpoint)
            }

            for row in self.tree.get_children():
                self.tree.delete(row)

            best_method = ""
            best_time = float("inf")

            for name, values in methods.items():

                root, itr, err, t = values

                self.tree.insert(
                    "",
                    tk.END,
                    values=(
                        name,
                        f"{root:.6f}",
                        itr,
                        f"{err:.2e}",
                        f"{t:.6f}"
                    )
                )

                if err < 1e-6 and t < best_time:
                    best_time = t
                    best_method = name

            self.result_label.config(
                text=(
                    f"✔ Recommended Method : {best_method}\n"
                    f"Reason : Least execution time | Required accuracy | Fast convergence\n"
                    f"Conclusion : {best_method} is the recommended method."

                )
            )

            self.plot_graph()

        except Exception as e:
            messagebox.showerror("Error", str(e))
    def reset(self):
        """Reset all inputs, results, graph, and stored data."""

        self.eq_entry.delete(0, tk.END)

        self.interval_box.set("")
        self.interval_box["values"] = ()

        self.intervals = []
        self.func = None
        self.dfunc = None
        self.expr = None

        for row in self.tree.get_children():
            self.tree.delete(row)

        self.result_label.config(
            text="Recommendation will appear here."
        )

        self.derivative_label.config(
            text="Derivative : "
        )

        self.ax.clear()
        self.ax.set_title("Function Graph")
        self.ax.set_xlabel("x")
        self.ax.set_ylabel("f(x)")
        self.ax.grid(True)

        self.canvas.draw()

    def plot_graph(self):
        """Plot the entered function."""

        try:

            if self.interval_box.current() != -1:
                a, b = self.intervals[self.interval_box.current()]
                xs = np.linspace(a - 2, b + 2, 500)
            else:
                xs = np.linspace(-10, 10, 500)
            ys = []

            for val in xs:
                try:
                    y = self.func(val)

                    if np.isfinite(y):
                        ys.append(y)
                    else:
                        ys.append(np.nan)

                except:
                    ys.append(np.nan)

            self.ax.clear()

            self.ax.plot(xs, ys, linewidth=2, label="f(x)")

            try:
                root = float(self.tree.item(self.tree.get_children()[0])["values"][1])

                self.ax.scatter(
                    root,
                    self.func(root),
                    color="red",
                    s=120,
                    label=f"Root = {root:.6f}"
                )

            except:
                pass

            self.ax.axhline(0, color="black", linewidth=1)
            self.ax.axvline(0, color="black", linewidth=1)

            if self.interval_box.current() != -1:

                a, b = self.intervals[self.interval_box.current()]

                self.ax.axvspan(
                    a,
                    b,
                    alpha=0.2,
                    color="green",
                    label="Selected Interval"
                )

            self.ax.set_title(f"Graph of f(x) = {self.expr}")
            self.ax.set_xlabel("X-axis")
            self.ax.set_ylabel("f(x) Value")
            self.ax.grid(True, linestyle="--", alpha=0.6)
            self.ax.legend()

            self.canvas.draw()

        except Exception:
            pass

    def validate_selection(self):

        if len(self.intervals) == 0:
            raise ValueError(
                "No interval found. Click 'Find Intervals' first."
            )

        if self.interval_box.current() == -1:
            raise ValueError(
                "Please select an interval."
            )
def main():
    root = tk.Tk()

    app = NumericalComparator(root)

    root.mainloop()


if __name__ == "__main__":
    main()                                

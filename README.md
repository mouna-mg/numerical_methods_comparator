# 🔢 Numerical Methods Comparator

A Python-based desktop application that compares the performance of four popular numerical methods for solving nonlinear equations. The application automatically detects valid intervals, computes symbolic derivatives, compares convergence performance, and visualizes the function graph through an interactive Tkinter-based graphical user interface.

---

## 📌 Features

- Enter any mathematical equation in terms of **x**
- Automatic equation validation
- Automatic symbolic differentiation using **SymPy**
- Automatic sign-change interval detection
- Interval selection through a dropdown menu
- Comparison of four numerical methods:
  - Bisection Method
  - Regula-Falsi Method
  - Secant Method
  - Newton-Raphson Method
- Displays:
  - Root
  - Number of Iterations
  - Final Error
  - Execution Time
- Automatic recommendation of the best-performing method
- Function graph with highlighted root and selected interval
- Export comparison results to CSV
- Reset functionality
- Dark-themed graphical user interface

---

## 🛠️ Technologies Used

- Python 3.11
- Tkinter
- SymPy
- NumPy
- Matplotlib
- Pandas

---

## 📂 Project Structure

```
numerical_methods_comparator/
│
├── math.py
└── README.md
```

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/mouna-mg/numerical_methods_comparator.git
cd numerical_methods_comparator
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python math.py
```

---

## 📖 How to Use

1. Enter a mathematical equation in terms of **x**.
2. Click **Find Intervals**.
3. Select one of the detected intervals.
4. Click **Compare Methods**.
5. View:
   - Comparison Table
   - Function Graph
   - Recommended Numerical Method
6. Export the results to a CSV file if required.

---

## 📊 Numerical Methods Implemented

- Bisection Method
- Regula-Falsi Method
- Secant Method
- Newton-Raphson Method

---

## 📈 Performance Parameters Compared

- Root Value
- Number of Iterations
- Final Error
- Execution Time

---

## 🧪 Sample Equations

```text
x**3 - 5*x - 1
cos(x) - x
log(x) - 1.6
exp(x) - 3
x*exp(x) - 2
```


## 📄 Output

The application generates:

- Numerical comparison table
- Function graph
- Recommended numerical method
- CSV report

---

## 🎯 Applications

- Engineering Numerical Methods Laboratory
- Educational demonstrations
- Root-finding algorithm comparison
- Mathematical computation and visualization
- Learning convergence behavior of numerical methods

---

## 👩‍💻 Author

**Mouna M G**

GitHub: https://github.com/mouna-mg

---

## 📜 License

This project is developed for educational and academic purposes.

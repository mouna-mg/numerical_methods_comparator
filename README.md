# 🔢 Numerical Methods Comparator

A Python-based desktop application that compares the performance of four popular numerical methods for solving nonlinear equations. The application provides automatic interval detection, symbolic differentiation, graphical visualization, and performance comparison through an interactive Tkinter GUI.

## 📌 Features
- Enter any mathematical equation in terms of **x**
- Automatic equation validation
- Automatic symbolic derivative generation using **SymPy**
- Automatic sign-change interval detection
- Interval selection using a dropdown menu
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
- CSV export of comparison results
- Reset functionality
- Dark-themed graphical user interface

## 🛠️ Technologies Used
- Python 3
- Tkinter
- SymPy
- NumPy
- Matplotlib
- Pandas

## 📂 Project Structure
```
NumericalMethodsComparator/
│
├── math.py
├── requirements.txt
├── README.md
├── dist/
│   └── math.exe
```

## 🚀 Installation

Clone the repository:
```bash
git clone https://github.com/mouna-mg/NumericalMethodsComparator.git
cd NumericalMethodsComparator
```

Install the required libraries:
```bash
pip install -r requirements.txt
```

Run the application:
```bash
python math.py
```

## 📖 How to Use
1. Enter a mathematical equation in terms of **x**.
2. Click **Find Intervals**.
3. Select one of the detected intervals.
4. Click **Compare Methods**.
5. View:
   - Comparison table
   - Function graph
   - Recommended numerical method
6. Export results to CSV if required.

## 📊 Numerical Methods Implemented
- Bisection Method
- Regula-Falsi Method
- Secant Method
- Newton-Raphson Method

## 📈 Performance Parameters Compared
- Root Value
- Number of Iterations
- Final Error
- Execution Time

## 🎯 Example Equations
```
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

## 👨‍💻 Author
**Mouna M G**

## 📜 License
This project is intended for educational and academic purposes.

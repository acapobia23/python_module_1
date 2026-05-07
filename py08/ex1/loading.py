import sys
import importlib


def check_dependencies() -> bool:
    modules = ["pandas", "numpy", "matplotlib"]
    str_ready = [
        "Data manipulation ready",
        "Numerical computation ready",
        "Visualization ready",
    ]
    check_flag = True
    print("Checking dependencies:")
    for module, msg in zip(modules, str_ready):
        try :
            mod = importlib.import_module(module)
            print(f"[OK] {module} ({mod.__version__}) - {msg}")
        except ModuleNotFoundError as e:
            msg = msg.replace("ready", "fail")
            print(f"[KO] {module} - {msg} : {e}")
            check_flag = False
    print()
    if check_flag is False:
        show_installation()
        return check_flag
    return check_flag


def show_installation() -> None:
    msg = (
        "\n\nInstalling with pip\n"
        "$> pip install -r requirements.txt\n"
        "$> python3 loading.py\n"
        "# Should run analysis and create visualization\n\n"
        "Installing with Poetry\n"
        "$> poetry install\n"
        "$> poetry run python loading.py\n"
        "# Should run analysis and create visualization with Poetry"
    )
    print(msg)


def generate_data(n: int) -> tuple["np.ndarray", "np.ndarray"]:

    import numpy as np

    time = np.linspace(0, 10, n)
    signal = np.sin(time)
    noise = np.random.randn(n)
    matrix_signal = signal + noise
    return time, matrix_signal


def create_dataframe(time: "np.ndarray", signal: "np.ndarray") -> "pd.DataFrame":
    import pandas as pd

    df = pd.DataFrame({
        "time": time,
        "signal": signal
    })
    df["time_norm"] = df["time"] / df["time"].max()
    df["abs_signal"] = df["signal"].abs()
    df["smooth"] = df["signal"].rolling(3).mean()
    return df

def generate_vis(df: "pd.DataFrame") -> None:
    import matplotlib.pyplot as plt

    plt.figure(figsize=(10, 5))

    plt.plot(df["time"], df["signal"], label="signal", linewidth=1)
    plt.plot(df["time"], df["smooth"], label="smooth", linestyle="--")

    plt.title("Matrix Signal Analysis")
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.legend()
    plt.grid(True)

    plt.savefig("matrix_analysis.png", dpi=300, bbox_inches="tight")
    plt.close()

if __name__ == "__main__":
    print("LOADING STATUS: Loading programs...\n")
    check = check_dependencies()
    if check is False:
        sys.exit(1)
    n_data = 5
    print("Analyzing Matrix data...")
    data = generate_data(n_data)
    print(f"Processing {n_data} data points...")
    df = create_dataframe(*data)
    print("Generating visualization...")
    generate_vis(df)
    print()
    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")



        

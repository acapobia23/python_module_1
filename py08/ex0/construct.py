import sys
import os

def not_env(py_vers: str) -> None:
    print("MATRIX STATUS: You're still plugged in")
    print("Current Python:", py_vers)
    print("Virtual Environment: None detected")
    print()
    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.")
    print()
    print("To enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate # On Unix")
    print("matrix_env\\Scripts\\activate # On Windows\n")
    print("Then run this program again.")
    


def on_env(py_vers: str) -> None:
    env_name = os.path.basename(os.path.dirname(os.path.dirname(py_vers)))
    env_path = os.path.dirname(os.path.dirname(py_vers))
    version = str(sys.version_info[0]) + "." + str(sys.version_info[1])
    print(version)
    install_path = env_path + "/lib/python" + version + "/site-packages"

    print("MATRIX STATUS: Welcome to the construct")
    print("Current Python:", py_vers)
    print("Virtual Environment:", env_name)
    print("Environment Path:", env_path)
    print()
    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting")
    print("the global system.")
    print()
    print("Package installation path:")
    print(install_path)


if __name__ == "__main__":

    py_vers = sys.executable
    if sys.prefix == sys.base_prefix:
        not_env(py_vers)
    else:
        on_env(py_vers)

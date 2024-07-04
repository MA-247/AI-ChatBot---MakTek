import subprocess

# Function to install dependencies from requirements.txt
def install_requirements():
    try:
        subprocess.check_call(["pip", "install", "-r", "requirements.txt"])
        print("All dependencies have been successfully installed.")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")

install_requirements()


import os

def update_numpy_references():
    # Define the path to the numpy_encoder.py file
    file_path = r"C:\Users\B-DEX\Desktop\DEVOPS AND MLOPS\Mlops_Project_template\env\Lib\site-packages\evidently\utils\numpy_encoder.py"

    # Read the content of the file
    with open(file_path, 'r') as file:
        file_data = file.read()

    # Replace np.float_ with np.float64
    file_data = file_data.replace('np.float_', 'np.float64')

    # Write the modified content back to the file
    with open(file_path, 'w') as file:
        file.write(file_data)

    print("Replacement complete.")

if __name__ == "__main__":
    update_numpy_references()

import kagglehub
import os

# folder curent
current_folder = os.getcwd()

# Download dataset in current folder
path = kagglehub.dataset_download("rangalamahesh/bank-churn", path=current_folder)

print("Path to dataset files:", path)

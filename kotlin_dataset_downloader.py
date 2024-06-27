# pip install gitpython
from git import Repo
from collections import deque
import shutil
import os

# # define raw and output folders
# raw_folder_name = "raw_repos"
# kotlin_file_folder_name = "kotlin_files"
#
# # map folders to download the repos to respective GitHub links
# folder_to_link = {
#     # "kotlin": "https://github.com/JetBrains/kotlin",  # that one is big and takes a while
#     # "v2rayNG": "https://github.com/2dust/v2rayNG",
#     # "Seal": "https://github.com/JunkFood02/Seal",
#     # "KernelSU": "https://github.com/tiann/KernelSU",
#     # "ViMusic": "https://github.com/vfsfitvnm/ViMusic"
# }
#
# # clone the repos to the respective folders
# for repo in folder_to_link:
#     Repo.clone_from(folder_to_link[repo], f"./{raw_folder_name}/{repo}")
#
# # move the .kt files to the test data folder (using dfs in this case)
# os.makedirs(kotlin_file_folder_name)
# q = deque([raw_folder_name])
# curr_num = 0
# while q:
#     curr = q.popleft()
#     for root, dirs, files in os.walk(curr, topdown=True):
#         for name in files:
#             if name.endswith(".kt"):
#                 os.rename(os.path.join(root, name), f"kotlin_files/{str(curr_num)}{name}")
#                 curr_num += 1
#         for name in dirs:
#             q.append(name)
#
# # zip kotlin files
# shutil.make_archive(kotlin_file_folder_name, 'zip', kotlin_file_folder_name)

Repo.clone_from("https://github.com/microsoft/CodeXGLUE", f"./concode")

import os
import sys
import json
import numpy as np

data_root = "./data/PuzzleIOI/fitting"
error_file = "./data/PuzzleIOI/error.txt"
# error_lst = np.loadtxt(error_file, dtype=str)

# with open("./data/PuzzleIOI/error.txt", "a") as e:
#     with open("./data/PuzzleIOI/subjects_all.txt", "r") as f:
#         for subject in os.listdir(data_root):
#             for motion in os.listdir(os.path.join(data_root, subject)):
#                 line_path = '/'.join(os.path.join(data_root, subject, motion).split('/')[2:])
#                 line = f"{line_path} {subject} {motion}\n"
#                 json_file = os.path.join(data_root, subject, motion, "gpt4v_response.json")
#                 if not os.path.exists(json_file):
#                     if line_path not in error_lst[:,0]:
#                         e.write(line)
#                         print(f"{line_path} not exists")
#                 else:
#                     try:
#                         with open(json_file, 'r') as j:
#                             json_data = json.loads(j.read())
#                         if "gender" not in json_data.keys():
#                             if line_path not in error_lst[:,0]:
#                                 e.write(line)
#                                 print(f"{line_path} wrong keys")
#                     except:
#                         if line_path not in error_lst[:,0]:
#                             e.write(line)
#                             print(f"{line_path} wrong json")


with open("./data/PuzzleIOI/subjects_test.txt", "w") as f:
    for subject in os.listdir(data_root):
        motions = os.listdir(os.path.join(data_root, subject))
        motions.remove("apose")
        motions.remove("full.jpg")
        for motion in np.random.choice(motions, 3, replace=False):
            os.makedirs(os.path.join("./logs", subject, motion), exist_ok=True)
            line_path = '/'.join(os.path.join(data_root, subject, motion).split('/')[2:])
            line = f"{line_path.replace('fitting', 'puzzle_capture')} {subject} {motion}\n"
            f.write(line)

                
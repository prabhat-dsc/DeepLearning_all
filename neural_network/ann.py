import os


dir="cnn_network"
os.makedirs(dir,exist_ok=True)
file_path=os.path.join(dir,"cnn.py")
code = """\
def cnn_model():
    print("This is a dummy CNN model.")

cnn_model()
"""

with open(file_path,'w') as f:
  f.write(code)
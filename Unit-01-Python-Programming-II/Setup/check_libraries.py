libraries = [
    "numpy",
    "pandas",
    "matplotlib",
    "sklearn",
    "seaborn",
    "openpyxl",
    "jupyter",
    "notebook",
    "plotly",
    "scipy",
    "cv2",
    "PIL"
]

print("=" * 50)
print("Checking Installed Libraries")
print("=" * 50)

for lib in libraries:
    try:
        __import__(lib)
        print(f"[OK] {lib} : Installed")
    except ImportError:
        print(f"[ERROR] {lib} : NOT Installed")

print("=" * 50) 

# python check_libraries.py 
# Example output:
# ==================================================
# Checking Installed Libraries
# ==================================================
#  numpy : Installed
#  pandas : Installed
#  matplotlib : Installed
#  sklearn : Installed
#  seaborn : Installed
#  openpyxl : Installed
#  jupyter : Installed
#  notebook : Installed
#  plotly : Installed
#  scipy : Installed
#  cv2 : Installed
#  PIL : Installed
# ==================================================

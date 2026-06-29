import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
import os

nb_path = 'Notebooks/Instagram_Analytics_Alfido_Tech.ipynb'
output_path = 'Notebooks/Instagram_Analytics_Alfido_Tech.ipynb'

os.makedirs('exports', exist_ok=True)
os.makedirs('visualizations', exist_ok=True)

print(f"Reading notebook: {nb_path}")
try:
    with open(nb_path, encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)
except FileNotFoundError:
    print(f"Error: {nb_path} not found.")
    exit(1)

ep = ExecutePreprocessor(timeout=600, kernel_name='python3')

print("Executing analysis pipeline... Generating 25+ plots and exporting datasets.")
try:
    ep.preprocess(nb, {'metadata': {'path': 'Notebooks/'}})
    print("✅ Analysis completed successfully.")
except Exception as e:
    print(f"❌ Error during execution: {e}")
finally:
    print(f"Saving results to: {output_path}")
    with open(output_path, 'w', encoding='utf-8') as f:
        nbformat.write(nb, f)

print("Done. Check 'visualizations/' and 'exports/' folders for output.")

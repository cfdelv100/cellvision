from pathlib import Path
from src.data.stats import analyze_dataset

dataset = Path("data/raw/bccd")

result = analyze_dataset(dataset)
print(result)
import random
from datasets import load_dataset

dataset = load_dataset("evalplus/humanevalplus", split="test")

random.seed(42)
sampled = dataset.shuffle(seed=42).select(range(10))

with open("problems.txt", "w") as f:
    for i, item in enumerate(sampled):
        f.write(f"\n{'='*60}\n")
        f.write(f"Problem {i+1} (ID: {item['task_id']})\n")
        f.write(f"{'='*60}\n")
        f.write("Prompt:\n\n")
        f.write(item["prompt"])
        f.write("\n\nCanonical Solution:\n\n")
        f.write(item["canonical_solution"])
        f.write("\n")
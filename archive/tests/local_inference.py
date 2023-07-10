# pip install -q transformers
from transformers import AutoModelForCausalLM, AutoTokenizer

checkpoint = "bigscience/bloomz-560m"

tokenizer = AutoTokenizer.from_pretrained(checkpoint)
model = AutoModelForCausalLM.from_pretrained(checkpoint)

inputs = tokenizer.encode("Write a fairy tale about a troll saving a princess from a dangerous dragon. Story:", return_tensors="pt")
outputs = model.generate(inputs)
print(tokenizer.decode(outputs[0]))
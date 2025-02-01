import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

class CodeLlamaModel:
    def __init__(self, model_name: str = "codellama/CodeLlama-7b-hf"):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name).to(self.device)

    def generate_code(self, prompt: str, max_length: int = 512) -> str:
        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.device)
        outputs = self.model.generate(inputs["input_ids"], max_length=max_length)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)
from model import CodeLlamaModel

def generate_code(prompt: str) -> str:
    model = CodeLlamaModel()
    return model.generate_code(prompt)
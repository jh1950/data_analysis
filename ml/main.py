import torch

from .models import RNN



class ML:
    def __init__(self, NM, device="cpu"):
        self.device = "cuda" if device in ["cuda", "gpu"] and torch.cuda.is_available() else "cpu"
        self.model = MODEL_CLASS[NM]["model"]
        self.loader = MODEL_CLASS[NM]["loader"]
        self.trainer = MODEL_CLASS[NM]["trainer"]
        self.predicter = MODEL_CLASS[NM]["predicter"]
        self.agg = MODEL_CONFIG[NM]

    def train(self):
        return 0

    def validation(self):
        pass

    def predict(self, x):
        return len(x)



MODEL_CLASS = { 
    "NN01": {
        "model": RNN,
        "loader": "provider",
        "trainer": "training",
        "validater": "validation",
        "predicter": "prediction",
    },
}

MODEL_CONFIG = {
    "NN01": {
        "batch_size": 16,
        "hidden_sizes": [288, 192, 144, 96, 32],
        "max_learning_rate": 0.001,
        "epochs": 100,
        "input_size": 0,
        "seq_len": 0,
        "dropout": 0.5,
        "output_size": 1,
        "save_path": "./",
    },
}

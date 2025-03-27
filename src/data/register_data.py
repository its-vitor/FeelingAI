import pandas as pd
import os

class RegisterData:
    def __init__(self, path: str):
        base_path = os.path.dirname(os.path.abspath(__file__))
        datasets_path = os.path.join(base_path, "datasets")
        os.makedirs(datasets_path, exist_ok=True)
        self.path = os.path.join(datasets_path, path)


    def register(self, data: dict):
        dataFrame = pd.DataFrame([data])

        try:
            existing_data = pd.read_csv(self.path)
            updated_data = pd.concat([existing_data, dataFrame], ignore_index=True)
            updated_data.to_csv(self.path, index=False)
        except FileNotFoundError:
            dataFrame.to_csv(self.path, index=False)
        except Exception as e:
            print(f"Houve um erro ao registrar: {e}")
    
    def registerPositive(self, message: str):
        self.register({
            "text": message,
            "feeling": "positive"
        })

    def registerNegative(self, message: str):
        self.register({
            "text": message,
            "feeling": "negative"
        })
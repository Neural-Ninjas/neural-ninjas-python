import os

class NeuralNinjas:
    def __init__(self):
        self.api_key = os.environ['NEURAL_NINJAS_API_KEY']
    
    def init(self, project):
        # Make API call to Neural Ninjas
        # Return run_id
        pass

    def log_metrics(self, metrics: dict):
        # Make API call to Neural Ninjas
        pass

    def log_artifact(self, type: str, path: str):
        # Make API call to Neural Ninjas
        pass

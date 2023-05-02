from typing import Dict, Optional

from neural_ninjas.api.neural_ninjas import NeuralNinjas


try:
    from lightning.pytorch.loggers.logger import Logger
    from lightning.pytorch.utilities import rank_zero_only
except ModuleNotFoundError:
    Logger, rank_zero_only = None, None


class NeuralNinjasLogger(Logger):
    def __init__(
        self,
        project: str = "lightning_logs",
        id: Optional[str] = None,
    ):
        super().__init__()
        self._project = project
        self._id = id
        self._logged_model_time: Dict[str, float] = {}
    
    @property
    def experiment(self):
        return NeuralNinjas()

    @property
    def name(self):
        return self._project

    @property
    def version(self):
        # Return the experiment version, int or str.
        return self._id

    @rank_zero_only
    def log_hyperparams(self, params):
        # params is an argparse.Namespace
        # your code to record hyperparameters goes here
        pass

    @rank_zero_only
    def log_metrics(self, metrics, step):
        # metrics is a dictionary of metric names and values
        # your code to record metrics goes here
        pass

    @rank_zero_only
    def save(self):
        # Optional. Any code necessary to save logger data goes here
        pass

    @rank_zero_only
    def finalize(self, status):
        # Optional. Any code that needs to be run after training
        # finishes goes here
        pass

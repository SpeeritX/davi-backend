from data.load_pandas import load_dataset


class Flights:
    def __init__(self):
        self.df = load_dataset()
        print("Dataset is ready...")

    @property
    def oblasts(self):
        return list(self.df.oblast.unique())

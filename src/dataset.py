import torch

class CustomDataset:
    """Custom Dataset"""

    def __init__(self, x, y):
        """
        Args:
            x:  categorical dataframe
            y: target values
        """
        self.x = x
        self.y = y
        

    def __len__(self):
        return self.x.shape[0]

    def __getitem__(self, idx):
        current_sample = self.x[idx,:]
        current_target = self.y[idx]
        return{
            "x" : torch.tensor(current_sample, dtype = torch.float),
            "y" : torch.tensor(current_target, dtype = torch.long)

        }
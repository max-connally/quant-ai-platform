import torch
import torch.nn as nn

class PricePredictor(nn.Module):

    def __init__(self, input_size=5):

        super().__init__()

        self.lstm = nn.LSTM(input_size, 32, batch_first=True)

        self.fc = nn.Linear(32, 1)

    def forward(self, x):

        out, _ = self.lstm(x)

        out = self.fc(out[:, -1, :])

        return out


def predict_price_change(df):

    returns = df["returns"].tail(10)

    return returns.mean()

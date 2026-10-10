import numpy as np
import torch
import torch.nn as nn
import matplotlib.pyplot as plt
from torch.utils.data import DataLoader, TensorDataset
import torch.nn.functional as F

inputs = np.array([[73, 67, 43],
                   [91, 88, 64],
                   [87, 134, 58],
                   [102, 43, 37],
                   [69, 96, 70],
                   [74, 66, 43],
                   [91, 87, 65],
                   [88, 134, 59],
                   [101, 44, 37],
                   [68, 96, 71],
                   [73, 66, 44],
                   [92, 87, 64],
                   [87, 135, 57],
                   [103, 43, 36],
                   [68, 97, 70]], dtype='float32')

# Targets (apples, oranges)
targets = np.array([[56, 70],
                    [81, 101],
                    [119, 133],
                    [22, 37],
                    [103, 119],
                    [57, 69],
                    [80, 102],
                    [118, 132],
                    [21, 38],
                    [104, 118],
                    [57, 69],
                    [82, 100],
                    [118, 134],
                    [20, 38],
                    [102, 120]], dtype='float32')

inputs = torch.from_numpy(inputs)
targets = torch.from_numpy(targets)


train_ds = TensorDataset(inputs, targets)

batch_size = 15
train_dl = DataLoader(train_ds, batch_size, shuffle=True)

model = nn.Linear(3, 2)
print(model.weight)
print(model.bias)

# preds = model(inputs)
# print(preds)
# print(targets)

loss_fn = F.mse_loss
# loss = loss_fn(preds, targets)
# print('Loss of the prediction: ', loss)

opt = torch.optim.SGD(
    model.parameters(), lr=1e-5)


def fit(num_epoch, model, loss_fn, opt, train_dl):

    for epoch in range(num_epoch):
        for xb, yb in train_dl:
            pred = model(xb)

            loss = loss_fn(pred, yb)
            loss.backward()
            opt.step()
            opt.zero_grad()

        if (epoch + 1) % 100 == 0:
            print(f'Epoch: {epoch+1}, Loss: {loss.item():.4f}')
        elif epoch is 0:
            print(f'Epoch: {epoch+1}, Loss: {loss.item():.4f}')


fit(1000, model, loss_fn, opt, train_dl)

preds = model(inputs)
print(preds)
print(targets)

new_row = torch.tensor([75, 63, 44.]).view(-1, 3)
print(new_row)

new_preds = model(new_row)
print(new_preds)


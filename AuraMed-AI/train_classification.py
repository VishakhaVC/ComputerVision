import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from torchvision import datasets, models, transforms

# 1. Image Preprocessing Pipelines
data_transforms = {
    'train': transforms.Compose([
        transforms.RandomResizedCrop(224),
        transforms.RandomHorizontalFlip(),
        transforms.RandomRotation(15),
        transforms.ColorJitter(brightness=0.2, contrast=0.2), # Augmentations for varied lighting
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ]),
    'val': transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ]),
}

def load_data(data_dir, batch_size=8):
    image_datasets = {
        x: datasets.ImageFolder(f"{data_dir}/{x}", data_transforms[x]) 
        for x in ['train', 'val']
    }
    
    dataloaders = {
        x: DataLoader(image_datasets[x], batch_size=batch_size, shuffle=True, num_workers=4)
        for x in ['train', 'val']
    }
    
    dataset_sizes = {x: len(image_datasets[x]) for x in ['train', 'val']}
    class_names = image_datasets['train'].classes
    
    return dataloaders, dataset_sizes, class_names

def train_model(data_dir, epochs=15):
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print(f"Device set to: {device}")
    
    # dataloaders, dataset_sizes, class_names = load_data(data_dir)
    # 4 Classes: Early, Healing, Infected, Healed
    num_classes = 4  # e.g., len(class_names)
    
    # 2. Build Model (EfficientNet-B0)
    model = models.efficientnet_b0(pretrained=True)
    
    # Replace last layer with our classifications
    num_ftrs = model.classifier[1].in_features
    model.classifier[1] = nn.Linear(num_ftrs, num_classes)
    model = model.to(device)
    
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=1e-4) # Adam preferred for smooth convergence
    
    # 3. Training Loop Example
    for epoch in range(epochs):
        model.train()
        print(f"Epoch {epoch}/{epochs}")
        # for inputs, labels in dataloaders['train']:
        #     inputs = inputs.to(device)
        #     labels = labels.to(device)
        #     optimizer.zero_grad()
        #     outputs = model(inputs)
        #     loss = criterion(outputs, labels)
        #     loss.backward()
        #     optimizer.step()
        print(f"Mock Validating...")

    # torch.save(model.state_dict(), 'best_wound_classifier.pth')
    print("Training Complete.")


if __name__ == "__main__":
    # Point data_dir to your prepared dataset structured as:
    # dataset/
    # ├── train/
    # │   ├── early/
    # │   ├── healing/
    # │   ├── infected/
    # │   └── healed/
    # └── val/ ...
    train_model(data_dir="dataset_path")

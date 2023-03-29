import transformers
import torch
import pandas as pd
from sklearn import preprocessing


# Adatok betöltése a Dry Bean Dataset-ből
data = pd.read_excel("./DryBeanDataset/Dry_Bean_Dataset.xlsx")


# Oszlopnevek megadása
data.columns = ["Area", "Perimeter", "MajorAxisLength", "MinorAxisLength", 
                "AspectRatio", "Eccentricity", "ConvexArea", "EquivDiameter", 
                "Extent", "Solidity", "Roundness", "Compactness", "ShapeFactor1", 
                "ShapeFactor2", "ShapeFactor3", "ShapeFactor4", "Class"]

# Letöltjük a pre-trained GPT-2 modellt
model = transformers.GPT2Model.from_pretrained("gpt2")

# Hozzáadjuk az optimizátort
optimizer = torch.optim.Adam(model.parameters(), lr=1e-5)

# Hozzáadjuk a hiba mérőt
criterion = torch.nn.CrossEntropyLoss()

# Adatok előkészítése
encoder = preprocessing.LabelEncoder()

for column in data.columns:
    data[column] = encoder.fit_transform(data[column])

# data["Area"] = encoder.fit_transform(data["Area"])
# data["Perimeter"] = encoder.fit_transform(data["Perimeter"])
# data["MajorAxisLength"] = encoder.fit_transform(data["MajorAxisLength"])
# data["MinorAxisLength"] = encoder.fit_transform(data["MinorAxisLength"])
# data["AspectRatio"] = encoder.fit_transform(data["AspectRatio"])
# data["Eccentricity"] = encoder.fit_transform(data["Eccentricity"])
# data["ConvexArea"] = encoder.fit_transform(data["ConvexArea"])
# data["EquivDiameter"] = encoder.fit_transform(data["EquivDiameter"])
# data["Extent"] = encoder.fit_transform(data["Extent"])
# data["Solidity"] = encoder.fit_transform(data["Solidity"])
# data["Roundness"] = encoder.fit_transform(data["Roundness"])
# data["Compactness"] = encoder.fit_transform(data["Compactness"])
# data["ShapeFactor1"] = encoder.fit_transform(data["ShapeFactor1"])
# data["ShapeFactor2"] = encoder.fit_transform(data["ShapeFactor2"])
# data["ShapeFactor3"] = encoder.fit_transform(data["ShapeFactor3"])
# data["ShapeFactor4"] = encoder.fit_transform(data["ShapeFactor4"])

# A cél oszlopát átalakítjuk számokká
# class_encoder = preprocessing.LabelEncoder()
# data["class"] = class_encoder.fit_transform(data["class"])

# A train_data változóba töltjük az adatokat
train_data = data[["Area", "Perimeter", "MajorAxisLength", "MinorAxisLength", 
                "AspectRatio", "Eccentricity", "ConvexArea", "EquivDiameter", 
                "Extent", "Solidity", "Roundness", "Compactness", "ShapeFactor1", 
                "ShapeFactor2", "ShapeFactor3", "ShapeFactor4", "Class"]].values

# Adatok előkészítése

for column in data.columns:
    data[column] = encoder.fit_transform(data[column])

# data["Area"] = encoder.transform(data["Area"])
# data["Perimeter"] = encoder.transform(data["Perimeter"])
# data["MajorAxisLength"] = encoder.transform(data["MajorAxisLength"])
# data["MinorAxisLength"] = encoder.transform(data["MinorAxisLength"])
# data["AspectRatio"] = encoder.transform(data["AspectRatio"])
# data["Eccentricity"] = encoder.transform(data["Eccentricity"])
# data["ConvexArea"] = encoder.transform(data["ConvexArea"])
# data["EquivDiameter"] = encoder.transform(data["EquivDiameter"])
# data["Extent"] = encoder.transform(data["Extent"])
# data["Solidity"] = encoder.transform(data["Solidity"])
# data["Roundness"] = encoder.transform(data["Roundness"])
# data["Compactness"] = encoder.transform(data["Compactness"])
# data["ShapeFactor1"] = encoder.transform(data["ShapeFactor1"])
# data["ShapeFactor2"] = encoder.transform(data["ShapeFactor2"])
# data["ShapeFactor3"] = encoder.transform(data["ShapeFactor3"])
# data["ShapeFactor4"] = encoder.transform(data["ShapeFactor4"])
# data["class"] = encoder.transform(data["class"])


# A val_data változóba töltjük az adatokat
val_data = data[["Area", "Perimeter", "MajorAxisLength", "MinorAxisLength", 
                "AspectRatio", "Eccentricity", "ConvexArea", "EquivDiameter", 
                "Extent", "Solidity", "Roundness", "Compactness", "ShapeFactor1", 
                "ShapeFactor2", "ShapeFactor3", "ShapeFactor4","Class"]].values

train_data = data[["Area", "Perimeter", "MajorAxisLength", "MinorAxisLength", 
                "AspectRatio", "Eccentricity", "ConvexArea", "EquivDiameter", 
                "Extent", "Solidity", "Roundness", "Compactness", "ShapeFactor1", 
                "ShapeFactor2", "ShapeFactor3", "ShapeFactor4","Class"]]
input_ids = train_data.values
labels = data["Class"].values


num_epochs = 5
# Tanítási ciklus
for epoch in range(num_epochs):
    # Tanítási adatok végigjárása
    for data in train_data:
        # Adatok előkészítése
        # input_ids, labels = data

        input_ids = train_data.values
        labels = data.Class.values
        # labels = data["Class"].values

        # Nullázzuk a gradienst
        optimizer.zero_grad()

        # Előrejelzés
        logits = model(input_ids)

        # Kiszámítjuk a hibát
        loss = criterion(logits.view(-1, logits.size(-1)), labels.view(-1))

        # Visszajelzés
        loss.backward()

        # Optimizálás
        optimizer.step()

    # Validáció
    total_val_loss = 0
    for data in val_data:
        input_ids, labels = data
        with torch.no_grad():
            logits = model(input_ids)
            total_val_loss += criterion(logits.view(-1, logits.size(-1)), labels.view(-1))

    # Nyomtatjuk a tanítási információt
    print("Epoch {}/{} Loss {:.4f} Validation Loss {:.4f}".format(epoch + 1, num_epochs, loss.item(), total_val_loss / len(val_data)))

# Minecraft Building Classifier

## Description

This project is a Minecraft building classifier that uses machine learning to identify and classify different types of buildings in Minecraft based on schematic files. The classifier takes into account the 3D information, including the spatial dimensions (length, width, height) and block types, to determine the building type.

## Table of Contents

- [Description](#description)
- [Table of Contents](#table-of-contents)
- [Installation](#installation)
- [Usage](#usage)
- [Data](#data)
- [Model](#model)
- [Training](#training)
- [Evaluation](#evaluation)
- [Results](#results)
- [Future Work](#future-work)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Installation

1. Clone the repository:

```
git clone https://github.com/gwerneckpaiva/minecraft-building-classifier.git
cd minecraft-building-classifier
```

2. Install the required dependencies:

```
pip install -r requirements.txt
```

## Usage

To use the Minecraft building classifier, follow these steps:

1. Prepare your schematic files and place them in the `schematics/` directory.
2. Modify the `config.py` file to specify the desired model hyperparameters, dataset path, and other settings.
3. Run the training script to train the classifier:

```
python train.py
```

4. After training, you can use the trained model to classify new schematic files:

```
python classify.py --file path/to/new_schematic.schematic
```

## Data

The dataset used for training and evaluation consists of Minecraft schematic files (`.schematic`) representing various types of buildings. The schematic files contain 3D information with block IDs for each position in the building.

Please note that the dataset used in this project is not provided in the repository due to licensing and size constraints. You can create your own dataset by collecting schematics of different building types or adapt an existing Minecraft schematic dataset.

## Model

The classifier utilizes a neural network with multiple layers for building classification. The model architecture includes a flatten layer as the input layer, followed by fully connected (linear) layers with ReLU activation functions.

## Training

The training script reads the dataset of schematic files, preprocesses the data, and trains the neural network using PyTorch. The model is trained to minimize the cross-entropy loss, and an appropriate optimizer is used for parameter updates.

## Evaluation

The trained model is evaluated on a separate test set of schematic files to assess its performance. Evaluation metrics such as accuracy, precision, recall, and F1 score are used to measure the classifier's effectiveness.

## Results

The classifier's performance on the test set is summarized in the `results/` directory. Additionally, some example predictions on new schematic files are provided in the `predictions/` directory.

## Future Work

Potential areas for future improvement and expansion of the project:

- Experiment with different neural network architectures, including 3D convolutional networks, to capture spatial patterns more effectively.
- Explore data augmentation techniques to increase the diversity of the training dataset.
- Develop a graphical user interface (GUI) for easier classification of new schematic files.

## Contributing

Contributions to the project are welcome! If you find any issues or have ideas for improvements, feel free to create a pull request or open an issue.

## License

[MIT License](LICENSE)

## Contact

For any inquiries or questions, please contact [Gabriel Werneck Paiva](mailto:gwerneckpaiva@gmail.com).

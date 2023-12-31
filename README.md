# AudioDeepFakeDetection

Application that detects the originality of audio files with artificial intelligence.

## Setup Environment

```bash
# Make sure your PIP is up to date
pip install -U pip wheel setuptools

# Install required dependencies
pip install -r requirements.txt
```

## Setup Datasets

You may download the datasets used in the project from the following URL:

https://drive.google.com/file/d/1O_PckJtEbQWlHEMSA5gDdxRooa1S1N2p/view

-   (Real) Human Voice Dataset:
    -   This dataset consists of 10.000 short audio clips of a single speaker reading passages from 7 non-fiction books.
-   (Fake) Synthetic Voice Dataset: 
    -   The dataset consists of fake audio clips (16-bit PCM wav).

After downloading the datasets, you may extract them under `data/real` and `data/fake` respectively. In the end, the `data` directory should look like this:

```
data
├── real
    └── LJ001-0001
    └── LJ001-0002
    └── LJ001-0003
    └── LJ001-0004
    └── LJ001-0005
    └── LJ001-0006
    ...
└── fake
    └── LJ001-0001_gen
    └── LJ001-0002_gen
    └── LJ001-0003_gen
    └── LJ001-0004_gen
    └── LJ001-0005_gen
    └── LJ001-0006_gen
    ...
```

## Application

You can run the file named [main.py](main.py) and load your audio file and test whether the file is real or not.

![start](https://github.com/onurkya7/AudioDeepFakeDetection/assets/100594545/caec9967-ccea-4e52-b550-76755a0c0305)

## License

Our project is licensed under the [MIT License](LICENSE).




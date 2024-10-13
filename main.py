import pandas as pd


def prepare_dataset():
    df = pd.read_csv('./datasets/titanic.csv')
    df = df[['Pclass', 'Sex', 'Age']]
    print(df.head())
    df.to_csv('./datasets/titanic.csv', index=False)


if __name__ == "__main__":
    prepare_dataset()


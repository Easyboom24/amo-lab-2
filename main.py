import pandas as pd


def prepare_dataset():
    df = pd.read_csv('./datasets/titanic.csv')
    print(df.head())

    df = df[['Pclass', 'Sex', 'Age']]
    print(df.head())

    df.to_csv('./datasets/titanic.csv', index=False)


def get_mean_age():
    df = pd.read_csv('./datasets/titanic.csv')
    print(df.info())
   
    mean_age = round(df['Age'].mean(), 1)
    print("Mean Age",mean_age)

    df['Age'].fillna(mean_age, inplace=True)
    print(df.info())

    df.to_csv('./datasets/titanic.csv', index=False)    


if __name__ == "__main__":
    # prepare_dataset()
    get_mean_age()


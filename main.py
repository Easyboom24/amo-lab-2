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



def get_one_hot_for_sex_column():
    df = pd.read_csv('./datasets/titanic.csv')
    print(df.info())

    df_encoded = pd.get_dummies(df, columns=['Sex'], drop_first=True, prefix='Sex')
    df_encoded['Sex'] = df['Sex']
    print(df_encoded.info())

    df_encoded.to_csv('./datasets/titanic.csv', index=False)


if __name__ == "__main__":
    # prepare_dataset()
    # get_mean_age()
    get_one_hot_for_sex_column()


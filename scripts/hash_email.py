import pandas as pd
def hash_email(df, column):
    df[column] = df[column].apply(lambda s: s[0]+ '****' + s[s.find('@'):])

#Test
Test = pd.DataFrame({'Email':['lamba@mail.ru', 'kri@yandex.ru']})
hash_email(Test, 'Email')
print(Test)

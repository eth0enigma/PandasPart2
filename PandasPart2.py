import pandas as pd

### Import 3 dataframes for our example
df = pd.read_csv('example1.csv')
print("................First Example DataFrame...................")
print(df.head(3))
print("................Second Example DataFrame...................")
df2 = pd.read_csv('example2.csv')
print(df2.head(3))
print("..................County Lookup.................")
dflookup = pd.read_csv('lookup.csv')
print(dflookup.head())
print("..................Combine DF and DF2 DataFrame.................")

## Syntax to convert dictionart to DataFrame  
#df_fromDictionary = pd.DataFrame(Dictionary_Example)


## Appending df2 to original DataFrame ####
df = df.append(df2)
print(df.head(6))
print("....................Merged DataFrame with Lookup...............")

### for how you can set it to inner, left or right
df = pd.merge(df, dflookup, how = 'left', left_on= ['City', 'State'], right_on = ['BUYCITY', 'BUYSTATE'])
print(df.head(6))
# this will join two dataframe by index values Have not found a reason to use this over Merge
#df = df.join(df2)


def Scorelevel(df):
    if df['Score'] >= 9:
        return 'Can\'t Loose Them'
    elif ((df['Score'] >= 8) and (df['Score'] < 9)):
        return 'Champions'
    elif ((df['Score'] >= 7) and (df['Score'] < 8)):
        return 'Loyal'
    elif ((df['Score'] >= 6) and (df['Score'] < 7)):
        return 'Potential'
    elif ((df['Score'] >= 5) and (df['Score'] < 6)):
        return 'Promising'
    elif ((df['Score'] >= 4) and (df['Score'] < 5)):
        return 'Needs Attention'
    else:
        return 'Require Activation'

df['Score_Level'] = df.apply(Scorelevel, axis=1)


### outputing rows without internal index.
df.to_csv('Output.csv', index = False)

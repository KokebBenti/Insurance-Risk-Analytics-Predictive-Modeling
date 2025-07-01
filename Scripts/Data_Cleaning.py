def drop_col(df,column):
 df.drop(columns=column, inplace=True)
 return df

def impute_rows(df):
 from sklearn.impute import SimpleImputer
 imputer = SimpleImputer(strategy='most_frequent')
 imputer2= SimpleImputer(strategy='median')
 cat_cols = df.select_dtypes(include=['object', 'category',"bool"]).columns
 num_cols = df.select_dtypes(include=['float64', 'int64']).columns
 df[cat_cols] = imputer.fit_transform(df[cat_cols])
 df[num_cols] = imputer2.fit_transform(df[num_cols]) 
 return df


def change_type(df):
 import pandas as pd
 df['TransactionMonth']=pd.to_datetime(df['TransactionMonth']) 
 return df


def encoder(df):
 from sklearn.preprocessing import LabelEncoder
 cat_cols = df.select_dtypes(include=['object', 'category','bool']).columns
 le = LabelEncoder()
 for col in cat_cols:
    df[col] = le.fit_transform(df[col])
 return df 


def scale_data(df):
 from sklearn.preprocessing import StandardScaler
 std_scaler = StandardScaler()
 num_cols = df.select_dtypes(include=['float64']).columns
 df_scaled =std_scaler.fit_transform(df[num_cols])  
 return df   

def test_data(df):
 from sklearn.model_selection import train_test_split
 train_set, test_set = train_test_split(df, test_size=0.2, random_state=42) 
 return (train_set, test_set) 
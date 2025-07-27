def drop_col(df,column):
 df.drop(columns=column, inplace=True)
 return df

def test_data(df):
 from sklearn.model_selection import train_test_split
 train, test = train_test_split(df, test_size=0.2, random_state=42) 
 return (train, test)  

def impute_rows(df):
 from sklearn.impute import SimpleImputer
 imputer = SimpleImputer(strategy='most_frequent')
 imputer2= SimpleImputer(strategy='median')
 cat_cols = df.select_dtypes(include=['object', 'category',"bool"]).columns
 num_cols = df.select_dtypes(include=['float64', 'int64']).columns
 df[cat_cols] = imputer.fit_transform(df[cat_cols])
 df[num_cols] = imputer2.fit_transform(df[num_cols]) 
 return df,imputer,imputer2


def change_type(df):
 import pandas as pd
 df['TransactionMonth']=pd.to_datetime(df['TransactionMonth']) 
 return df

def scale_data(df,col): 
  from sklearn.preprocessing import StandardScaler
  std_scaler = StandardScaler()
  df[col] =std_scaler.fit_transform(df[col]) 
  return df, std_scaler 

  
def encoder(df):
 from scipy import sparse
 import pandas as pd
 from sklearn.preprocessing import OneHotEncoder
 cat_cols = df.select_dtypes(include=['object', 'category','bool']).columns
 num_df = df.drop(columns=cat_cols)
 X_num = sparse.csr_matrix(num_df.values)
 ohe = OneHotEncoder(handle_unknown='ignore', sparse_output=True)
 ohe_array = ohe.fit_transform(df[cat_cols])
 ohe_cat_cols = ohe.get_feature_names_out(cat_cols).tolist()
 X_all = sparse.hstack([X_num,ohe_array])
 all_cols=list(num_df.columns)+ohe_cat_cols
 print(ohe_cat_cols)
 df_fin = pd.DataFrame.sparse.from_spmatrix(X_all, columns=all_cols)
 return df_fin,ohe 


 

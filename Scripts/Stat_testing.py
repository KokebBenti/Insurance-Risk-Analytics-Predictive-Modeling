def separate_claims(df,categories,types,important_columns):
  dictionary_for_claims = {}
  for category in (categories):
    name=str(category)+"_claims"
    value=df[df[types]==str(category)][important_columns]
    dictionary_for_claims[name] = value
  return dictionary_for_claims

def separate_claims_numerical(df,categories,types,important_columns):
  dictionary_for_claims = {}
  for category in (categories):
    name=str(category)+"_claims"
    value=df[df[types]==category][important_columns]
    dictionary_for_claims[name] = value
  return dictionary_for_claims


def anova_test(data):
 from scipy import stats 
 f_stat, p_value_anova = stats.f_oneway(*data.values()) 
 return p_value_anova

def t_test(data):
 from scipy import stats 
 t_stat, p_value_ttest = stats.ttest_ind(*data.values()) 
 return p_value_ttest
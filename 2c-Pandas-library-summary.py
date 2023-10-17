df['col'].unique()	# unique values for col
df.nunique()		# count unique values
df.columns
len(df.columns)
df.apply(pd.unique)			# unique values for each column
df["col"].value_counts()		# count unique values for a column
df["col"].value_counts(normalize=True)	# %
df[['state', 'grade']].value_counts()['U.S.']		# count unique values for each combination of the 2 columns, then return only rows with US for the 1st col
df[df['state'] == 'U.S.']['grade'] == 'A-'		# column grade of all rows with US as value for state col, compare each value with 'A-'
df.drop(['cycle','branch'], axis=1, inplace=True)
df.rename(columns = renaming_dic, inplace = True) 	# key=current, value=new
df.isnull().sum() 		# counting missing values
df.isnull().any()		# true/false if column has missing values
df[df.isnull().any(axis=1)] 	# print rows with missing values 
	isna = isnull 		# Series & DataFrames, Series; prefer isna
df[df['col'].isnull()] 		# print rows with missing values on specific column
df[df['col'].notnull()]		# print rows without missing values on specific column
df[df.isnull().any(axis = 1)].shape[0] 	# counting missing value records
df.dropna()				# drop rows with 1+ missing values, returns new dataframe
df[df.isnull().sum(axis=1) > 1] 	# display rows containing 2+ missing fields
df.dropna(thresh=2 , inplace=False)		# drop rows with 2+ missing values
df.dropna(subset = ['col'], inplace =False)	# drop rows with missing values on the column
df['col'].fillna(value = df['col'].mean(), inplace=True)	# imputation with mean
df.fillna(method = "ffill", limit=2, inplace=True)	# forward fill: fill with previous value, limit of 2 consecutive nans
df.interpolate(method='linear')			# fill nan values with interpolation method
df[date_cols] = df[date_cols].apply(pd.to_datetime)	# convert columns to datetime
df = pd.read_csv("dataset.csv", parse_dates=date_cols)	# read dataset with columns as datetime
df['col'] = df['col'].astype(int)	# parse column as int
df[df['col'] > 500]			# get outliers
df[df['col'] > 500].sort_values(by='col', ascending=False)	# sort rows by column
df.describe().T				# describe and transpose
df.plot(x='col1', y='col2')		# plot line graph with cols x-y
df.loc[df['col'] > 500, 'col'] = df['col'].mean()	# replace outliers with mean of same column
df.duplicated() 				# False for first occurrence and True for every duplicate after
df.duplicated(subset=['brand'], keep=last)   	# finds duplicates on specific col , only last occurrence is False
df.drop_duplicates() 				# remove rows with duplicates in any col
df.drop_duplicates(subset=['brand']) 		# remove duplicates based on specific col







import pandas as pd

# data exploring
class Explore:
    def __init__(self, df):
        self.df = df
        
    # check shape of the data
    def shape(self):
        print('----------------Shape of the Dataset---------------- \n')
        print(self.df.shape)
     
    # check features in the data
    def features(self):
        print('----------------Features in the Dataset---------------- \n')
        print(self.df.columns)
        
    # Check summary statistics
    def stats(self):
        print('----------------Summary Statistics of the Features---------------- \n')
        print(self.df.describe()) 
    
    # check info on dataset
    def info(self):
        print('----------------Dataset Overall Information---------------- \n')
        print(self.df.info())


# data cleaning
class Clean(Explore):
    
    # check for missing values percentage
    def missing_duplicated(self):
    # identify the total missing values per column
    # sort in order 
        miss = self.df.isnull().sum().sort_values(ascending = False)

        # calculate percentage of the missing values
        percentage_miss = (self.df.isnull().sum() / len(self.df) * 100).sort_values(ascending = False)

        # store in a dataframe 
        missing = pd.DataFrame({"Missing Values": miss, "Percentage(%)": percentage_miss})
    
        print("\n Duplicated Rows:\n")
        duplicate_count = self.df.duplicated().sum()
        print(f"- Total duplicated rows: {duplicate_count} \n \n")

        return missing

    # remove duplicated rows
    def remove_duplicated_rows(self):
        self.df.drop_duplicates(subset=None, keep="first", inplace=True)
        
        # confirm if the duplicated rows have been removed
        duplicates = f'The dataset now has {self.df.duplicated().sum()} duplicate rows'

        return duplicates
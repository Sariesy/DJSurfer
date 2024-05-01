
import pandas as pd
from djsurfer.datainterface import DataInterface

#%%
class TsvObject(DataInterface):
    """
    A class representing a tsv object to access data in a tsv (Tab-Separated Values) file.

    Args:
        path (str): The path to the text file.
        name (str, optional): The name of the text object. Defaults to None.
        comment (str, optional): Any additional comment about the text object. Defaults to None.
    """

    def __init__(self, path, name=None, comment=None, delimiter='\t|,'):
        
        # Initialize the text interface object, passing the path, name, and comment to the base class.
        super().__init__(path=path, name=name, comment=comment)
        
        # Default delimiter is a comma.
        self.delimiter = delimiter


        
    def get_df(self):
        """
        Read the tsv file and return its contents as a pandas DataFrame.

        Returns:
            pandas.DataFrame: The contents of the tsv file as a DataFrame.
        """
        df = pd.read_csv(self.path, sep=self.delimiter, engine='python')
        
        return df
    
    def to_excel(self, path):
        """
        Save the tsv object to an Excel file.

        Args:
            path (str): The path to save the Excel file.
        """
        self.df.to_excel(path, index=False)
        

if __name__ == '__main__':
    
    from pathlib import Path
    obj = TsvObject(Path(__file__).parent / r'..\..\tests\demo_data\demo.tsv')


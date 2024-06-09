# from os import path
import pandas as pd



class Pipeline:
    def __init__(self):
        self.__factors = pd.read_excel('./data/factors.xlsx', header=0).fillna('')

    def load_select_factor(self, service):
        return self.__factors
    
    def data_save(self, save_path, df, *args, **kwargs):
        df.to_excel(save_path, **kwargs)

    def load_dw_data(self):
        pass
    
    def get_data_api(self):
        pass
    
    def info_save(self):
        pass

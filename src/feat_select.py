import optbinning
from optbinning import OptimalBinning
import pandas as pd
import numpy as np
from sklearn.feature_selection import f_classif, chi2
from tqdm import tqdm

def cal_iv(x, y, bin_type):
    optb = OptimalBinning(name='feature', dtype=bin_type)
    optb.fit(x, y)
    binning_table = optb.binning_table
    binning_table.build()
    return binning_table.iv


def feature_ranking(df, label, feat_list):
    stat_dict = {'feature':[],'iv':[], 'pval_test':[]}
    y = df[label]
    
    for feature in tqdm(feat_list):
        x = df[feature]
        x_stat = np.array(x).reshape(-1, 1)
        stat_dict['feature'].append(feature)
        data_type = df[feature].dtype
        bin_type = "categorical" if data_type in ('object', 'string') else "numerical"
        try:
            _, stat_test = f_classif(x_stat, y) if data_type == 'float' else chi2(x_stat, y)
        except:
            stat_test = [None]
        
        iv = cal_iv(x, y, bin_type=bin_type)
        stat_dict['iv'].append(iv)
        stat_dict['pval_test'].append(stat_test[0])

    return pd.DataFrame(stat_dict)
#!/usr/bin/env python

"""Tests for 'tsv' data in `djsurfer` package."""
import pytest
import numpy as np
import pandas as pd

from pathlib import Path

#%%
@pytest.fixture
def dir_data():
    
    dir = Path(__file__).parent / 'demo_data'
    dir.mkdir(exist_ok=True)
    
    arr0 = np.random.rand(100, 11)
    columns = [f'col_{i}' for i in range(11)]    
    df = pd.DataFrame(np.round(arr0, 4), columns=columns)   
    df.to_csv(dir / 'data0.tsv', index=False, sep='\t')
    
    arr1 = np.random.rand(100, 7)
    columns = [f'col_{i}' for i in range(5, 12)]    
    df = pd.DataFrame(np.round(arr1, 4), columns=columns)   
    df.to_csv(dir / 'data1.tsv', index=False, sep='\t')    

    return str(dir)

#%%
def test_tsvobject(dir_data):
    from djsurfer.lib_interface.tsv_object import TsvObject

    path = Path(dir_data) / 'data0.tsv'
    obj = TsvObject(path)
    
    assert isinstance(obj.dataframe, pd.DataFrame)

#%%   
def test_datapool(dir_data):
    
    from djsurfer.datapool import DataPool
    from djsurfer.lib_interface.tsv_object import TsvObject
    
    dp = DataPool(dir_data, interface=TsvObject)    
    assert len(dp.objs) == 2


#%%
def test_datainterface():
    
    from djsurfer.datainterface import DataInterface
    from djsurfer.lib_interface.tsv_object import TsvObject
    
    assert issubclass(TsvObject, DataInterface)
    
#%%

def test_datapool_get_signal(dir_data):
    
    from djsurfer.datapool import DataPool
    from djsurfer.lib_interface.tsv_object import TsvObject
    
    dp = DataPool(dir_data, interface=TsvObject)    
    signal = dp.get_signal('col_10')    
    assert signal.shape == (100, 2)

#%%
    
import pickle

import numpy as np
import pandas as pd
from pandas import DataFrame


def which_bin(elem, bins):
    """Return the index of first intervals that element is in

    Args:
        elem(float): a number.
        bins: an array of intervals in the format of (lower, upper]

    Returns:
        int: an index of the first interval the element is in. -1 if not found.

    """
    for idx, bounds in enumerate(bins, start=1):
        if bounds[0] < elem <= bounds[1]:
            return idx
    else:
        return -1


def transpose(matrix):
    """Matrix transpose

    Args:
        matrix: list of list

    Returns:
        list: list of list

    """
    return list(map(list, zip(*matrix)))


def save(dataset, labels):
    with open('../data/raw/dataset.pkl', 'wb') as fp:
        pickle.dump(dataset, fp)
    with open('../data/raw/labels.pkl', 'wb') as fp:
        pickle.dump(labels, fp)


def load():
    with open('../data/raw/dataset.pkl', 'rb') as fp:
        d = pickle.load(fp)
    with open('../data/raw/labels.pkl', 'rb') as fp:
        l = pickle.load(fp)
    return d, l


def array3D_to_dataframe(dataset, labels):
    """

    Args:
        dataset: nepochs x nchannels x nsamples
        labels: nepochs x 1

    Returns:
        data.frame

    """
    flat = []


def dataset2Xy(ds_pwd, labels):
    """Convert dataset, labels to X, y for sklearn

    Args:
        ds_pwd: 3D array of shape n_epoch, n_channel, n_feature

    Returns:
        X, 2D array of shape n_epoch, n_channel x n_feature
            fe-1-ch-1, fe-1-ch-2, ..., fe-n_fe-ch-n_ch
        y, same shape as labels
    """
    ds_pwd = np.array(ds_pwd)
    ne, nc, ns = np.shape(ds_pwd)
    X = ds_pwd.transpose([0, 2, 1]).reshape(-1, nc * ns)
    y = np.array(labels)
    return X, y


def dataset_3d_to_2d(dataset):
    """Convert 3D feature dataset to 2D

    Args:
        dataset: 3D list of nepoch x nchannel x nfeatures
    Returns:
        np.array: 2D-array of (nfeatures x nchannel) x (nepoch)
    """
    n1, n2, n3 = np.shape(dataset)
    return np.array(dataset).transpose([1,2,0]).reshape([n2*n3,n1])


def dataset_to_df(dataset, labels):
    """Convert numpy array DATASET, LABELS to pd.DataFrame

    Args:
        dataset: size nepoch x nchannel x nsamples/nfeatures
        labels: nepoch x 1
    Returns:
        pd.DataFrame: nrow = nepoch x nsamples; ncol = nchannel + 1
    """
    ds_pwd = np.array(dataset)
    ne, nc, ns = np.shape(ds_pwd)
    df_pwd = pd.DataFrame(ds_pwd.transpose([0,2,1]).reshape(-1, np.shape(ds_pwd)[1]),
                         columns=['ch'+ str(i) for i in np.arange(0, nc)])
    df_pwd = df_pwd.assign(labels = np.repeat(labels, ns))\
        .assign(epoch = np.repeat(np.arange(0, ne), ns))
    return df_pwd


locate = lambda listOfElems, elem: [ i for i in range(len(listOfElems)) if listOfElems[i] == elem ]
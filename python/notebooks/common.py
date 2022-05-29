from pathlib import Path


def dataDirectory(dataDirectoryName='data'):
    """
    Return the directory that contains the data.
    
    We assume that the data folder is locate in a parent directory of this file and named 'data'.
    If your setup is different, you will need to change this method.
    """
    dataDir = Path(__file__).resolve().parent
    print(f"__file__: {__file__}")
    while not list(dataDir.rglob('data_book_gedeck')):
        dataDir = dataDir.parent
    found = [d for d in dataDir.rglob('data_book_gedeck') if d.is_dir()]
    if not found:
        raise Exception(f'Cannot find data directory with name {dataDirectoryName} along the path of your source files')
    return found[0]
    
    
    
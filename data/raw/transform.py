from pathlib import Path
from zipfile import ZipFile

arch_zip_path = './archive.zip'
path_ = Path('data/raw/archive.zip')

# opening the zip file in read mode
with ZipFile(path_, 'r') as zip:
    # display the contents of the zip file
    zip.printdir()

    # extracting all the files
    print('Extract in progress...')

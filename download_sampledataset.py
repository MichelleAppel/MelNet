import requests
import zipfile

print('downloading')
url = 'https://cdn.mos.musicradar.com/audio/samples/musicradar-eighties-samples.zip' # get data from specific sample website
r = requests.get(url, allow_redirects=True)
zip_path = './samples.zip'
open(zip_path, 'wb').write(r.content) # download zip

print('unzipping')
with zipfile.ZipFile(zip_path, 'r') as zip_ref: # unzip
  zip_ref.extractall('.')

print('done')
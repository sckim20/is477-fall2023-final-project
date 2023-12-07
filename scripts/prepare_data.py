import requests
import hashlib

# Car data
data_url = "https://archive.ics.uci.edu/static/public/186/wine+quality.zip"
response_1 = requests.get(data_url)
with open('wine.zip', mode='wb') as f:
    f.write(response_1.content)

filename = 'wine.zip'
with open(filename, mode='rb') as f:
    data = f.read()
    sha256hash = hashlib.sha256(data).hexdigest()

wine_sha256 = '2bae62c4481220623579d4c4fb36b55652b6b75e06e49fa1981b8198362dfdab'
if wine_sha256 != sha256hash:
    print("Computed hash does not match")
else:
    print("Computed hash match with the original data")




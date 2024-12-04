from pprint import pprint
import yaml

with open('DATA/bands.yaml') as bands_in:
    band_data = yaml.load(bands_in, Loader=yaml.Loader)

pprint(band_data)

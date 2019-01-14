import os.path
import pandas as pd
pkgdir = os.path.dirname(__file__)

# Jhonson & Jhonson
jj = pd.read_csv(f'{pkgdir}/data/jj.csv', index_col=0, parse_dates=True)
jj.index = jj.index.to_period("Q")

# Global temperatures
globaltemp = pd.read_csv(f'{pkgdir}/data/globaltemp.csv', index_col=0, 
                            parse_dates=True)
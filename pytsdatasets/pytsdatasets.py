import os.path
import pandas as pd

pkgdir = os.path.dirname(__file__)
jj = pd.read_csv(f'{pkgdir}/data/jj.csv', index_col=0, parse_dates=True)
jj.index = jj.index.to_period("Q")

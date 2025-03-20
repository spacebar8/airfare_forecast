#!/usr/bin/env python3

from collections import defaultdict
import csv
import pandas as pd

## Processed CSV Sorted
# filepath = "data/processed-data-sorted.csv"

# def read_csv(filepath):
#   '''
#   Output: {('airport_iata_1', 'airport_iata_2'): {'date': 'yyyy-qq', 'fare': 'XX.XX'}}
#   '''
#   output = defaultdict(lambda: defaultdict(list))
#   with open(filepath, 'r') as f:
#     csv_reader = csv.DictReader(f)
#     for row in csv_reader:
#       # print(row['year'], row['quarter'], row['airport_iata_1'], row['airport_iata_2'], row['fare'])
#       output[(row['airport_iata_1'], row['airport_iata_2'])]['date'].append(f"{row['year']}-Q{row['quarter']}")
#       output[(row['airport_iata_1'], row['airport_iata_2'])]['fare'].append(row['fare'])

#   return output

## Raw CSV Sorted
filepath = "data/raw-data-sorted.csv"

def read_csv(filepath):
  '''
  Output: {('airport_1', 'airport_2'): {'date': 'yyyy-qq', 'fare': 'XX.XX'}}
  '''
  output = defaultdict(lambda: defaultdict(list))
  with open(filepath, 'r') as f:
    csv_reader = csv.DictReader(f)
    for row in csv_reader:
      # print(row['Year'], row['quarter'], row['airport_iata_1'], row['airport_iata_2'], row['fare'])
      output[(row['airport_1'], row['airport_2'])]['date'].append(f"{row['Year']}-Q{row['quarter']}")
      output[(row['airport_1'], row['airport_2'])]['fare'].append(row['fare'])

  return output

data = read_csv(filepath)  # using csv module

# print(data[('XNA', 'SWF')])
df = pd.DataFrame(data[('BOS', 'LGA')])
df['ds'] = pd.PeriodIndex(df['date'], freq='Q') \
             .to_timestamp(freq='Q')  # PeriodIndex(freq='Q') expects '%Y-%q' format, outputs end of qtr

df['period'] = df['ds'].dt.to_period('Q')
df['shift'] = df['period'].shift(periods=1, fill_value=(df['period'].min() - 1))

def diff_qtr(a: pd.Period, b: pd.Period) -> int:
  return (a - b).n

# df['diff'] = df.apply(lambda x: diff_qtr(x['period'], x['shift']), axis=1)


# df['mask'] = 1
# df.loc[df['shift'] + 1 == df['period'], 'mask'] = 0

df['bool'] = (df['shift'] + 1 != df['period'])
df['mask'] = df['bool'].cumsum()


res = df.loc[df['mask'] == df['mask'].value_counts().idxmax(), ['ds', 'fare']]
res = res.reset_index(drop=True)


with pd.option_context('display.max_rows', None, 'display.max_columns', None):
  print(res)
  # print(df)

def find_longest_timeseq(data: pd.DataFrame, ycol: list, limit: int) -> pd.DataFrame:
  '''
  Finds the longest sequence of quarterly dates that is at least of size "limit".
  Returns a pd.DF that is in format for FB Prophet e.g. cols = ['ds', 'y']
    where 'ds' is datestamp [datetime] and 'y' is column to forecast [float]

  :params:
    data = pd.Dataframe({'date': ['2023-Q4', '2024-Q1', ...], 'fare': [1.2, 3.4, ...]})
    ycol = ['fare']  # column to forecast
    limit = 50
  :output: 
    pd.Dataframe({'ds': ['2023-12-31', '2024-03-31', ...], 'y': [1.2, 3.4, ...]})
  '''

  return None

# print(df.head())
# print(df.dtypes)
# print(len(routes))
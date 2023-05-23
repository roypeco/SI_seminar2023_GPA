# ライブラリのインポート
import pandas as pd

# csvファイルをDF型で読み込む
def load_csv(name: str):
  df = pd.read_csv('../csv_file/' + name, index_col=0)

  return df

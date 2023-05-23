# 自作関数のインポート
import read_csv, calc

# mainの定義
def main():
  df = read_csv.load_csv('score.csv')
  gpa = calc.get_gpa(list(df['評価']), list(df['単位']))
  print("あなたのGPAは，" + str(gpa) + "です．")

# main関数の実行
if __name__ == '__main__':
  main()

# ライブラリのインポート
import decimal

#gpaを計算する関数の定義
def get_gpa(score_list: list, credit_list: list):
  
  #GP積の和を求める
  decimal.getcontext().prec=4
  result = 0
  for i, j in zip(score_list, credit_list):
    gpa_tmp = decimal.Decimal((i-55)) * decimal.Decimal((j/10))
    result += gpa_tmp

  # GPAを求める
  decimal.getcontext().prec=3
  result = decimal.Decimal(result) / decimal.Decimal(sum(credit_list))

  return result

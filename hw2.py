# Git-Leegoeun
def get_integer(prompt):
  b=int(input(prompt))
  return b
def exchange(cash):
  result500=cash//50
  print("500원 동전의 개수:",result500)
  money=cash%500
  result100=money//100
  print("100원 동전의 개수:",result100)
  money=cash%100
  result50=money//50
  print("50원 동전의 개수:",result50)
  money=cash%50
  result10=money//10
  print("10원 동전의 개수:",result10)
total=get_integer("동전으로 교환하고자 하는 금액은? ")
exchange(total

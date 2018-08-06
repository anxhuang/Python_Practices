#練習自訂例外 Custom Exception
class OverBudgetException (Exception):
    e="已經超支了\n"
    pass

budget=1000
total=0
book={}
try:
    while True:
        item=input("消費項目: ")
        price=int(input("消費金額: "))
        total += price
        if total <= budget:
            book[item]=price #等同於book.update({item:price}), 沒有這個key就會新增
            print(f"目前消費金額: {total}")
        else:
            raise OverBudgetException
            break
except OverBudgetException:
    print(OverBudgetException.e,book)
input("Enter to exit")


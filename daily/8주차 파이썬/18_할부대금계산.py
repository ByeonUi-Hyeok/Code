def installments():
    price = int(input("상품대금 >>> "))
    months = int(input("할부개월수(3-12) >>> "))
    result = round(price/months,-1)
    return result

print("월할부금액은 {:,.0f}원입니다.".format(installments()))
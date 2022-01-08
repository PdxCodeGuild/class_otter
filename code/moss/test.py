def cnvr_dig(n):
    if n > 19:
        return ones[n//10] + tens[n%10]


def cnvr(n):
    result= ''
    result += cnvr_dig ((n//100)%10)
    if n >100 and n % 100:
        result += 'and'
    result += cnvr_dig (n % 100)
    return result





ones = ['one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
tens = ['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']

print(cnvr(22))
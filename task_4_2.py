import requests


def currency_rates(args):
    if args.isupper() is not True:
        args = args.upper()
    url = "http://www.cbr.ru/scripts/XML_daily.asp"
    response = requests.get(url)
    money_list = response.text.split('ID=')
    money_list.remove(money_list[0])
    money_dict = {}

    for money in money_list:
        find_key = money.split('<CharCode>')
        find_val = money.split('/Name><Value>')
        find_ratio = money.split('<Nominal>')
        key = find_key[1][0:3]
        val = find_val[1][0:find_val[1].find('<')]
        ratio_money = find_ratio[1][0:find_ratio[1].find('<')]
        money_dict.setdefault(key, [val, ratio_money])

    if money_dict.get(args) is not None:
        int_num = int(money_dict.get(args)[0][0:money_dict.get(args)[0].find(',')])
        float_num = round((int(money_dict.get(args)[0][(money_dict.get(args)[0].find(',')) + 1:]) / 10000), 2)
        number = int_num + float_num
        print(f'{args} {round(number / int(money_dict.get(args)[1]), 2)}')
    else:
        print(money_dict.get(args))


currency_rates('USd')
currency_rates('EUr')

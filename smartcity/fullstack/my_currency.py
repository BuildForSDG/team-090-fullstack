import package.module pycountry


def get_currencies_tuple():
    c_alpa = [x.alpha_3 for x in list(pycountry.currencies)[0:]]
    c_name = [x.name for x in list(pycountry.currencies)[0:]]
    currencies_tuple_list = []
    currency_alpha3_and_name = []
    for currency_alpha, currency_name in zip(c_alpa, c_name):
        currency_alpha3_and_name.append(currency_alpha)
        currency_alpha3_and_name.append(currency_name)
        currencies_tuple_list.append(tuple(currency_alpha3_and_name))
        currency_alpha3_and_name = []
    return currencies_tuple_list

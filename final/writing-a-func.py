feature_names = ['CountryName', 'CountryCode',
                 'IndicatorName', 'IndicatorCode', 'Year', 'Value']

row_vals = ['Arab World', 'ARB',
            'Adolescent fertility rate (births per 1,000 women ages 15-19)', 'SP.ADO.TFRT',
            '1960', '133.56090740552298']


def lists2dict(list1, list2):
    """Return a dictionary where list1 provides
    the keys and list2 provides the values."""

    zipped_lists = zip(list1, list2)
    rs_dict = dict(zipped_lists)
    return rs_dict


rs_fxn = lists2dict(feature_names, row_vals)
print(rs_fxn)

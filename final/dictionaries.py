feature_names = ['CountryName', 'CountryCode',
                 'IndicatorName', 'IndicatorCode', 'Year', 'Value']

row_vals = ['Arab World', 'ARB',
            'Adolescent fertility rate (births per 1,000 women ages 15-19)', 'SP.ADO.TFRT',
            '1960', '133.56090740552298']

zipped_lists = zip(feature_names, row_vals)
rs_dict = dict(zipped_lists)
print(rs_dict)

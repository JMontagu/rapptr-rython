from assets import assets

gb_assets = {}

for asset in assets:
    if asset['CountryOfIssue'] == 'GB':
        issuer = asset['Issuer']
        if gb_assets.get(issuer):
            gb_assets[issuer].append(asset)
        else:
            gb_assets[issuer] = [asset]

for issuer in gb_assets:
    issuerAssets = gb_assets[issuer]
    values = []
    for asset in issuerAssets:
        values.append(asset['Price'] * asset['Quantity'])

    if sum(values) > 10:
        print('Disclose: ' + issuer)
    else:
        print('Ok: ' + issuer)

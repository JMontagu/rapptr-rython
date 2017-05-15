from assets import assets

alertLevels = {
    'ok': [],
    'warning': [],
    'disclosure': [],
}

for asset in assets:
    if asset['CountryOfIssue'] == 'AUD' and asset['Quantity'] > 50:
        alertLevels['disclosure'].append(asset)
    elif asset['CountryOfIssue'] == 'UK':
        alertLevels['ok'].append(asset)

print('You have ' + str(len(alertLevels['ok'])) + ' oks')
print('You have ' + str(len(alertLevels['warning'])) + ' warnings')
print('You have ' + str(len(alertLevels['disclosure'])) + ' disclosure')

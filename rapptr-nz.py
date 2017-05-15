from assets import assets

for asset in assets:
    if asset['CountryOfIssue'] == 'NZ':
        value = ((asset['Quantity'] * asset['VotesPerShare'] / asset['TotalVotes']) * 1)
        if value > 0.5:
            print('Disclose: ' + asset['AssetName'])
        else:
            print('Ok ' + asset['AssetName'])

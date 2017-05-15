from assets import assets

## Step 1: create the variable 'portfolio_name' to hold the portfolio name and give it a name
portfolio_name = 'Foo'

# Print the portfolio name and ID
print('Portfolio name: ' + portfolio_name)

## Step 2: create a ID number 'portfolio_id'
portfolio_id = 5

# Print it
print('Portfolio ID: ' + str(portfolio_id))

## Step 3: Create a variable 'last_data' to hold when the portfolio last had data added to it
last_data = 2015

# Print the last data year, and how many months it's been
age = (2017 - last_data) * 12
print('Last data ' + str(last_data) + ', ' + str(age) + ' months ago')

## Step 4: Given list of assets, count how many assets are to be imported
count = 0
for asset in assets:
  count += 1

print('Assets to process: ' + str(count))

## Step 5: Given list of assets, each asset in the list is a dictionary containing the key 'Issuer'. Print each issuer name out.

issuers = []
for asset in assets:
  issuers.append(asset['Issuer'])

print(issuers)
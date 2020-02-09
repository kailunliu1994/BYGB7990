#Kailun Liu Homework 8 final project
#Assume tax rate in New York city is fixed as 8.875%
import pandas as pd
#define the function for the final price that customer need to pay.
#Since I can not find the information about restaurants and food price, I had to hard code 2 of my favorite restaurants info and set the price by the info given by ubereats.
restNameFile = 'D:/python final/RestName.csv'
reviewNameFile = 'D:/python final/Review.txt'
def finalPrice(p):
    pFloat = float(p)
    tFloat = float(p)*0.08875
    if pFloat > 30:
        d = 5
    else:
        d = 8
    dFloat = float(d)
    f = pFloat + tFloat + dFloat
    return f
print('Welcome to the food order system\n Here is the list restaurants name:\n')
#read the restaurants' info
df=pd.read_csv(restNameFile)
restName = df['Name']
print(restName)
chooseRestNumber = input('Choose the index of the restaurant you want to order\n')
restNameChoose = restName[float(chooseRestNumber)]
if float(chooseRestNumber) == 0:
    menuNameFile = 'D:/python final/Guo.csv'
elif  float(chooseRestNumber) == 1:
    menuNameFile = 'D:/python final/Chairman.csv'
#using the method introduced in lab6 to read the csv file and print the menu with price
with open(menuNameFile,'r',encoding = 'utf8') as menuFile:
    line = menuFile.readline()
    line = menuFile.readline().replace('\n','')
    while line != '':
        lineList = line.split(',')
        menuName  = lineList[0]
        menuPrice = lineList[1]
        menuType = lineList[2]
        outputLine = menuName + ' ' + menuPrice + ' ' + menuType + '\n'
        print(outputLine)
        line = menuFile.readline().replace('\n','')
#Creat a loop for customer to add items. And error check for the index number customer enter.
errorCheck = 'N'
while errorCheck != 'Y':
    try:
        k1 = float(input('What do you want to order type in the index number.\n'))
       
        dk = pd.read_csv(menuNameFile)
        price = dk['Price']
        orderPrice = price[k1]
        k2 = input('Do you want to order more? Y/N \n')
        while k2 != 'N':
            k3 = input('What do you want to order type in the index number.\n')
            orderPrice2 = price[float(k3)]
            orderPrice = float(orderPrice) + float(orderPrice2)
            k2 = input('Do you want to order more? Y/N \n')
        errorCheck = 'Y'
    except:
        print('Enter a index number showed next to the item.')
        
    
#Calculate the final price and finish the order
final = finalPrice(orderPrice)
finalConfirm = 'The order total price is $'+str(final)+', do you want to confirm the order? Y/N\n'
k4 =input(finalConfirm)
if k4 == 'Y':
    print('Thank you for your order!')
    custResponse= input('Would you like to leave a review? Y/N\n')
    if custResponse == 'Y':
        custReview = input('Write down your review\n')
        with open(reviewNameFile,'w',encoding = 'utf8') as reviewFile:
            finalReview = restNameChoose + ' ' +custReview + '\n'
            reviewFile.write(finalReview)
    if custResponse =='N':
        print('Bye')
if k4 == 'N':
    print('Bye Bye')
#Record the customer review: 

# problem 1

user_input1=input('enter 1st input')
user_input2=input('enter 2nd input')
if user_input1>user_input2:
    print('\nYes input1 is greater than input2')
else:
    print('\nNo input2 is greater than input1')

# problem 2
shopping_list=['soap','oil','biscuit','flour']
check_item=input(' enter item name')
if check_item in shopping_list:
    print ('\nYes ' + check_item + ' is in the list')
    item_price=int(input('enter item price'))
    if item_price < 100:
       print('\nYes give me the item')
       purchasedate=input('enter purchase date')
       ordernum=input('enter order number')
       print(check_item + '  is purchased on ' + str(purchasedate) + ' th of this month with ' + str(item_price) + '  Rs having order number ' + str(ordernum))
    else:
       print('\nNo I do not want to buy')
 
else:
    print('\nNo item is not in the list')






phone=input("Enter number: ")
digit_mapping={"1":"one","2":"two","3":"three","4":"four","5":"five"}
output=" "
for i in phone:
    output += digit_mapping.get(i,"NO data found")+" "
print (output)

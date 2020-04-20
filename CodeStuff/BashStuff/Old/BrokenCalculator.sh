
#!/bin/bash

echo "Welcome to a super basic text calculator!"
read -p "enter first number: " first_number
echo $first_number
read -p "enter second number:" second_number
echo $second_number
read -p "enter operator" operator
echo $operator
operators=("+" "-" "*" "/")
if [ $operator in $operators ]; then
	echo "operator is gud"
	exit
else
	echo "operator is not gud"
	exit
fi

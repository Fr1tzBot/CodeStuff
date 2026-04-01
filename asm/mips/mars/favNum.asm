# Write a program that reads a single integer N from the user.
# It then prints the string: "Is N your favorite number?"
.text
    li $v0 5
    syscall

    move $t0 $v0

    la $a0 msg1
    li $v0 4
    syscall

    move $a0 $t0
    li $v0 1
    syscall

    la $a0 msg2
    li $v0 4
    syscall
.data
    msg1: .asciiz "Is "
    msg2: .asciiz " your favorite number?"

.text
    #can do this or set a cap for name length...
    #prompt user for # of chars in name
    la $a0 chars
    li $v0 4
    syscall

    #read input
    li $v0 5
    syscall
    move $t0 $v0

    #increment by 2 for null-terminator and \n
    addi $t0 $t0 2

    #prompt user for their name
    la $a0 prompt
    li $v0 4
    syscall

    #poll for name
    la $a0 name
    move $a1 $t0
    li $v0 8
    syscall

    #print greeting
    la $a0 greet
    li $v0 4
    syscall

    # #move user-provided name back to print register
    la $a0 name
    li $v0 4
    syscall

.data
    name:
    chars: .asciiz "How many characters in your name? "
    prompt: .asciiz "Enter Your name: "
    greet: .asciiz "Hello, "

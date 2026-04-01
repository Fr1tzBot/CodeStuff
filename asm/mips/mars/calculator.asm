.text
    #initially use read_float syscall for inputs
    li $a1 6

    la $a0 prompt1
    jal prompt
    mov.s $f1 $f0

    la $a0 prompt2
    jal prompt
    mov.s $f2 $f0

    #switch to read_char for operator
    li $a1 12

    la $a0 prompt3
    jal prompt
    move $t0 $v0

    #branches for +, -, *, /
    beq $t0 42 times
    beq $t0 43 plus
    beq $t0 45 minus
    beq $t0 47 div

    #jump to output by default to avoid defaulting to +
    b output

    plus:
        add.s $f3 $f1 $f2
        b output
    minus:
        sub.s $f3 $f1 $f2
        b output
    times:
        mul.s $f3 $f1 $f2
        b output
    div:
        div.s $f3 $f1 $f2
        b output
    output:
        #print a single \n because read_char doesnt use enter
        li $a0 10
        jal print_char

        #print the equation entered
        mov.s $f12 $f1
        jal print_float

        move $a0 $t0
        jal print_char

        mov.s $f12 $f2
        jal print_float

        #print = sign
        li $a0 61
        jal print_char

        #followed by the result
        mov.s $f12 $f3
        jal print_float

        #finally exit to ensure we don't run our functions
        li $v0 10
        syscall

print_float:
    li $v0 2
    syscall
    jr $ra

print_char:
    li $v0 11
    syscall
    jr $ra

prompt:
    li $v0 4
    syscall

    move $v0 $a1
    syscall
    jr $ra

.data
    prompt1: .asciiz "Enter First Number: "
    prompt2: .asciiz "Enter Second Number: "
    prompt3: .asciiz "Enter Operator (+, -, *, /): "

.text
.globl __start
__start:
    li $v0, 4004
    li $a0, 1
    la $a1, msg
    li $a2, 13
    syscall

    # exit code 0
    li $v0, 4001
    li $a0, 0
    syscall
.data
    msg: .asciiz "Hello world!\n"

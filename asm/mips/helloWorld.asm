.text
    la $a0 msg
    li $v0 4
    syscall
.data
    msg: .asciiz "Hello world!\n"

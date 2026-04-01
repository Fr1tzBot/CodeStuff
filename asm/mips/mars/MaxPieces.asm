.text
    loop:
        #prompt user for input
        #syscall 5 is read_int
        li $v0 5
        syscall

        #jump to end if users input is <0
        bltz $v0 end

        #v0 is n, and will remain n until we print our result

        #First we use t1 to hold n^2
        mult $v0 $v0
        mflo $t1

        #T1 now holds our n+n^2
        add $t1 $t1 $v0

        #T1 now holds n^2+n+2
        addi $t1 $t1 2

        #unfortunately div doesn't work on immediates
        #$t2 for 2, fittingly :)
        li $t2 2

        #Finally, T1 holds our solution
        div $t1 $t2
        #pump result straight to a0 to save an instruction
        mflo $a0

        #Print solution, followed by a newline
        li $v0 1
        syscall

        #ascii 10 is \n
        li $a0 10
        #syscall 11 is print_char
        li $v0 11
        syscall
    b loop

    end:
        #syscall 10 is exit
        li $v0 10
        syscall


.text
    #prompt user for start and end
    #syscall 5 is read_int
    li $v0, 5
    syscall

    #T1 is start
    move $t1 $v0

    #syscall 5 is read_int
    li $v0, 5
    syscall

    #T2 is end
    move $t2 $v0

    #terminate if End<Start
    blt $t2 $t1 end

    #store start for later
    move $t0 $t1
    loop1:
        #print out each number, starting with $t1
        move $a0 $t0

        #syscall 1 is print_int
        li $v0, 1
        syscall

        #ascii 32 is space, syscall 11 is print_char
        li $a0 32
        li $v0 11
        syscall

        addi $t0 $t0 1

        #loop while i < end
        ble $t0 $t2 loop1

    #ascii 10 is \n, syscall 11 is print_char
    li $a0, 10
    li $v0 11
    syscall

    #store our length in $t0 temporarily
    sub $t0 $t2 $t1
    addi $t0 $t0 1
    move $a0 $t0
    #print this length
    li $v0, 1
    syscall

    li $a0, 10
    li $v0 11
    syscall

    #prompt for number of chunks
    li $v0, 5
    syscall

    #check that number of chunks is reasonable
    #pull directly from v0 to save an instruction
    blez $v0 end
    bgt $v0 $t0 end

    #overwrite $t0 with our remainder, and $t3 with our chunk size
    div $t0 $v0
    mflo $t3
    mfhi $t0

    #t4, our chunk boundary, is initialized to the start
    move $t4 $t1

    #recall $t1 is start and $t2 is end

    loop2:
        #if we are at our boundary, print a newline
        blt $t1 $t4 skip1
            #increment boundary by our chunk size
            add $t4 $t4 $t3
            #if we still have remainder numbers, add one
            beqz $t0 skip2
                #push our chunk boundary back
                addi $t4 $t4 1
                #and decrement the remainder count
                addi $t0 $t0 -1
            skip2:

            #print a newline to seperate chunks
            li $a0, 10
            li $v0 11
            syscall
        skip1:

        #print the int we're on
        move $a0 $t1

        li $v0, 1
        syscall

        #print a space to seperate ints
        li $a0 32
        li $v0 11
        syscall

        #increment counter
        addi $t1 $t1 1
        #loop if counter <= end
    ble $t1 $t2 loop2


    end:
        #exit syscall
        li $v0 10
        syscall


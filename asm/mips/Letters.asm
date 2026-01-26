# Author: Fritz Geib
# Email: ftgeib@mtu.edu
# Class: EE1142 R01

.text
	.macro val (%var)
        blez %var end
        bgt %var 40 end
    .end_macro

    .macro val_input (%var)
        bltz %var end
        bge  %var 40 end
    .end_macro

    .macro print
        li $a0 10
        print_char

        move $t0 $s0
        li $t2 1
        print_loop:
            lw $a0 0($t0)
            addi $a0 $a0 65
            print_char

            # print either a space or newline next
            div $t2 $s2
            mfhi $t1

            bnez $t1 next
                li $a0 10
                print_char
            next:
            addi $t0 $t0 4
            addi $t2 $t2 1
        ble $t2 $s4 print_loop

    .end_macro

    .macro print_end
        print
        b end
    .end_macro

    .macro call (%type)
        li $v0 %type
        syscall
    .end_macro

    .macro read_int (%save)
        call 5
        move %save $v0
    .end_macro

    .macro print_int
        call 1
    .end_macro

    .macro print_char
        call 11
    .end_macro

    .macro exit
        call 10
    .end_macro


    la $s0 data
    # read number of rows
    read_int $s1
    # input validation
    val $s1

    # read number of columns
    read_int $s2
    # input validation
    val $s2

    # read default character
    read_int $s3
    # input validation (character specific)
    bltz $s3 end
    bgt $s3 25 end

    # store in $s4 the total number of values in the array
    mult $s1 $s2
    mflo $s4

    move $t0 $s0
    li $t1 0
    # populate data array
    populate:
        sw $s3 0($t0)
        addi $t0 $t0 4
        addi $t1 $t1 1
    blt $t1 $s4 populate

    loop:
        # read row
        read_int $t0
        # input validation
        val_input $t0

        # read column
        read_int $t1
        val_input $t1

        # calculate the index of the selected letter
        # number of cols ($s2) * row selected ($t0) + col selected ($t1) = index ($t2)
        mult $s2 $t0
        mflo $t2
        add $t2 $t1 $t2

        #from here, we convert the index to a usable memory address
        li $t3 4
        mult $t2 $t3
        mflo $t2
        add $t2 $s0 $t2

        # load the selected letter into $t4
        lw $t4 0($t2)

        # increment $t4
        addi $t4 $t4 1

        # if $t4 > 25, loop back to 0
        bgt $t4 25 if
        b fi
        if:
            li $t4 0
        fi:

        # store the incremented letter back into $t4
        sw $t4 0($t2)
    b loop

    end:
        bgtz $s4 print_end
        exit
    print_end:
        print
        exit


.data
    # enough space for a full matrix (4*40*40)
    data: .space 6400


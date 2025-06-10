.data
x: .word 5
y: .word 3
z: .word 9
promedio_msg: .asciiz "1. Promedio: "
dif_cuad_msg: .asciiz "\n2. Diferencia cuadrática: "
mult_result_msg: .asciiz "\n3. Multiplicación: "

.text
.globl main

main:
    lw $t0, x
    lw $t1, y
    lw $t2, z
    
    li $v0, 4
    la $a0, promedio_msg
    syscall
    
    add $t3, $t0, $t1
    add $t3, $t3, $t2
    div $t3, $t3, 3
    move $a0, $t3
    li $v0, 1
    syscall
    
    li $v0, 4
    la $a0, dif_cuad_msg
    syscall
    
    sub $t4, $t0, $t1
    mul $t4, $t4, $t4
    move $a0, $t4
    li $v0, 1
    syscall
    
    li $v0, 4
    la $a0, mult_result_msg
    syscall
    
    mul $a0, $t3, $t4
    li $v0, 1
    syscall
    
    li $v0, 10
    syscall
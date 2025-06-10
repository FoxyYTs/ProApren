.data
lado_cuadrado_msg: .asciiz "Ingrese el lado del cuadrado: "
lado_rectangulo1_msg: .asciiz "\nIngrese el primer lado del rectángulo: "
lado_rectangulo2_msg: .asciiz "Ingrese el segundo lado del rectángulo: "
area_cuadrado_msg: .asciiz "\n1. Área del cuadrado: "
area_rectangulo_msg: .asciiz "\n2. Área del rectángulo: "
suma_areas_msg: .asciiz "\n3. Suma de áreas: "
promedio_areas_msg: .asciiz "\n4. Promedio de áreas: "

.text
.globl main

main:
    li $v0, 4
    la $a0, lado_cuadrado_msg
    syscall
    
    li $v0, 5
    syscall
    move $t0, $v0
    
    mul $t1, $t0, $t0
    
    li $v0, 4
    la $a0, area_cuadrado_msg
    syscall
    
    move $a0, $t1
    li $v0, 1
    syscall
    
    li $v0, 4
    la $a0, lado_rectangulo1_msg
    syscall
    
    li $v0, 5
    syscall
    move $t2, $v0
    
    li $v0, 4
    la $a0, lado_rectangulo2_msg
    syscall
    
    li $v0, 5
    syscall
    move $t3, $v0
    
    mul $t4, $t2, $t3
    
    li $v0, 4
    la $a0, area_rectangulo_msg
    syscall
    
    move $a0, $t4
    li $v0, 1
    syscall
    
    li $v0, 4
    la $a0, suma_areas_msg
    syscall
    
    add $t5, $t1, $t4
    move $a0, $t5
    li $v0, 1
    syscall
    
    li $v0, 4
    la $a0, promedio_areas_msg
    syscall
    
    div $a0, $t5, 2
    li $v0, 1
    syscall
    
    li $v0, 10
    syscall
.MODEL SMALL
.STACK
.DATA
M1 DB 10,13,"WELCOME$"
M2 DB 10,13,"TCET$"
.CODE
MACRO DISP XX
MOV AH,09
LEA DX,XX
INT 21H
ENDM
MACRO DISP1 XX,YY
MOV AH,09
LEA DX,XX
INT 21H
MOV AH,09
LEA DX,YY
INT 21H
ENDM
.STARTUP
DISP M1
DISP M2
DISP1 M2,M1
.EXIT
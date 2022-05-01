%{
#define NUM 1
%}

%%
[0-9]+\.[0-9]+|[0-9]+ {return NUM;}
int|char|bool|void {return 2;}
[a-zA-Z]+[a-zA-Z0-9]* {return 3;}
%%

#include<stdio.h>
int main(int argc, char *argv[]){
  int val;

  while(val=yylex()){
    switch(val){
      case 1:
        printf("\n%s-Number", yytext);
        break;
      case 2:
        printf("\n%s-Keyword", yytext);
        break;
      case 3:
        printf("\n%s-Identifier", yytext);
        break;
    }
  }

  return 0;
} 
#include <stdio.h>
   struct racional {
    private:
      int numerador;
      int denominador;
      int numerador2, denominador2;
      int n, n2, d, d2;
      int sumnumerador, sumdenominador;
      int mulnumerador, muldenominador;
    public:
      void imprimir();
      void asignar();
      void sumar();
      void simplificar();
      void multiplicar();
      void leer();
    };
    void racional::sumar(){
      sumnumerador=numerador*denominador2+numerador2*denominador;
      sumdenominador=denominador2*denominador;
    }
     void racional::multiplicar(){
      mulnumerador=numerador*numerador2;
      muldenominador=denominador2*denominador;
    }
     void racional::simplificar(){
        if(sumdenominador==1){
	     }else{
	         int b=2;
	         while(b<=sumnumerador){
	         	 if(sumdenominador%b==0 && sumnumerador%b==0){
		            sumdenominador=sumdenominador/b;
			          sumnumerador=sumnumerador/b;
	        	}else{
		        b++;
		}}
           }
         if(muldenominador==1){
	     }else{
	         int b=2;
	         while(b<=mulnumerador){
	         	 if(muldenominador%b==0 && mulnumerador%b==0){
		            muldenominador=muldenominador/b;
			         mulnumerador=mulnumerador/b;
	        	}else{
		        b++;
		       }
        	}
	      }
       
    }
       

    void racional::imprimir() {
      printf("\n%d/%d",sumnumerador,sumdenominador);
      printf("\n%d/%d",mulnumerador,muldenominador);
    };
    
    void racional::asignar() {
      numerador= n;
      denominador=d;
      numerador2=n2;
      denominador2=d2;
    };
    void racional::leer() {
      scanf("%d",&n);
      scanf("%d",&d);
      scanf("%d",&n2);
      scanf("%d",&d2);
    }
   
    int main() {

      racional r;
      r.leer();
      r.asignar();
      r.sumar();
      r.multiplicar();
      r.simplificar();
      r.imprimir();
    } 
  
   

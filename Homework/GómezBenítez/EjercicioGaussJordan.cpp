#include <stdio.h>
#include<stdlib.h>
#include<time.h>

   struct racional {
    private:
    public:
      int numerador;
      int denominador;
    void asignar(racional,racional);
    void imprimir(racional,racional);
    void reducir(racional, racional);
    racional simplificar(racional);
    };
    void asignar(racional vectorinicial[5],racional vectorfinal[5]){
        vectorinicial[3].numerador=1;
        vectorinicial[3].denominador=1;
        vectorinicial[4].numerador=0;
        vectorinicial[4].denominador=1;
        vectorinicial[5].numerador=0;
        vectorinicial[5].denominador=1;
        time_t t;
        srand((unsigned) time(&t));
        for (int i=0; i<3;i++){
           vectorinicial[i].numerador=rand()%(9-1);
           vectorinicial[i].denominador=rand()%(9-1);
           while(vectorinicial[i].denominador==0){
               vectorinicial[i].denominador=rand()%(9-1);
           }
     }
     for(int i=0;i<6;i++){
           vectorfinal[i].numerador=vectorinicial[i].numerador;
           vectorfinal[i].denominador=vectorinicial[i].denominador;
        }
    }
    racional simplificar(racional vectorfinal){
      if(vectorfinal.denominador==1){
	     }else{
	         int b=2;
	         while(b<=vectorfinal.numerador){
	         	 if(vectorfinal.denominador%b==0 && vectorfinal.numerador%b==0){
		            vectorfinal.denominador=vectorfinal.denominador/b;
			          vectorfinal.numerador=vectorfinal.numerador/b;
	        	}else{
		        b++;
		}}
           } return vectorfinal;
    }
    void reducir(racional vectorinicial[5],racional vectorfinal[5]){
     
         for(int i=0; i<4; i=i+3){
              vectorfinal[i].numerador *=vectorinicial[0].denominador;
              vectorfinal[i].denominador *=vectorinicial[0].numerador;
       }
        for(int i=1; i<5; i=i+3){
              vectorfinal[i].numerador = vectorfinal[i].numerador * vectorinicial[2].numerador - vectorinicial[2].numerador*vectorinicial[1].numerador;
              vectorfinal[i].denominador =vectorinicial[1].denominador * vectorinicial[2].denominador;
       }
          for(int i=2; i<6; i=i+3){
             vectorfinal[i].numerador = vectorfinal[i].numerador * vectorinicial[1].numerador - vectorinicial[1].numerador*vectorinicial[2].numerador;
             vectorfinal[i].denominador = vectorinicial[2].denominador * vectorinicial[1].denominador;
    }
           for(int i=0; i<6; i++){
            vectorfinal[i]=simplificar(vectorfinal[i]);
    }  
       
        
    }
    void imprimir(racional vectorinicial[5],racional vectorfinal[5]){
        for(int i=0;i<6;i++){
          if(vectorinicial[i].denominador==1){
            printf("%d\t",vectorinicial[i].numerador);
          }else{
            if(vectorinicial[i].numerador==0){
              printf("%d\t",vectorinicial[i].numerador);
            } else
            {
              printf("%d/%d\t",vectorinicial[i].numerador,vectorinicial[i].denominador);
            }
          }
        }
        printf("\n----------------------------------------------\n");
         for(int i=0;i<6;i++){
           if(vectorfinal[i].denominador==1){
            printf("%d\t",vectorfinal[i].numerador);
          }else{
            if(vectorfinal[i].numerador==0){
              printf("%d\t",vectorfinal[i].numerador);
            } else
            {
              printf("%d/%d\t",vectorfinal[i].numerador,vectorfinal[i].denominador);
            }
          }
         }
    }
    
    int main() {
      racional vectorinicial[6], vectorfinal[6];
      asignar(&vectorinicial[6],&vectorfinal[6]);
      reducir(&vectorinicial[6],&vectorfinal[6]);
      imprimir(&vectorinicial[6],&vectorfinal[6]);
    }
   
   

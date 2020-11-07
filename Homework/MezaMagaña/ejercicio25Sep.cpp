/*
Autor Joshua Immanuel Meza Magana
Fecha 25/09/2020
Version 1.0.0
Programa que pide dos numeros racionales, y devuelve su suma y multiplicacion.
*/
#include <stdio.h>
#include <iostream>
#include <conio.h>
#include <cmath>
using namespace std;

struct racional{
    private:
    int numeradorUno, denominadorUno;
    int numeradorDos, denominadorDos;
    int numeradorSuma, denominadorSuma;
    int numeradorProducto, denominadorProducto;
    int *listaPrimos=new int[numPrimos];
    int numPrimos=1;
    void reducir(int *, int *);
    void expandirLista();
    public:
    void asignar();
    void suma();
    void producto();
    void imprimir();
};

void racional::reducir(int * numA, int * numB){
    /* Reduce ambos numeros lo mayor posible y encuentra por su cuenta los posibles primos */
    int primo=0, flag=0, i, numActual;

    listaPrimos[0]=2;

    while(sqrt((*numA)*(*numA))>=listaPrimos[primo] && sqrt((*numB)*(*numB))>=listaPrimos[primo]){

        if(*numA%listaPrimos[primo]==0 && *numB%listaPrimos[primo]==0){
            *numA/=listaPrimos[primo];
            *numB/=listaPrimos[primo];
        }else{
            primo++;

            if(primo==numPrimos){
                expandirLista();
                
                numActual=(listaPrimos[numPrimos-2])+1;

                //Criba de Erastostenes
                while(true){
                    for(i=0; i<numPrimos-1;i++){
                        if(numActual%listaPrimos[i]==0){
                            flag=1;
                            break;
                        };
                    };
                    
                    if(flag==0){
                        listaPrimos[numPrimos-1]=numActual;
                        break;
                    }else{
                        flag=0;
                        numActual++;
                    };
                };
            };
        };
    };
};

void racional::expandirLista(){
    /*Expande el tamaño de la lista*/
    numPrimos++;

    int *ptrTemporal=new int[numPrimos];

    for(int i=0;i<numPrimos;i++){
        if(i<numPrimos-1){ /*Copia todos los datos*/
            ptrTemporal[i]=listaPrimos[i];
        }else{ /*Pone 0 en memoria vacia*/
            ptrTemporal[i]=0;
        };
    };

    delete[] listaPrimos; /*Reinicia como puntero al array*/

    listaPrimos=ptrTemporal; 
};

void racional::asignar(){
    /*Pide al usuario los valores y los guarda*/
    cout << "Inserte el primer numerador: ";
    cin >> numeradorUno;
    cout << "Inserte el primer denominador: ";
    cin >> denominadorUno;
    cout << "Inserte el segundo numerador: ";
    cin >> numeradorDos;
    cout << "Inserte el segundo denominador: ";
    cin >> denominadorDos;
    cout << "\n";
};

void racional::suma(){
    /*Suma ambas racionales y las almacena*/
    numeradorSuma = numeradorUno * denominadorDos + numeradorDos * denominadorUno;
    denominadorSuma = denominadorUno * denominadorDos;

    reducir(&numeradorSuma,&denominadorSuma);
};

void racional::producto(){
    /*Multiplica ambas racionales y las almacena*/
    numeradorProducto = numeradorUno * numeradorDos;
    denominadorProducto = denominadorUno * denominadorDos;

    reducir(&numeradorProducto,&denominadorProducto);
};

void racional::imprimir(){
    /*Suma*/
    if(denominadorSuma==0){
        cout << "Suma de fracciones: Indefinido" << endl;
    }else if(numeradorSuma==denominadorSuma){
        cout << "Suma de fracciones: 1" << endl;
    }else if(denominadorSuma==1 || denominadorSuma==-1){
        cout << "Suma de fracciones: " << denominadorSuma*numeradorSuma << endl;
    }else if(numeradorSuma==0){
        cout << "Suma de fracciones: 0" << endl;
    }else if(numeradorSuma<0 && denominadorSuma<0){
        cout << "Suma de fracciones: " << numeradorSuma*-1 << "/" << denominadorSuma*-1 << endl;
    }else if(numeradorSuma<0 || denominadorSuma<0){
        if(numeradorSuma<0){
            cout << "Suma de fracciones: " << numeradorSuma << "/" << denominadorSuma << endl;
        }else{
            cout << "Suma de fracciones: -" << numeradorSuma << "/" << denominadorSuma*-1 << endl;
        };
    }else{
        cout << "Suma de fracciones: " << numeradorSuma << "/" << denominadorSuma << endl;
    };

    /*Producto*/
    if(denominadorProducto==0){
        cout << "Multiplicacion de fracciones: Indefinido" << endl;
    }else if(numeradorProducto==denominadorProducto){
        cout << "Multiplicacion de fracciones: 1" << endl;
    }else if(denominadorProducto==1 || denominadorProducto==-1){
        cout << "Multiplicacion de fracciones: " << denominadorProducto*numeradorProducto << endl;
    }else if(numeradorProducto==0){
        cout << "Multiplicacion de fracciones: 0" << endl;
    }else if(numeradorProducto<0 && denominadorProducto<0){
        cout << "Multiplicacion de fracciones: " << numeradorProducto*-1 << "/" << denominadorProducto*-1 << endl;
    }else if(numeradorProducto<0 || denominadorProducto<0){
        if(numeradorProducto<0){
            cout << "Multiplicacion de fracciones: " << numeradorProducto << "/" << denominadorProducto << endl;
        }else{
            cout << "Multiplicacion de fracciones: -" << numeradorProducto << "/" << denominadorProducto*-1 << endl;
        };
    }else{
        cout << "Multiplicacion de fracciones: " << numeradorProducto << "/" << denominadorProducto << endl;
    };

    delete[] listaPrimos;
};

int main(){
    racional r;

    r.asignar();
    r.suma();
    r.producto();
    r.imprimir();

    return 0;
};
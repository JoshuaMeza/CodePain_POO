/*
Author Joshua Immanuel Meza Magana
Date 04/10/2020
Version 1.0.0
Program wich creates a random array of 3*3 and generates their inverse.
*/
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <ctime>
#include <cstdlib>
using namespace std;

struct Rational{
    private:
        int num;
        int den;
        int euclidsAlgorithm(int,int);
        int generateRandom();
    public:
        void asignRandom();
        void asignNumber(int);
        void reduceRationals();
        float verifySign();
        void doSume(Rational, Rational);
        void doDivision(Rational);
        void makeAbsolute();
        void makeNegative();
        void printCouple();
};

struct GaussJordan{
    private:
        Rational array[6][3];
    public:
        void generateArray();
        void guideProgress();
        void printArray();
};

int Rational::euclidsAlgorithm(int num, int den){
    /* Gets the greatest common factor */
    int rest = num % den;

    if(rest != 0){
        den=euclidsAlgorithm(den, rest);
    }

    return den;
}

int Rational::generateRandom(){
    /* Generates random numbers avoiding the 0 */
    int randomNumber =(rand() % 10);

    if(randomNumber == 0){
        randomNumber = generateRandom();
    }

    return randomNumber;
}

void Rational::asignRandom(){
    /* Asigns the numbers */
    num=generateRandom();
    den=generateRandom();
}

void Rational::asignNumber(int number){
    /* Asigns specific numbers */
    num = number;
    den = 1;
}

void Rational::reduceRationals(){
    /* Divide the number with their greatest common factor */
    int mcd;

    if(num != 0 && den != 0){

        if(num > den){ // Giving order
            mcd=euclidsAlgorithm(num, den);
        }else{
            mcd=euclidsAlgorithm(den, num);
        }

        num/=mcd;
        den/=mcd;

    }else if(den == 0){ // Undefined
        cout << "ERROR - DENOMINATOR EQUAL TO 0" << endl;
        exit(-1);
    }else{ // 0 division reduction
        den=1;
    }

    if(den<0){
        num *= -1;
        den *= -1;
    }
}

float Rational::verifySign(){
    /* Used to know the sign of the number */
    float number = (float)num/(float)den;

    return(number);
}

void Rational::doSume(Rational selectedNumber, Rational original){
    /* Sume of fractions */ 
    Rational _aux; //Recreate the another fraction
    _aux.num = selectedNumber.num * original.num;
    _aux.den = selectedNumber.den * original.den;

    _aux.reduceRationals();

    num = (_aux.den) * num + (_aux.num) * den;
    den *= (_aux.den);
}

void Rational::doDivision(Rational aux){
    /* Makes the final division */
    num *= aux.den;
    den *= aux.num;
}

void Rational::makeAbsolute(){
    num = abs(num);
    den = abs(den);
}

void Rational::makeNegative(){
    num *= -1;
}

void Rational::printCouple(){
    /* Prints a rational */
    if(den<0){
        cout << num*-1 << "/" << den*-1;
    }else{
        cout << num << "/" << den;
    }
    
}

void GaussJordan::generateArray(){
    /* Asigns every number */
    int i, j;

    for(j=0; j<3; j++){
        for(i=0; i<3; i++){
            array[i][j].asignRandom();
            if(i == j){
                array[i+3][j].asignNumber(1);
            }else{
                array[i+3][j].asignNumber(0);
            }
        }
    }
}

void GaussJordan::guideProgress(){
    /* Algorithm in steps */
    Rational r1, r2;
    int h, i, j;
    float verifier;

    // (0,1) y (0,2)
    r1 = array[0][0]; // Principal line fraction

    for(i=0; i<6; i++){
        array[i][0].doDivision(r1);
        array[i][0].reduceRationals();
    }
    
    for(h=0; h<2; h++){
        verifier = array[0][h+1].verifySign(); // Selected fraction

        r2 = array[0][h+1]; // Selected fraction copy

        if(verifier > 0){ // Only two existing cases (num2 pos or neg)
            r2.makeNegative(); // Makes -num2 * 1

            for(i=0; i<6; i++){
                array[i][h+1].doSume(r2, array[i][0]);
                array[i][h+1].reduceRationals();
            }
        }else{
            r2.makeAbsolute(); // Makes num2 * 1

            for(i=0; i<6; i++){
                array[i][h+1].doSume(r2, array[i][0]);
                array[i][h+1].reduceRationals();
            }
        }
    }

    // (1,0) y (1,2)
    r1 = array[1][1]; // Principal line fraction

    for(i=0; i<6; i++){
        array[i][1].doDivision(r1);
        array[i][1].reduceRationals();
    }

    for(h=0; h<3; h=h+2){
        verifier = array[1][h].verifySign(); // Selected fraction

        r2 = array[1][h]; // Selected fraction copy

        if(verifier > 0){ // Only two existing cases (num2 pos or neg)
            r2.makeNegative(); // Makes -num2 * 1

            for(i=0; i<6; i++){
                array[i][h].doSume(r2, array[i][1]);
                array[i][h].reduceRationals();
            }
        }else{
            r2.makeAbsolute(); // Makes num2 * 1

            for(i=0; i<6; i++){
                array[i][h].doSume(r2, array[i][1]);
                array[i][h].reduceRationals();
            }
        }
    }

    // (2,0) y (2,1)
    r1 = array[2][2]; // Principal line fraction

    for(i=0; i<6; i++){
        array[i][2].doDivision(r1);
        array[i][2].reduceRationals();
    }

    for(h=0; h<2; h++){
        verifier = array[2][h].verifySign(); // Selected fraction

        r2 = array[2][h]; // Selected fraction copy

        if(verifier > 0){ // Only two existing cases (num2 pos or neg)
            r2.makeNegative(); // Makes -num2 * 1

            for(i=0; i<6; i++){
                array[i][h].doSume(r2, array[i][2]);
                array[i][h].reduceRationals();
            }
        }else{
            r2.makeAbsolute(); // Makes num2 * 1

            for(i=0; i<6; i++){
                array[i][h].doSume(r2, array[i][2]);
                array[i][h].reduceRationals();
            }
        }
    }

    // Division
    for(j=0; j<3; j++){
        for(i=0; i<6; i++){
            array[i][j].doDivision(array[j][j]);
            array[i][j].reduceRationals();
        }
    }
}

void GaussJordan::printArray(){
    int i, j;

    cout << "Table:" << endl;
    for(j=0; j<3; j++){
        cout << "|  ";
        
        for(i=0; i<6; i++){
            array[i][j].printCouple();
            cout << "  |  ";
        }

        cout << endl;
    }
}

int main(){
    srand((unsigned) time(0));
    GaussJordan g;
    
    g.generateArray();
    g.printArray();
    g.guideProgress();
    g.printArray();

    return 0;
}
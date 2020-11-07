/*
Author Joshua Immanuel Meza Magana
Date 26/09/2020
Version 1.0.0
Program wich generates 3 random rational numbers and turn them into 1 0 0.
*/
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <ctime>
using namespace std;

struct rational{
    private:
    int originalArray[3][2]={{0,0}, {0,0} , {0,0}}; // Original to print
    int finalArray[6][2]={{0,0}, {0,0}, {0,0}, {1,1}, {0,1}, {0,1}}; // Final in where the program works
    void reduceRationals(int *, int*);
    int generateRandom();
    int euclidsAlgorithm(int, int);
    public:
    void createRationals();
    void transformRationals();
    void printResults();
};

void rational::reduceRationals(int *numA, int *numB){
    /* Reduce the rational */
    int mcd;

    if(*numA != 0 && *numB != 0){
        if(*numA > *numB){ // Giving order
            mcd=euclidsAlgorithm(*numA, *numB);
        }else{
            mcd=euclidsAlgorithm(*numB, *numA);
        }

        *numA/=mcd;
        *numB/=mcd;
    }
}

int rational::generateRandom(){
    /* Generates a random number, if its 0, then generates another */
    int randomNumber =(rand() % 10);

    if(randomNumber == 0){
        randomNumber = generateRandom();
    }

    return randomNumber;
}

int rational::euclidsAlgorithm(int numerator, int denominator){
    /* Finds the mcd */
    // Numerator has to be bigger than denominator
    int rest = numerator % denominator;

    if(rest != 0){
        denominator=euclidsAlgorithm(denominator, rest);
    }

    return denominator;
}

void rational::createRationals(){
    /* Asigns the numbers */
    for(int i=0; i<3; i++){
        // Original Array
        originalArray[i][0] = generateRandom();
        originalArray[i][1] = generateRandom();
        reduceRationals(&originalArray[i][0], &originalArray[i][1]);
        // Needed to work
        finalArray[i][0] = originalArray[i][0];
        finalArray[i][1] = originalArray[i][1];
    }
}

void rational::transformRationals(){
    /* Makes the array become: 1 0 0 [number/number] [number/number] [number/number] */
    int i;

    // F1 * 1/F1
    for(i=0; i<4; i=i+3){
        finalArray[i][0] *= originalArray[0][1];
        finalArray[i][1] *= originalArray[0][0];
        reduceRationals(&finalArray[i][0], &finalArray[i][1]);
    }
    
    // F2 * R3 - F3 * F2
    for(i=1; i<5; i=i+3){
        finalArray[i][0] = finalArray[i][0] * originalArray[2][0] - originalArray[2][0]*originalArray[1][0];
        finalArray[i][1] = originalArray[1][1] * originalArray[2][1];
        reduceRationals(&finalArray[i][0], &finalArray[i][1]);
    }

    // F3 * R2 - F2 * F3
    for(i=2; i<6; i=i+3){
        finalArray[i][0] = finalArray[i][0] * originalArray[1][0] - originalArray[1][0]*originalArray[2][0];
        finalArray[i][1] = originalArray[2][1] * originalArray[1][1];
        reduceRationals(&finalArray[i][0], &finalArray[i][1]);
    }
}

void rational::printResults(){
    /* Prints the results */
    printf("-----------------------------------------------\n");
    printf("Original  | %d/%d | %d/%d | %d/%d | 1 | 0 | 0 |\n",originalArray[0][0],originalArray[0][1],originalArray[1][0],originalArray[1][1],originalArray[2][0],originalArray[2][1]);
    printf("-----------------------------------------------\n");
    printf("New       | %d | %d | %d | %d/%d | %d/%d | %d/%d |\n",finalArray[0][0],finalArray[1][0],finalArray[2][0],finalArray[3][0],finalArray[3][1],finalArray[4][0],finalArray[4][1],finalArray[5][0],finalArray[5][1]);
    printf("-----------------------------------------------\n");
    printf("Procedure | F1 * 1/F1 \n");
    printf("          | %d/%d * F2 - %d/%d * F3\n",originalArray[2][0],originalArray[2][1],originalArray[1][0],originalArray[1][1]);
    printf("          | %d/%d * F3 - %d/%d * F2\n",originalArray[1][0],originalArray[1][1],originalArray[2][0],originalArray[2][1]);
    printf("-----------------------------------------------");
}

int main(){
    srand((unsigned) time(0));
    rational r;

    r.createRationals();
    r.transformRationals();
    r.printResults();

    return 0;
}
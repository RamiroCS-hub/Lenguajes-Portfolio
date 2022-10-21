#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int contr,Ncj=0,cont[20],CCont[20], x=0;
int longitud, cantC;
int numC = 0;
//Letras para copiar n,b,N
int flag = 0;
struct Cajas{
    int cantC;
    char name[20];
    struct Cajas *sigC;//puntero que apunta a la siguiente caja
}Caja1;

//Iniciamos los punteros de tipo struct 
struct Cajas *inicio = &Caja1; // Puntero que siempre apunta a la primera caja
struct Cajas *pC = NULL; // Puntero que se mueve en las cajas

void agregarObjetos(void);
void Ordenamiento(int*,int);
void CheckC(void);
void intercambiar(int*, int*);
void showStruc(void);

int main(){
    system("@cls||clear");
    
    printf("Ingrese en cuantas cajas va a ordenar las cosas\n");
    scanf("%d",&cantC);
    for(int i = 0; i<cantC;i++){
        pC = malloc(sizeof(Caja1)); //Hago una lista con la cantidad de cajas que me pide el usuario
        struct Cajas* Aux = inicio;
        
        while(Aux->sigC != NULL){
            Aux = Aux->sigC;
        }
        Aux->sigC = pC;
        pC->sigC = NULL;
    }
    pC = &Caja1; //Puntero que se mueve en las cajas
    do{
        agregarObjetos();
        Ncj++;
    }while(Ncj!=cantC);
    
    longitud = sizeof cont / sizeof cont[0];
    
    //Ordenamos e imprimimos
    Ordenamiento(cont,longitud);
    printf("Imprimiendo despues de ordenar...\n");
    CheckC();
    //Para ver los objetos de una caja en particular
    showStruc();
 return 0;
}

void CheckC(){
    int c=0;
    for(int i=0; i<10; i++){
        for(int j=0; j<10; j++){
            if(cont[i] == CCont[j] && CCont[j] != 0) {c+=j;}
        }
        if(cont[i] != 0)
            {c++;printf("Cantidad de objetos en la caja %d: %d\n", c, cont[i]);}
        c=0;
    }
}
    
void agregarObjetos(){
        int contr = 1, i=0;
        numC++;
        char concat[250] = {0};
        while(contr!=0){
            //int x, es la posición de cada caja.
            system("@cls||clear");
            
            printf("Esta es la %d caja\n",numC);
            printf("Ingrese un objeto\n");
            //Se va agregando ojetos a la caja cada vez que se cumple un ciclo del while
            
            scanf("%s",pC->name);
            
            printf("Ingrese 1 para agregar otro objeto o 0 para pasar a otra caja\n");
            scanf("%d",&contr);
            
            strcat(concat,pC->name);
            strcat(concat,",");
            
            i++;
            //Representan los dos el total de objetos y su index la caja en la que se encuentran, uno lo ordeno y el otro no
            cont[x]++;
            CCont[x]++; 
        }
        //Copio en pC->name todos los objetos de esa caja
        strcpy(pC->name,concat);
        x++;
        
        pC = pC->sigC;
    }
void showStruc(){
    int caja;
    pC = inicio;
    printf("De que caja quiere ver los objetos? \n");
    scanf("%d",&caja);
    for(int i=1; i<caja ; i++){
        pC = pC->sigC;
    }
    printf("Los objetos de esa caja: \n");
    printf("%s \n",pC->name);
}    
    
void Ordenamiento(int cont[], int longitud) {
    for (int X = 0; X < longitud; X++) {
        for (int indiceActual = 0; indiceActual < longitud - 1;indiceActual++) {
            int indiceSiguienteElemento = indiceActual + 1;
            
            if (cont[indiceActual] < cont[indiceSiguienteElemento]) {
            intercambiar(&cont[indiceActual], &cont[indiceSiguienteElemento]);
            } 
        }
    }
}

void intercambiar(int *a, int *b){
    int temporal = *a;
    *a = *b;
    *b = temporal;
}


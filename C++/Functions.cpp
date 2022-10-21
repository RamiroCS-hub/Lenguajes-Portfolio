#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <vector>

using namespace std;
//Letras para copiar n,b,N

//PROTOTIPOS
string login(void);
vector<string> firstRead(void);

class passManager{
    public:
        string passI;
        string pass;
        string nameU;
        string passU;
        vector<string> datosTest;
        int pos;
        passManager(string user,vector<string> datos){
            this->nameU = user;
            this->datosTest = datos;
        };
        void addPass(void);
        void readPass(void);
        void posUser(void);
        void printAll(void);
        void removePass(void);
};

vector<string> firstRead(){
    ifstream archivo("datos.txt");
    vector<string> datosTest;
    string datos,test;
    //LEO TODO EL ARCHIVO
    while(!archivo.eof()){
        archivo>>datos;
        datosTest.push_back(datos);
    }   
    return datosTest;
}
//METODOS
void passManager::posUser(void){
    int i=0;
    int pos2 = 0;
    bool flag;
    //ME FIJO LA POS DEL NAME QUE INGRESO EL USUARIO
    for(string test : this->datosTest){
        if(test == this->nameU){
            pos2 = i;
            flag = true;
        }
        i++;
    }
    if(flag == false){
        this->pos = 1;
        this->datosTest.insert(this->datosTest.begin(),this->nameU);
        this->datosTest.insert(this->datosTest.begin() + this->pos,"&");
    }else{
        this->pos = pos2 + 1;
    }
}

void passManager::addPass(){
    cout<<"Ingrese a que va a pertenecer la contraseña"<<endl;
    cin>>this->passI;
    cout<<"Ingrese la contraseña"<<endl;
    cin>>this->pass;
    this->datosTest.insert(this->datosTest.begin() + this->pos,passI); //agrego lo que me pide al lado del nomre del usuario 
    this->datosTest.insert(this->datosTest.begin() + this->pos + 1,pass);
    cout<<"[0] Para volver al menu"<<endl
        <<"[4] Para salir"<<endl;
}
string login(){
    string name;
    cout<<"Ingrese su name: ";
    cin>>name;
    return name;
}
// vector<string> copyVector(const vector<string>& original){
//   vector<string> newVec;
//   newVec.reserve(original.size());
//   copy(original.begin(), original.end(), back_inserter(newVec));
//   return newVec;
// }

void passManager::readPass(){
    int i = this->pos;
    string contra;
    cout<<"Sus contraseñas son: "<<endl;
    //PRINTEO SOLO LAS CONTRASEÑAS DE EL USUARIO EN USO
    for(string test : this->datosTest){
        if(test == this->nameU){
            while(this->datosTest[i] != "&"){
                cout<<datosTest[i]<<" ";
                i+=2;
            }
        }
    }
    i = this->pos;
    
    cout<<endl<<"Que contraseña quiere ver?"<<endl;
    cin>>contra;
    while(this->datosTest[i] != "&"){
        if(this->datosTest[i] == contra){
            cout<<datosTest[i]<<":"<<datosTest[i + 1];
        }
        i++;
    }
    cout<<endl;
    cout<<"[0] Para volver al menu"<<endl
        <<"[4] Para salir"<<endl;
}
void passManager::removePass(){
    int i = this->pos;
    string passR;
    bool flag = false;
    cout<<"Estas son sus contraseñas:"<<endl;
    for(string test : this->datosTest){
        if(test == this->nameU){
            while(this->datosTest[i] != "&"){
                cout<<this->datosTest[i]<<" "; //Imprimo solo el nomre de las contraseñas
                i+=2;
            }
        }
    }
    cout<<endl<<"Escriba la que quiere remover"<<endl;
    cin>>passR;
    int z=0;
    for(string test : this->datosTest){
        if(test == passR){ // busco la contraseña que se pidio
            this->datosTest.erase(this->datosTest.begin()+z);
            this->datosTest.erase(this->datosTest.begin()+z);
            flag = true;
        }
        z++;
    }
    if(flag == false){
        cout<<"No existe la contraseña para borrar"<<endl;
    }else{
        cout<<"Se borro la contraseña correctamente"<<endl;
    }
    cout<<"[0] Para volver al menu"<<endl
        <<"[4] Para salir"<<endl;
}
void passManager::printAll(){
    ofstream archivo("datos.txt");
    for(string test : this->datosTest){
        archivo<<test<<" ";
    }
    archivo.close();
}
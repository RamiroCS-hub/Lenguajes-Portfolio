#include "Functions.h"
//Letras para copiar n,b,N
int op=0;

int main(){
    passManager *metodP; // defino un puntero de tipo passManager que es la clase
    string name = login();
    vector<string> datos = firstRead();
    passManager user1(name,datos);
    metodP = &user1; // apunto el puntero hacia el ojeto que creao
    metodP->posUser();
    while(op != 4){
        switch(op){
            default:
                system("@cls||clear");
                cout<<"\t"<<"WELCOME "<<name<<endl;
                cout<<"[1] Para agregar una nueva contraseña"<<endl
                    <<"[2] Para ver sus contraseñas"<<endl
                    <<"[3] Para borrar alguna contraseña"<<endl
                    <<"[4] Para salir"<<endl;
                cin>>op;
                break;
            case 1:
                system("@cls||clear");
                metodP->addPass();
                cin>>op;
                break;
            case 2:
                system("@cls||clear");
                metodP->readPass();
                cin>>op;
                break;
            case 3:
                system("@cls||clear");
                metodP->removePass();
                cin>>op;
                break;
        }
    }
    metodP->printAll();
    return 0;
}
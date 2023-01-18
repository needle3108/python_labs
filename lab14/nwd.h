#ifndef NWD_H
#define NWD_H

int NWD(int a, int b){
    if(b==0){
        return a;
    }
    else return NWD(b, a%b);
}

#endif
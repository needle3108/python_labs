#ifndef FUNKCJA_H
#define FUNKCJA_H

void sort(int *T, int s){
    for(int i=1; i<s; i++){
        int el = T[i];
        int j = i - 1;
        while(j>=0 && T[j]>el){
            T[j+1] = T[j];
            --j;
        }
        T[j+1] = el;
    }
}

#endif
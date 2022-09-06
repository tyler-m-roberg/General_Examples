#include "sum_array.h"

EXPORT int sum_array(double arr[], double* result, int size){
    double sum = 0;

    for(int i = 0; i < size; i++){
        
        sum+=(arr[i]*2);
    }

    *result = sum;
    return 1;
}
#include <iostream>
#include "cpl.h"

int main() {
    Complex a(1,1);
    Complex b = a+a;
    Complex::mode(POLAR);
    std::cout <<(b)<<std::endl;
    std::cout <<(b);
    return 0;
}

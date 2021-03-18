#ifndef  COMPLEX_HPP
#define  COMPLEX_HPP
#define POLAR 0x1
#define RET 0x2

#include <ostream>
#include <iostream>

class Complex {
private:
    double r, i;

public:
    Complex(double a, double b, int mode = RET);

    double real();

    double imaginario();

    double arg();

    double abs();

    Complex operator+( Complex &a);

    Complex operator-( Complex &a);

    Complex operator*( Complex &a);

    Complex operator/(Complex a);

    std::string toString(int mode = RET, unsigned int ndec = 4);

    friend std::ostream &operator<<(std::ostream &os, Complex obj);
    static void mode(int md);

protected:
    static int defaultRpr;

};

#endif

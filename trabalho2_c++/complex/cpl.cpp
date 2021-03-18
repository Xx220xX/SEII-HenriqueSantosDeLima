#include"cpl.h"
#include<cmath>
#include <memory>

Complex::Complex(double a, double b, int mode) {
    this->r = a;
    this->i = b;
    if (mode == POLAR) {

        this->r = a * cos(b);
        this->i = a * sin(b);
    }
}

template<typename ... Args>
std::string string_format(const std::string &format, Args ... args) {
    int size = snprintf(nullptr, 0, format.c_str(), args ...) + 1;
    if (size <= 0) { return ""; }
    std::unique_ptr<char[]> buf(new char[size]);
    snprintf(buf.get(), size, format.c_str(), args ...);
    return std::string(buf.get(), buf.get() + size - 1);
}

double Complex::real() {
    return this->r;
}

double Complex::imaginario() {
    return this->i;
}

double Complex::arg() {
    return atan2(r, i);
}

double Complex::abs() {
    return sqrt(r * r + i * i);
}

Complex Complex::operator+( Complex &b) {
    return Complex(r + b.r, i + b.i);
}

Complex Complex::operator-( Complex &b) {
    return Complex(r - b.r, i - b.i);
}

Complex Complex::operator*( Complex &b) {
    return Complex(r * b.r - i * b.i, i * b.r + b.i * r);
}

Complex Complex::operator/(Complex b) {
    return Complex(this->abs() / b.abs(), arg() - b.arg());
}

std::string Complex::toString(int mode, unsigned int ndec) {
    std::string s;

    double angle;
    switch (mode) {
        case POLAR:
            angle = this->arg() / M_PI * 180.0;
            s = string_format(("%." + std::to_string(ndec) + "lf{%." + std::to_string(ndec) + "lf}"),
                              this->abs(), angle);
            break;
        case RET:
            double im = this->i;
            char sum = '+';
            if (im < 0) {
                sum = '-';
                im = -im;
            }
            s = string_format(
                    (std::string("%.") + std::to_string(ndec) + "lf" + sum + "%." + std::to_string(ndec) + "lf"),
                    this->r, im);
            break;

    }
    return s;
}

std::ostream &operator<<(std::ostream &os, Complex obj) {
    return os << obj.toString(Complex::defaultRpr);
}
int Complex::defaultRpr = RET;

void Complex::mode(int md) {
    if (md==RET || POLAR)
    Complex::defaultRpr = md;
}



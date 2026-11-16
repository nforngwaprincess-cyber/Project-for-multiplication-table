#include <iostream>
#include <cmath>
using namespace std;
int main(){
	double a, b, c;
	
	cout <<"Enter a, b, c: ";
    cin >> a >> b >> c;
    if (a == 0) {
    	cout << "Not a quadratic equation." << endl;
    return 0;
}

double D = b * b - 4 * a *c;

if (D > 0){
	double r1 = (-b + sqrt(D)) / (2 * a);
	double r2 = (-b - sqrt(D)) / (2 * a);
	cout << "Real and distinct roots:" << r1 << " and " << r2 << endl;
}
else if (D == 0) {
	double r = -b / (2 * a);
	cout << "Equal roots: " << r << endl;
}
else {
     double real = -b / (2 * a);
	 double imag = sqrt(-D) / (2 * a);
	 cout  << "complex roots: " << real << " + " << imag << "i and "
	       << real << " - " << imag << " i " << endl;
  }
  return 0 ; 
} 

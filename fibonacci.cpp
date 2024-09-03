#include <iostream>
#include <cmath>

using namespace std;

bool eQuadradoPerfeito(int num) {
    int raiz = static_cast<int>(sqrt(num));
    return raiz * raiz == num;
}

bool pertenceAFibonacci(int n) {
    return eQuadradoPerfeito(5 * n * n + 4) || eQuadradoPerfeito(5 * n * n - 4);
}

int FibonacciRecursivo(int N) {
    int ret;
    if (N <= 0){
        ret -1;
    } else{
        if(N == 1){
            ret = 0;
        } else 
            if(N == 2){
                ret = 1;
            }else{
            ret = FibonacciRecursivo(N - 1) + FibonacciRecursivo(N - 2);
        }
    }
    return ret;
}

void imprimirSequenciaFibonacciRecursivo(int n, int pos = 1) {
    int fib = FibonacciRecursivo(pos);
    if (fib > n) return;  
    if (pos > 1) cout << ", ";
    cout << fib;
    imprimirSequenciaFibonacciRecursivo(n, pos + 1);  
}

int main() {
    setlocale(LC_ALL, "Portuguese");
    int numero;

    cout << "Digite um número para verificar se pertence à sequência de Fibonacci: ";
    cin >> numero;

    if (pertenceAFibonacci(numero)) {
        cout << numero << " pertence à sequência de Fibonacci." << endl;
        imprimirSequenciaFibonacciRecursivo(numero);
        cout << endl;
    } else {
        cout << numero << " não pertence à sequência de Fibonacci." << endl;
    }
    return 0;
}

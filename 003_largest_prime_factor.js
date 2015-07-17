//Problem 3 - Largest prime factor
//The prime factors of 13195 are 5, 7, 13 and 29.
//What is the largest prime factor of the number 600851475143 ?


console.log('Exercise 3 - Highest prime number is: ' +
    findPrimeVersion(600851475143));

function findPrimeVersion(_startNum) {
    var solution = _startNum;
    for (i = 2; i < solution; i++) {
        if (solution % i == 0) {
            solution = findPrimeVersion(solution / i);
        }
    }
    return solution;
}

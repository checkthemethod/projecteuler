//Problem 6 - Sum square difference
//Find the difference between the sum of the squares 
//of the first one hundred natural numbers and the square of the sum.

console.log('Exercise 6: Difference is ' +
    (squareOfsumOfFirstNNaturalNumbers(100) -
    sumOfFirstNNaturalNumbers(100)));

function sumOfFirstNNaturalNumbers(_n) {
    var sum = 0;
    for (var i = 1; i <= _n; i++) {
        sum += i * i;
    }
    return sum;
}

function squareOfsumOfFirstNNaturalNumbers(_n) {
    var sum = 0;
    for (var i = 1; i <= _n; i++) {
        sum += i;
    }
    return sum * sum;
}

// Problem 7 - 10001st prime
// By listing the first six prime numbers: 
// 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
// What is the 10 001st prime number?

console.log('Exercise 7 - 10001st prime number is: '+logPrimeNumbers(10001));

function isItPrime(_num) {
	for(var i = 2; i < _num; i++) {

		if(_num%i == 0) {
		return false;
	}

	}
	

	return true;
}



function logPrimeNumbers(_limit) {
	var primeNumberArray = [],
	i = 2;

	while(primeNumberArray.length < _limit) {
		if(isItPrime(i)) {
			primeNumberArray.push(i);
		}

		i++;
	}

return primeNumberArray[_limit-1];
}
//loop through numbers
//
//while array is not at 10002
// keep checking numbers
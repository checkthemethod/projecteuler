//Problem 1 - Multiples of 3 and 5
//If we list all the natural numbers below 10 that are multiples of 3 or 5, 
//we get 3, 5, 6 and 9. The sum of these multiples is 23.
//Find the sum of all the multiples of 3 or 5 below 1000.

console.log('Exercise 1 - Sum of all multiples of 3 under 1000 is: ' + getSumOfMultiples());

function getSumOfMultiples() {
	var i = 0,
	finalSum = 0;

	while(i < 1000) {
		if(i%3 == 0 || i%5 == 0 ) {
			finalSum+=i;
		}

		i++;
	}
	return finalSum;
}

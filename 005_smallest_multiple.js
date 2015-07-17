//Problem 5 - Smallest multiple
//2520 is the smallest number that can be divided by 
//each of the numbers from 1 to 10 without any remainder.
//What is the smallest positive number that is 
//evenly divisible by all of the numbers from 1 to 20?


console.log('Exercise 5 - Smallest number is: '+findSmallestNumber(20));

function findSmallestNumber(_limit) {
	var solution = 2; //start with even number

	while(!isDivisible(solution, _limit)) {
		solution+=2; //add 2 to keep it even
	}
	return solution;
}

function isDivisible(_solution, _limit) {
	for(var i=1; i<_limit; i++) {
		if(_solution%i !== 0 ) {
			return false;
		}
	}
	return true;
}
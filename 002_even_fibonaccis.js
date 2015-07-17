// create fibonacci sequencer
console.log('Exercise 2 - Sum of all even multiples is: '+ getMultipleOf2Sum(runFibonacci()));

function runFibonacci() {
	var i= 1,
	fibonacciArray = [],
	limit = 4000000;
	while(i < limit) {
		if(fibonacciArray[fibonacciArray.length-2]  == null) {

			fibonacciArray.push(i);
			i++;
		} else {
			fibonacciArray.push(i);
			i = fibonacciArray[fibonacciArray.length-1]+fibonacciArray[fibonacciArray.length-2];
		}
	}

	return fibonacciArray;
}

//get sum from the multiples of 2 from the fibonnaci array
function getMultipleOf2Sum(_fibonacciArray) {
	var sum = 0;
	for(var i=0;i<_fibonacciArray.length;i++) {
		if(_fibonacciArray[i]%2 == 0) {
			sum += _fibonacciArray[i];
		}
	}
	return sum;
}




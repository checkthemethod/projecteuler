//Problem 4 - Largest palindrome product
//A palindromic number reads the same both ways. 
//The largest palindrome made from the product 
//of two 2-digit numbers is 9009 = 91 × 99.
//Find the largest palindrome made from the product of two 3-digit numbers.


console.log('Exercise 4 - largest palindrome is: '+findPalindrome(1000));

function findPalindrome(_testNum) {

	var limit = _testNum,
	forwardVal = 0,
	reverseVal = 0,
	highestVal = 0,
	firstMultiple = 0,
	secondMultiple = 0;

	for(var i = limit; i > 99; i--) {

		for(var j = limit; j > 99; j--) {
			forwardVal = j*i;
			reverseVal = reverseNumber(forwardVal);
			if(forwardVal == reverseVal) {
				if(forwardVal > highestVal){
					firstMultiple = i;
					secondMultiple = j;
					highestVal = forwardVal;
				}
			}
		}
	}
	return highestVal;
}



function reverseNumber(_value){
	var stringVal = String(_value);
	var testArray = stringVal.split("");
	var test = testArray.reverse();
	var newNum = Number(test.join(''));
	return newNum;
}



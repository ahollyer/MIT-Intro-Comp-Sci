var primes = [];
var i = 1;

while(primes.length <= 1000) {
	divisor = 2;
	while(divisor < i/2){
		if(i % divisor != 0) {
			divisor++;
		}
		else {
			i++;
		}
		primes += i;
	}
}

print(primes);
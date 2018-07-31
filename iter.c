#import <stdio.h>
int main(void){
	unsigned long long int big = 52*52*52*52*52;
	for(unsigned long long int i=0;i<big;i++){
		printf("%lld\n",i);
	}
}


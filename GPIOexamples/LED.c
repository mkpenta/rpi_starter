#include <wiringPi.h>

int main(void)
{
	wiringPiSetup();
	pinMode(0, OUTPUT);	 //pin 0 = 17, see wiring pi docs
	
	
	digitalWrite(0, HIGH);
	delay(500);
	digitalWrite(0, LOW);
	delay(500);

	return 0;
}

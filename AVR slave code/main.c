
// avrdude -p atmega32 -c stk500v1 -P COM4 -b19200 -Uflash:w:D:\Microcontroler\AVR\AVR_COMPLIE\main.hex:i
//(1MHZ)  avrdude -p atmega32 -c stk500v1 -P COM4 -b19200 -U lfuse:w:0xe1:m -U hfuse:w:0x99:m
//(8MHZ) avrdude -p atmega32 -c stk500v1 -P COM4 -b19200 -U lfuse:w:0xe4:m -U hfuse:w:0x99:m

#include "uart.h"
#include <avr/io.h>

// function prototypes
void Timer_config(void);
void Motor1(int Duty_cycle);
void Motor_config(void);
void Motor_forward(void);
void Motor_backward(void);
void Motor_stop(void);
void Motor_mapping(char val);


int main(void) 
{
	int arr[2];
	int i = 0;	// counter for arr
	uint8_t x; // dummy variable
    UART_Init(9600);  /* Initialize UART at 9600 baud rate */
	Motor_config();
	Timer_config();
    
    while(1)
    {	
		arr[i] = UART_RxChar();
		// handle first element of the arr
		if(arr[i] == 49)	Motor_forward();
		if(arr[i] == 50)	Motor_backward();
		if(arr[i] == 51)	{Motor_forward(); Motor_mapping(57);}
		if(arr[i] == 52)	Motor_stop();
		
		i++; 
		arr[i] = UART_RxChar();
		// handle second element of the arr
		if(arr[i] == 42)		x = x;// astrisk	// do nothing
		else
		{
			Motor_mapping(arr[i]);// send duty cycle
		}
		i = 0;	// clear arr index counter

    }

    
    return (0);
}

void Motor_config(void)
{
	DDRB |= (1<<PINB0) | (1<<PINB1);
}

void Motor_forward(void)
{
	PORTB |= 1<<PINB0;
	PORTB &= ~(1<<PINB1);
}

void Motor_backward(void)
{
	PORTB |= 1<<PINB1;
	PORTB &= ~(1<<PINB0);
}

void Motor_stop(void)
{
	PORTB &= ~(1<<PINB0);
	PORTB &= ~(1<<PINB1);
}

void Motor_mapping(char val)
{
	if(val == 48)	Motor1(0);
	if(val == 49)	Motor1(100);
	if(val == 50)	Motor1(4000);
	if(val == 51)	Motor1(4500);
	if(val == 52)	Motor1(5500);
	if(val == 53)	Motor1(5000);
	if(val == 54)	Motor1(7000);
	if(val == 55)	Motor1(10000);
	if(val == 56)	Motor1(15000);
	if(val == 57)	Motor1(19000);
}

// timer1 OCR1A function
void Motor1(int Duty_cycle)
{
	// Pulse width range
	OCR1A = ICR1 - Duty_cycle;
}

void Timer_config(void)
{
	// making the 2 pwm pins as output
	DDRD |= (1<<PIND5) | (1<<PIND4);
	// 8 prescalling
	TCCR1B |= 1<<CS11;
	// Waveform Generation Mode (Fast PWM)
	TCCR1A |= 1<<WGM11;
	TCCR1B |= (1<<WGM12) | (1<<WGM13);
	// inverting mode (Table 17-3.)
	TCCR1A |= (1<<COM1A1) | (1<<COM1A0);
	TCCR1A |= (1<<COM1B1) | (1<<COM1B0);
	// ICR top count
	ICR1 = 19999; // 0:19999 = 20000 indicates 50hz pulse for controlling servos
}

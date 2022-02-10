#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <irq.h>
#include <uart.h>
#include <console.h>
#include <generated/csr.h>

#include "delay.h"

static char *readstr(void)
{
	char c[2];
	static char s[64];
	static int ptr = 0;

	if(readchar_nonblock()) {
		c[0] = readchar();
		c[1] = 0;
		switch(c[0]) {
			case 0x7f:
			case 0x08:
				if(ptr > 0) {
					ptr--;
					putsnonl("\x08 \x08");
				}
				break;
			case 0x07:
				break;
			case '\r':
			case '\n':
				s[ptr] = 0x00;
				putsnonl("\n");
				ptr = 0;
				return s;
			default:
				if(ptr >= (sizeof(s) - 1))
					break;
				putsnonl(c);
				s[ptr] = c[0];
				ptr++;
				break;
		}
	}
	return NULL;
}

static char *get_token(char **str)
{
	char *c, *d;

	c = (char *)strchr(*str, ' ');
	if(c == NULL) {
		d = *str;
		*str = *str+strlen(*str);
		return d;
	}
	*c = 0;
	d = *str;
	*str = c+1;
	return d;
}

static void prompt(void)
{
	printf("RUNTIME>");
}

static void help(void)
{
	puts("Available commands:");
	puts("help                            - this command");
	puts("reboot                          - reboot CPU");
	puts("led                             - led test");
	puts("IR				- IR test");
	puts("w				- wheels test");
}

static void reboot(void)
{
	ctrl_reset_write(1);
}

static int recibirForma(void)
{

		unsigned int Forma = 0;

		Forma = VGA_Mapa_Forma_read();

		return Forma;	
		
}

static void led_test(void)
{
	unsigned int form = 0;
	printf("Test del los leds... se interrumpe con el botton 1\n");
	while(!(buttons_in_read()&1)) {

		form = recibirForma();

		leds_out_write(form);
	}
	
}
/*
static void infra_test(void){

	printf("Test de infra ... se interrumpe con el boton 1\n");

	unsigned int seguidor = 0;

	while(!(buttons_in_read()&1)) {
		seguidor = infrarrojo_infras2_read();
		printf("Infrarrojo: %x \n",seguidor);
		delay_ms(1000);
		}

}*/

static int infrarrojo(void){
   
	unsigned int entrada = infrarrojo_infras2_read();
	unsigned int salida=3;
	
	if((entrada == 0x4)||(entrada == 0x5)||(entrada == 0x6)||(entrada == 0x7)||(entrada == 0xC)||(entrada == 0xD)||(entrada == 0xE)||(entrada == 0xF)||(entrada == 0x14)||(entrada == 0x15)||(entrada == 0x16)||(entrada == 0x17)||(entrada == 0x1C)||(entrada == 0x1D)||(entrada == 0x1E)||(entrada == 0x1F)){
		if ((entrada == 0x7)||(entrada == 0xF)||(entrada == 0x17))
		{
			salida = 2;
			printf("Gire a la izquierda: %x \n",entrada);
		}
		else if ((entrada == 0x1C)||(entrada == 0x1D)||(entrada == 0x1E))
		{
			salida = 1;
			printf("Gire a la derecha: %x \n",entrada);
		}
		else if ((entrada == 0x1F))
		{
			salida = 3;
			printf("Pare: %x \n",entrada);
		}
		else
		{
			salida = 0;
			printf("Siga: %x \n",entrada);
		}
		
	}
	else
	{
		salida = 3;
			printf("Está quieto: %x \n",entrada);
	}
	
	
	
	return salida;

}


static void w_test(void){
	unsigned int state = 3;
	
	while(!(buttons_in_read()&1)){

		state = infrarrojo();
		ruedas_move_write(state);
		delay_ms(1000);
		/*switch(state){
			case 0: 
				ruedas_move_write(0);
				delay_ms(5000);
				state = 1;
				break;
			case 1: 
				ruedas_move_write(1);
				delay_ms(5000);
				state = 2;
				break;
			case 2: 
				ruedas_move_write(2);
				delay_ms(5000);
				state = 3;
				break;
			case 3: 
				ruedas_move_write(3);
				delay_ms(5000);
				state = 4;
				break; 
			case 4: 
				ruedas_move_write(4);
				delay_ms(5000);
				ruedas_move_write(3);
				return;
				break; 

		}*/
	}
}

static void console_service(void)
{
	char *str;
	char *token;

	str = readstr();
	if(str == NULL) return;
	token = get_token(&str);
	if(strcmp(token, "help") == 0)
		help();
	else if(strcmp(token, "reboot") == 0)
		reboot();
	else if(strcmp(token, "led") == 0)
		led_test();
	else if(strcmp(token, "IR") == 0)
		infrarrojo();
	else if(strcmp(token, "w") == 0)
		w_test();
	prompt();
}

int main(void)
{
	irq_setmask(0);
	irq_setie(1);
	uart_init();

	puts("\nSoC - RiscV project UNAL 2020-2-- CPU testing software built "__DATE__" "__TIME__"\n");
	help();
	prompt();

	while(1) {
		console_service();
	}

	return 0;
}

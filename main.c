#include <stdio.h>
#include "pico/stdlib.h"
//#include "boards/pico.h"

int main() {
    setup_default_uart();
    printf("Hello, world!\n");
    cont uint led_pin = 25;

    gpio_init(led_pin);
    gpio_set_dir(led_pin, GPIO_OUT);

    while (true) {
        gpio_put(led_pin, true);
        sleep_ms(500);
        gpio_put(led_pin, true);
        sleep_ms(500);
    }
}
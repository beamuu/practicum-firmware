#include <avr/io.h>
#include <avr/interrupt.h>  /* for sei() */
#include <util/delay.h>     /* for _delay_ms() */
#include <avr/pgmspace.h>   /* required by usbdrv.h */

#include "meg.h"
#include "usbdrv.h"

#define RQ_SET_LED         0
#define RQ_SET_LED_VALUE   1
#define RQ_GET_SWITCH      2
#define RQ_GET_LIGHT       3

#define RQ_GET_REED0       4
#define RQ_GET_REED1       5
#define RQ_GET_REED2       6
#define RQ_GET_REED3       7

#define RQ_BUZZER_ON       8
#define RQ_BUZZER_OFF      9

#define RQ_LED_RED_ON      10
#define RQ_LED_RED_OFF     11

#define RQ_LED_GREEN_ON    12
#define RQ_LED_GREEN_OFF   13

#define RQ_CHECK_CARD      14

/* ------------------------------------------------------------------------- */
/* ----------------------------- USB interface ----------------------------- */
/* ------------------------------------------------------------------------- */
usbMsgLen_t usbFunctionSetup(uint8_t data[8])
{
    usbRequest_t *rq = (void *)data;

    /* declared as static so they stay valid when usbFunctionSetup returns */
    static uint8_t switch_state;  
    static uint16_t light_value;
    static uint8_t reed_id0;
    static uint8_t reed_id1;
    static uint8_t reed_id2;
    static uint8_t reed_id3;
    static uint8_t card;
    if (rq->bRequest == RQ_SET_LED)
    {
        uint8_t led_val = rq->wValue.bytes[0];
        uint8_t led_no  = rq->wIndex.bytes[0];
        //set_led(led_no, led_val);
        return 0;
    }

    else if (rq->bRequest == RQ_SET_LED_VALUE)
    {
        uint8_t led_value = rq->wValue.bytes[0];
        set_led_value(led_value);
        return 0;
    }

    else if (rq->bRequest == RQ_GET_SWITCH)
    {
        //switch_state = SWITCH_PRESSED();

        /* point usbMsgPtr to the data to be returned to host */
        usbMsgPtr = &switch_state;

        /* return the number of bytes of data to be returned to host */
        return 1;
    }

    // else if (rq->bRequest == RQ_GET_)
    // {
    //     light_value = read_adc(PC4);
    //     usbMsgPtr = (uchar*) &light_value;
    //     return sizeof(light_value);
    // }
    else if (rq->bRequest == RQ_GET_REED0) // 4
    {
        reed_id0 = REED0();
        usbMsgPtr = &reed_id0;
        return 1;
    }
    else if (rq->bRequest == RQ_GET_REED1) // 5
    {
        reed_id1 = REED1();
        usbMsgPtr = &reed_id1;
        return 1;
    }
    else if (rq->bRequest == RQ_GET_REED2) // 6
    {
        reed_id2 = REED2();
        usbMsgPtr = &reed_id2;
        return 1;
    }
    else if (rq->bRequest == RQ_GET_REED3) // 7
    {
        reed_id3 = REED3();
        usbMsgPtr = &reed_id3;
        return 1;
    }
    else if (rq->bRequest == RQ_BUZZER_ON) // 8
    {
        buzzer_on();
        return 0;
    }
    else if (rq->bRequest == RQ_BUZZER_OFF) // 9
    {
        buzzer_off();
        return 0;
    }
    else if (rq->bRequest == RQ_LED_RED_ON) // 10
    {
        led_on_red();
        return 0;
    }
    else if (rq->bRequest == RQ_LED_RED_OFF) // 11
    {
        led_off_red();
        return 0;
    }
    else if (rq->bRequest == RQ_LED_GREEN_ON) // 12
    {
        led_on_green();
        return 0;
    }
    else if (rq->bRequest == RQ_LED_GREEN_OFF) // 13
    {
        led_off_green();
        return 0;
    }
    else if (rq->bRequest == RQ_CHECK_CARD) // 14
    {
        card = CARD_CHECK1();
        usbMsgPtr = &card;
        return 1;
    }

    /* default for not implemented requests: return no data back to host */
    return 0;
}

/* ------------------------------------------------------------------------- */
int main(void)
{
    init_peri();
    usbInit();

    /* enforce re-enumeration, do this while interrupts are disabled! */
    usbDeviceDisconnect();
    _delay_ms(300);
    usbDeviceConnect();

    /* enable global interrupts */
    sei();

    /* main event loop */
    for(;;)
    {
        usbPoll();
    }

    return 0;
}

/* ------------------------------------------------------------------------- */

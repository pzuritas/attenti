
char voltmeter_pin = 'A0';
int temperature_pin = 'A7';
int offset = 20; //correction value, may be changed

void setup()
{
    Serial.begin(9600);
}

void loop()
{
    int voltage = analogRead(voltmeter_pin);
    int temperature = analogRead(temperature_pin);
    float kelvin_reading = log(10000.0 * ((1024.0 / temperature - 1)));
    kelvin_reading = 1 / (
        0.001129148 + (
            0.000234125 + (0.0000000876741 * pow(kelvin_reading, 2))
            ) * kelvin_reading
        );
    Serial.print("V,");
    Serial.println(voltage);
    Serial.print("T,");
    Serial.println(kelvin_reading);
    delay(250);
}

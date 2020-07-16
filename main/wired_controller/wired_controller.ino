// wired_controller.ino: Pablo Zurita
// Arduino script to send Attenti data via Serial to computer.
const int GSR=A2;
int sensorValue=0;
int gsr_average=0;
int temp_average = 0;
// PARAMETERS: CHANGE ACCORDING TO TEST
//int voltmeter_pin = 0; // Voltage/CSR pin, parameter
int ThermistorPin = 7; // Thermistor pin
//int offset = 750; // Voltage offest, test first to benchmark
float temp_offset = 47.425; // Temperature offset, test first to benchmark
int serial_port = 9600; // Serial port to access in PC
int period = 833; // Period for data capture in ms. If f is samples per minute, 
                  // then period must be (f / 60000)^(-1).

float R1 = 10000; // Thermistor resistance.
float c1 = 1.009249522e-03, c2 = 2.378405444e-04, c3 = 2.019202697e-07; // Stei-
                //nhart-Hart coefficients.

float v_thermistor;
float logR2, R2, temp;

void setup()
{
    Serial.begin(serial_port);
}

void loop()
{
    //float voltage = analogRead(voltmeter_pin); // Volage measurment
    //voltage -= offset;
    long sumV=0;
    long sumT=0;
    for(int i=0;i<10;i++)           //Average the 10 measurements to remove the glitch
      {
      float voltage = analogRead(GSR);
      sumV += voltage;
      v_thermistor = analogRead(ThermistorPin);
      float R2 = R1 * (1023.0 / (float)v_thermistor - 1.0);
      logR2 = log(R2);
      temp = (1.0 / (c1 + c2*logR2 + c3*logR2*logR2*logR2));
      temp = temp - 273.15;
      temp -= temp_offset;
      sumT += temp;
      }
    gsr_average = sumV/10;
    temp_average = sumT/10;
    Serial.print("V,");
    Serial.println(gsr_average);
    Serial.print("T,");
    Serial.println(temp_average);
    delay(period);
}

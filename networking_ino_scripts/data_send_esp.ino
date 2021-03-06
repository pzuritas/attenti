#include <WiFi.h>

String voltmeter_pin = 'A0';
String temperature_pin = 'A7';
int offset = 110; //correction value, may be changed
float temp_offset = -54.89;

char* ssid = "test";
char* pass = "";

int status = WL_IDLE_STATUS;

char server[] = "hostid";

String postDataOne;
String postDataTwo;
String postVariableOne = "temp=";
String postVariableTwo = "volt=";

WiFiClient client;

void setup()
{
 
    Serial.begin(9600);

    WiFi.begin(ssid, password);

    while (WiFi.status() != WL_CONNECTED)
    {
        delay(500);
        Serial.println("Connecting to WiFi..");
    }

    Serial.println("Connected to the WiFi network");

    Serial.print("SSID: ");
    Serial.println(WiFi.SSID());
    IPAddress ip = WiFi.localIP();
    IPAddress gateway = WiFi.gatewayIP();
    Serial.print("IP Address: ");
    Serial.println(ip);
}

void loop()
{
  float voltage = analogRead(voltmeter_pin);
    voltage -= offset;
  float temperature = analogRead(temperature_pin);
  float kelvin_reading = log(10000.0 * ((1024.0 / temperature - 1)));
    kelvin_reading = 1 / (
        0.001129148 + (
            0.000234125 + (0.0000000876741 * pow(kelvin_reading, 2))
            ) * kelvin_reading
        );
  kelvin_reading -= temp_offset;

  postDataOne = postVariableOne + kelvin_reading;

  if (client.connect(server, 80))
  {
    client.println("POST /test/post.php HTTP/1.1");
    client.println("Host: hostid");
    client.println("Content-Type: text/csv");
    client.print("Content-Length: ");
    client.println(postData.length());
    client.println();
    client.print(postDataOne);
  }

  postDataTwo = postVariableTwo + voltage;

  if (client.connect(server, 80))
  {
    client.println("POST /test/post.php HTTP/1.1");
    client.println("Host: hostid");
    client.println("Content-Type: text/csv");
    client.print("Content-Length: ");
    client.println(postData.length());
    client.println();
    client.print(postDataTwo);
  }

  if (client.connected())
  {
    client.stop();
  }

  Serial.println(postData);

  delay(100);
}

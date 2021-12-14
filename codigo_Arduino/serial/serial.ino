const int led = 13;
const int led1 = 12;
void setup() {
  pinMode(led,OUTPUT);
  pinMode(led1,OUTPUT);
  digitalWrite (led, LOW);
  digitalWrite (led1, LOW);
  Serial.begin(9600);
  Serial.println("Conexion Establecida");
}

void loop() {
  while(Serial.available())
  {
    char str=Serial.read();
    digitalWrite (led, HIGH);
    Serial.println(str);
  }
  digitalWrite (led, LOW);
}

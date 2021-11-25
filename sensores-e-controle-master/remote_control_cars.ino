//Pinos do Driver L298

//Motor direito
int IN1 = 1 ; //Motor direito pra frente
int IN2 = 2 ; //Motor direito ré

//Motor esquerdo
int IN3 = 3 ; //Motor esquerdo pra frente
int IN4 = 4 ; //Motor esquerdo ré

int state_temp;
int vSpeed = 200;   // Define velocidade padrão 0 - 255.
char state;
  
void setup() {
  Serial.begin(9600) ;
  pinMode(IN1,OUTPUT) ;
  pinMode(IN2,OUTPUT) ;
  pinMode(IN3,OUTPUT) ;
  pinMode(IN4,OUTPUT) ;

  digitalWrite(IN1, LOW) ;
  digitalWrite(IN2, LOW) ;
  digitalWrite(IN3, LOW) ;
  digitalWrite(IN4, LOW) ;
    
}

  
void loop() {
  // Variable
  if (Serial.available() > 0) {
    state_temp = Serial.read();
    state = state_temp;
  }

  // Se o estado  recebido for igual a '8', o carro se movimenta para frente.
  if (state == '8') {
    Serial.println("Comando para Frente");
    
    digitalWrite(IN1, HIGH) ;
    digitalWrite(IN2, LOW) ;
    digitalWrite(IN3, HIGH) ;
    digitalWrite(IN4, LOW) ;
    delay(1000);
  }

  // Se o estado recebido for igual a '7', o carro se movimenta para Frente Esquerda.
  else if (state == '7') {  
    Serial.println("Comando para Frente-Esquerda");

    digitalWrite(IN1, HIGH) ;
    digitalWrite(IN4, HIGH) ;
    delay(250) ;

    digitalWrite(IN1, HIGH) ;
    digitalWrite(IN2, LOW) ;
    digitalWrite(IN3, HIGH) ;
    digitalWrite(IN4, LOW) ;      
    delay(1000) ;
  }

  // Se o estado recebido for igual a '9', o carro se movimenta para Frente Direita.
  else if (state == '9') {   
    Serial.println("Comando para Frente-Direita");

    digitalWrite(IN2, HIGH) ;   
    digitalWrite(IN3, HIGH) ;
    delay(250) ;
 
    digitalWrite(IN1, HIGH) ;
    digitalWrite(IN2, LOW) ;
    digitalWrite(IN3, HIGH) ;
    digitalWrite(IN4, LOW) ;
    delay(1000) ;
  }

  // Se o estado recebido for igual a '2', o carro se movimenta para trás.
  else if (state == '2') { 
    Serial.println("Comando para Trás");

    digitalWrite(IN1, LOW) ;
    digitalWrite(IN2, HIGH) ;
    digitalWrite(IN3, LOW) ;
    digitalWrite(IN4, HIGH) ;
    delay(1000) ;
  }

  // Se o estado recebido for igual a '1', o carro se movimenta para Trás Esquerda.
  else if (state == '1') {  
    Serial.println("Comando para Trás-Esquerda");

    digitalWrite(IN1, HIGH) ;
    digitalWrite(IN4, HIGH) ;
    delay(250) ;
     
    digitalWrite(IN1, LOW) ;    
    digitalWrite(IN2, HIGH) ;
    digitalWrite(IN3, LOW) ;
    digitalWrite(IN4, HIGH) ;
    delay(1000) ;
  }

  // Se o estado recebido for igual a '3', o carro se movimenta para Trás Direita.
  else if (state == '3') {  
    Serial.println("Comando para Trás-Direita");

    digitalWrite(IN2, HIGH) ;
    digitalWrite(IN3, HIGH) ;
    delay(250) ;

    digitalWrite(IN1, LOW) ;
    digitalWrite(IN2, HIGH) ;
    digitalWrite(IN3, LOW) ;
    digitalWrite(IN4, HIGH) ;
    delay(1000) ;
  }

  // Se o estado recebido for igual a '4', o carro se movimenta para esquerda.
  else if (state == '4') {   
    Serial.print("Comando para Esquerda");

    digitalWrite(IN1, HIGH) ;
    digitalWrite(IN4, HIGH) ;
    delay(500) ;

    digitalWrite(IN1, HIGH) ;
    digitalWrite(IN2, LOW) ;
    digitalWrite(IN3, HIGH) ;
    digitalWrite(IN4, LOW) ;
    delay(1000) ;
  }

  // Se o estado recebido for igual a '6', o carro se movimenta para direita.
  else if (state == '6') {   
    Serial.println("Comando para Direita");
    
    digitalWrite(IN3, HIGH) ;
    digitalWrite(IN2, HIGH) ;
    delay(500) ;

    digitalWrite(IN1, HIGH) ;
    digitalWrite(IN2, LOW) ;
    digitalWrite(IN3, HIGH) ;
    digitalWrite(IN4, LOW) ;
    delay(1000) ;
  }

  // Se o estado recebido for igual a '5', o carro permanece parado.
  else if (state == '5') {   
    Serial.print("Comando para Parar");
     
    digitalWrite(IN1, LOW) ;
    digitalWrite(IN2, LOW) ;
    digitalWrite(IN3, LOW) ;
    digitalWrite(IN4, LOW) ;    
  }
}

/*
   ctrl_debitmetre.ino
   Auteur: Émile Jetzer
   Date: 2021-01-07

   Lecture de la valeur du débitmètre, et envoi sur la ligne série.
*/

// Inclusions
#define BROCHE 2 // La broche 2 permet les interruptions[^2]

// Variables globales
volatile long unsigned int nombre_de_tours = 0; // Nombre de tours dans les derniers delai ms
unsigned int delai = 1000; // [ms] Délai entre les calculs de débit
float debit = 0; // [Hz]
long unsigned int derniere_mesure = 0; // [ms] Moment de la dernière mesure

void setup() {
  // Intialiser la communication série
  Serial.begin(9600); // Bas débit pour permettre la gestion des interruptions.

  // Initialiser les broches de lecture
  pinMode(13, INPUT);

  // Configurer l'interruption[^2]
  attachInterrupt(digitalPinToInterrupt(BROCHE), interruption, RISING);

  // Attente pour la communication série...
  while (!Serial) {
    ;
  }

  // Annonce des colonnes
  Serial.println("t[s] f[Hz]");
}

void loop() {
  // Est-ce qu'il y a une demande d'information?
  if (Serial.available()) {
    detachInterrupt(digitalPinToInterrupt(BROCHE));
    String commande = Serial.readStringUntil('\n'); // [^1]
    Serial.println(commande);

    if (commande == "lire") {
      float heure = (float)derniere_mesure / 1000.0; // [s]
      Serial.println(String(heure) + " " + String(debit));
    }
    attachInterrupt(digitalPinToInterrupt(BROCHE), interruption, RISING);
  }

  // Mise à jour des lectures
  if ( (millis() - derniere_mesure) >= delai ) {
    debit = 1000.0 * (float)nombre_de_tours / (float)delai; // [Hz]
    nombre_de_tours = 0;
    derniere_mesure = millis();
  }
}

void interruption(void) {
  // Ajout d'un tour
  nombre_de_tours++;
}

/*
   [^1]: https://www.arduino.cc/reference/en/language/functions/communication/serial/readstringuntil/
   [^2]: https://www.arduino.cc/reference/en/language/functions/external-interrupts/attachinterrupt/
*/

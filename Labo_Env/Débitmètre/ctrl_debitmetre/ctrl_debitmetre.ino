/*
   ctrl_debitmetre.ino
   Auteur: Émile Jetzer
   Date: 2021-01-07

   Lecture de la valeur du débitmètre, et envoi sur la ligne série.
*/

// Inclusions
#define BROCHE 2 // La broche 2 permet les interruptions[^2] sur Arduino Due, Mega & micro
#define ENVOI_AUTOMATIQUE true // Permet de régler l'envoi automatique des données à un intervalle.
#define SECONDE 1000.0 // [ms/s] Facteur de conversion en secondes
#define MINUTE 60.0 // [s/min] Facteur de conversion en minutes
#define FACTEUR_DEBIT 98.0 // [Hz*min/L] Facteur dans la spécification du débitmètre[^3]
#define DELAI_MESURE 1000u // [ms] Délai entre les calculs de débit
#define DELAI_COM 2000u // [ms] Délai minimal entre les communications

// Variables globales
volatile uint32_t nombre_de_tours = 0; // Nombre de tours dans les derniers delai ms
uint32_t derniere_mesure, derniere_com; // [ms] Moment de la dernière mesure ou communication

void setup() {
  // Intialiser la communication série
  Serial.begin(9600); // Bas débit pour permettre la gestion des interruptions.
  pinMode(BROCHE, INPUT); // Initialiser les broches de lecture
  attachInterrupt(digitalPinToInterrupt(BROCHE), isr, RISING); // Interruption[^2]
  while (!Serial) {;} // Attente pour la communication série...
  Serial.println("t[min] f[Hz] Q[L/min]"); // Annonce des colonnes
}

void loop() {
  // On vérifie périodiquement si on a une demande de communication,
  // mais pas trop souvent: ça interfère avec l'exécution des interruptions.
  if ( (millis() - derniere_com) >= DELAI_COM ) {
    if (Serial.available()) { // Est-ce qu'il y a une demande d'information?
      detachInterrupt(digitalPinToInterrupt(BROCHE));
      
      String commande = Serial.readStringUntil('\n'); // [^1]
      exec_com(commande);
      
      attachInterrupt(digitalPinToInterrupt(BROCHE), isr, RISING);
    } else if (ENVOI_AUTOMATIQUE) {
      detachInterrupt(digitalPinToInterrupt(BROCHE));
      exec_com("lire");
      attachInterrupt(digitalPinToInterrupt(BROCHE), isr, RISING);
    }
  }

  // Mise à jour des lectures
  if ( (millis() - derniere_mesure) >= DELAI_MESURE ) {
    nombre_de_tours = 0;
    derniere_mesure = millis();
  }
}

void isr(void) {
  // Ajout d'un tour
  nombre_de_tours++;
}

void exec_com(String commande) {
  if (commande == "lire") {
    float heure = millis() / SECONDE / MINUTE; // [s]
    float freq = SECONDE * nombre_de_tours / DELAI_MESURE; //[Hz] 
    float debit = SECONDE * nombre_de_tours / DELAI_MESURE / FACTEUR_DEBIT; // [L/min]
    Serial.println(String(heure) + " " + String(freq) + " " + String(debit));
    derniere_com = millis();
  }
}

/*
   [^1]: https://www.arduino.cc/reference/en/language/functions/communication/serial/readstringuntil/
   [^2]: https://www.arduino.cc/reference/en/language/functions/external-interrupts/attachinterrupt/
   [^3]: https://digiten.shop/collections/counter/products/digiten-0-3-6l-min-g1-4-water-coffee-flow-hall-sensor-switch-meter-flowmeter-counter-connect-hose
*/

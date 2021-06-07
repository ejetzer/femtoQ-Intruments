/*
 * Visualisation du signal du débitmètre
 * Auteur: Émile Jetzer
 * Date: 2020-01-08
 * 
 * Visualisation du signal du débitmètre
 */
// Inclusions
#define BROCHE A0

void setup() {
  // Intialiser la communication série
  Serial.begin(9600); // Bas débit pour permettre la gestion des interruptions.
  pinMode(BROCHE, INPUT); // Initialiser les broches de lecture
  while (!Serial) {;} // Attente pour la communication série...
  Serial.println("V[bit]"); // Annonce des colonnes
}

void loop() {
  Serial.println(analogRead(BROCHE));
}

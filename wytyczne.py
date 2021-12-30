# Założenia
# Implementacja testu -> Implementacja funkcjonalności
# Kalkulator to klasa, która kontroluje: Walidację danych wejściowych, Operacje arytmetyczne i logiczne, Dostarczanie wyników operacji.

# Testy inicjacji klasy
# 1) Test tworzenia obiektu klasy kalkulator. Sprawdzenie czy można utworzyć obiekt klasy przy pomocy konstruktora bezparametrowego.
# 2) Test wartości domyślnej kalkulatora. Sprawdzenie czy metoda zwracająca bieżącą wartość kalkulatora zwraca wartość ”0”.
# 3) Test domyślnego systemu prezentacji danych. Sprawdzenie czy metoda zwracająca bieżący system prezentacji danych zwraca wartość ”dec”.
# 4) Test domyślnego typu danych. Sprawdzenie czy metoda zwracająca bieżący typ danych zwraca wartość ”qword”.
# 5) Test domyślnej wartości pól binarnych. Sprawdzenie czy metoda zwracająca bieżącą wartość pól binarnych zwraca tablicę 64 pól o wartości ”0” .

# Testy wprowadzania znaków
# Test wprowadzania znaków w systemie binarnym
# 1) Testy czy metoda do wprowadzania danych przyjmuje znak ”1”-> {q1, 1ww, 11 w1e1}
# 2) Testy czy metoda do wprowadzania danych przyjmuje znak ”0”
# 3) Testy czy metoda do wprowadzania danych przyjmuje znak ”+”
# 4) Testy czy metoda do wprowadzania danych przyjmuje znak ”-”
# 4) Testy czy metoda do wprowadzania danych przyjmuje znak ”*”
# 4) Testy czy metoda do wprowadzania danych przyjmuje znak ”/”
# 4) Testy czy metoda do wprowadzania danych przyjmuje znak ”!”
# 5) …Reszta akceptowanych znaków….
# 6) Testy czy metoda do wprowadzania danych ignoruje pozostałe znaki {12 -> char}

# Test wprowadzania znaków w systemie ósemkowym
# 1) Test czy metoda do wprowadzania danych przyjmuje znak ”1”
# 2) Test czy metoda do wprowadzania danych przyjmuje znak ”0”
# 3) …Reszta akceptowanych znaków numerycznych….
# 1) Test czy metoda do wprowadzania danych przyjmuje znak ”*”
# 1) Test czy metoda do wprowadzania danych przyjmuje znak ”/”
# 4) Testy czy metoda do wprowadzania danych przyjmuje znak ”+”
# 5) Testy czy metoda do wprowadzania danych przyjmuje znak ”-”
# 6) …Reszta akceptowanych znaków….
# 7) Testy czy metoda do wprowadzania danych ignoruje pozostałe znaki

# Test wprowadzania znaków w systemie ….
# 1) Implementacja pozostałych grup testowych dec hex

# Testy wprowadzania wartości
# Test wprowadzania wartości dla typu bajt
# 1) Testy czy metoda do wprowadzania danych przyjmuje wartości z zakresu - 128 < -> 127
# 2) Testy czy metoda do wprowadzania danych kończy przyjmowanie znaków po osiągnięciu wartości określonej zakresem. ”-129” -> ”12”, ”291” -> ”29”
# 3) Testy czy metoda do wprowadzania danych przyjmuje znaki operatorów po osiągnięciu wartości określonej zakresem(+ -= *)

# 4)zmienić testy inputu dla binarnych to match rest


# Test wprowadzania wartości dla typu word ….
# 1) ….

# Testy rzutowania wartości między systemami prezentacji danych
# Testy rzutowania wartości z systemu binarnego na pozostałe
# 1) Test rzutowania wartości z systemu binarnego na system dziesiętny
# 2) …

# Testy rzutowania wartości między typami danych
# Testy rzutowania wartości z bajt na word
# 1) Testy propagacji bitu znaku dla wartości dodatnich
# 2) Testy propagacji bitu znaku dla wartości ujemnych

Testy rzutowania wartości z word na bajt
1) Testy pozostawienia informacji z ośmiu bitów
2) Testy utraty informacji z bitów powyżej ośmiu

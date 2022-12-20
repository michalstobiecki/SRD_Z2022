## Zasady konkursu SRD
### Zespoły
Należy dobrać się w zespoły złożone z:
* Grupa 11 (15:20 - 16:50) - 1-3 osób,
* Grupa 13 (17:10 - 18:40)- 1-3 osób,
* Grupa 15 (19:00 - 20:30)- 1-2 osoby. 

Proszę nazwać zespół (nazwa pojawi się w tabeli z wynikami). Proszę nie używać danych osobowych w nazwach. 

### Zbiór danych i cel konkursu
Celem konkursu jest uzyskanie jak największego **accuracy** (procent poprawnie zaklasyfikowanych obserwacji [TP+TN/(TP+TN+FP+FN)]) w klasyfikacji zmiennej celu **IsIPA**. Do stworzenia modelu proszę wykorzystać zbiór danych **IPA.csv**, natomiast finalną predykcję należy wykonać na zbiorze **IPA_test.csv**. Opis zbioru znajduje się w pliku **IPA_description.txt**.

### Wyniki
Wyniki należy przesłać na adres **lkrain@sgh.waw.pl** do końca zajęć danej grupy. W treści maila należy podać nazwę grupy oraz imiona i nazwiska członków - wystarczy mail od jednego członka grupy. Jako załączniki należy zamieścić:
1. Skrypt R/Python/Julia ze wykorzystanym kodem
2. Plik CSV o nazwie **[nazwa_grupy]_IPA_prediction.csv** zawierający jedną kolumnę z 5000 predykcjami dla kolejnych wierszy ze zbioru testowego **IPA_test.csv**. Nagłówek jest opcjonalny, predykcje powinny przyjmować wartości 1/0 lub TRUE/FALSE.

Proszę dokładnie sprawdzić czy kolejność predykcji zgadza się z kolejnością obserwacji w zbiorze testowym.

Tabela z rankingiem zespołów pojawi się na GitHubie w poniższym pliku README. Najlepszy zespół w każdej grupie zajęciowej otrzyma dodatkowe 5 punktów, kolejny 4 punkty, itd.

Życzę powodzenia. 

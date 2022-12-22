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

### Wyniki konkursu

Grupa 11
| **Zespół**     | **Accuracy** | **Punkty** | **Język** | **Model**                  |
|----------------|--------------|------------|-----------|----------------------------|
| XDBoost        | 87,36        | 5          | Python    | XGBoost                    |
| WKS            | 86,9         | 4          | Python    | XGBoost                    |
| MMMM           | 86,64        | 3          | Python    | GradientBoostingClassifier |
| Ankara Messi   | 86,58        | 2          | Python    | RandomForestClassifier     |
| Ostatnia Grupa | 86,16        | 1          | Python    | DecisionTreeClassifier     |
| MAK            | 83,62        | 0          | Python    | LogisticRegression         |

Grupa 13
| **Zespół** | **Accuracy** | **Punkty** | **Język** | **Model**                      |
|------------|--------------|------------|-----------|--------------------------------|
| Leo Miesi  | 86,94        | 5          | Python    | HistGradientBoostingClassifier |
| ACA        | 86,94        | 5          | Python    | XGBoost                        |
| Trojaczki  | 86,92        | 4          | Python    | XGBoost                        |
| AJJ        | 86,88        | 3          | Python    | XGBoost                        |
| m_kwadrat  | 86,44        | 2          | Python    | GradientBoostingRegressor      |
| Kobra      | 86,15        | 1          | Python    | DecisionTreeClassifier         |
| Kh7        | 85,84        | 0          | Python    | XGBoost                        |

Grupa 15
| **Zespół**                                           | **Accuracy** | **Punkty** | **Język** | **Model**                  |
|------------------------------------------------------|--------------|------------|-----------|----------------------------|
| MLWizards                                            | 87,06        | 5          | Python    | LGBMClassifier             |
| Decision Trees Or The Unexpected Virtue Of Ignorance | 86,18        | 4          | Python    | DecisionTreeRegressor      |
| Konwektor                                            | 85,82        | 3          | Python    | DecisionTreeRegressor      |
| SRD Super Przedmiot                                  | 85,57        | 2          | Python    | GradientBoostingClassifier |
| Pacjoh                                               | 85,08        | 1          | Python    | SVC                        |

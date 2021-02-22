# Funkcje aplikacji:
# Możliwość założenia swojego profilu (ok)
# Liczenie czasu spędzonego przy komputerze, od momentu wlaczenia aplikacji, po zakonczeniu czas jest zapisywany, a licznik resetowany (ok)
# Możliwość tworzenia notatek (ok)
# Możliwość tworzenia tasków (w jakim celu siadało się do komputera, czy udało się go osiągnąć, ile czasu spędziło się przy każdym z zadań) (Zuzia musi dopracowac
# koncepcje notatek)
# Możliwość określenia nastroju przed korzystaniem z komputera, określenie nastroju po i podanie powodu (ok)
# Przypomnienia (czas spędzony przy komputerze, ćwiczenia fizyczne, patrzenie w dal, mruganie, picie, korzystanie z toalety, spacer, rozciąganie się)
# Możliwość wybrania poziomu restrykcji (każdy posiada swoją postać i dostosowaną kolorystycznie skórkę) (ok)

import datetime
import time


class User:

    def __init__(self):
        pass

    def create_user_profile(self):
        """Funckcja odpowiedzialna za tworzenie nowego uzytkownika."""
        pass

    def delete_user_profile(self):
        """Funkcja odpowiedzialna za usuwanie profilu uzytkownika."""
        pass

    def edit_user_profile(self):
        """Funkcja odpowiedzialna za edycje profilu uzytkownika."""
        pass


class Timer:

    def __init__(self):
        pass

    def start_timer(self):
        """Funkcja odpowiedzialna za rozpoczecie liczenia czasu od momentu uruchomienia aplikacji."""
        start_time = time.time()
        return start_time

    def stop_timer(self):
        """Funkcja odpowiedzialna za zakonczenie liczenia czasu do momentu zamkniecia aplikacji."""
        stop_time = time.time()
        return stop_time

    def save_timer_data(self, name, time_spent):
        """Funkcja odpowiedzialna za zapisanie calkowitego czasu uzytkowania aplikacji do pliku (bazy)."""
        timestamp = str(datetime.datetime.now().isoformat()).replace("T", " ")[:19]
        file = open('timer.txt', 'a')
        file.write(f'[+] {timestamp} [+] Uzytkownik {name} spedzil przed komputerem {time_spent}.\n')
        file.close()


class Notes:

    def __init__(self):
        pass

    def create_new_note(self):
        """Funkcja odpowiedzialna za tworzenie nowych notatek."""
        pass

    def delete_new_note(self):
        """Funkcja odpowiedzialna za kasowanie istniejacych notatek."""
        pass

    def edit_note(self):
        """Funkcja odpowiedzialna za edytowanie istniejacych notatek."""
        pass

    def save_note(self):
        """Funkcja odpowiedzialna za zapisywanie notatek."""
        pass


class Mood:

    def __init__(self):
        pass

    def initial_mood_status(self):
        """Funkcja odpowiedzialna za okreslenie nastroju uzytkownika przed korzystaniem z komputera."""
        pass

    def final_mood_status(self):
        """Funkcja odpowiedzialna za okreslenie nastroju uzytkownika po korzystaniu z komputera."""
        pass

    def user_mood_reason(self):
        """Funkcja odpowiedzialna za opisanie nastroju uzytkownika po korzystaniu z komputera."""


class Notifications:

    def __init__(self):
        pass

    def create_notification(self):
        """Funkcja odpowiedzialna za pojawienie sie okienka notyfikacji z odpowiednia informacja."""
        pass


class Restrictions:

    def __init__(self):
        pass

    def light_restriction(self):
        """Funkcja odpowiedzialna za leniwego ludzika."""
        pass

    def medium_restrictions(self):
        """Funkcja odpowiedzialna za srednio leniwego ludzika."""
        pass

    def hard_restrictions(self):
        """Funkcja odpowiedzialna za ludzika bezkompromisowego."""
        pass


if __name__ == '__main__':
    timer = Timer()
    t1 = timer.start_timer()
    time.sleep(5)
    t2 = timer.stop_timer()
    timer.save_timer_data('Krzysio Ibisz', t2-t1)

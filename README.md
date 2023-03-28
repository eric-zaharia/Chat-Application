Am implementat un server de chat si un client.
In fisierul server.py am definit o clasa Client cu metodele init, str si run(pentru a o putea apela in contextul altui
thread). In run primim datele de la client daca exista, printam in terminal mesajul si facem broadcast celorlalti clienti.
Daca nu exista datele, inchidem socket-ul si eliminam clientul din conexiunile active. Cream un thread pentru fiecare
client.

In client.py avem metoda receive care ruleaza pe un thread si interfata grafica care ruleaza pe thread-ul main. Am un
buton de quit care face sigkill pe client. Item-urile de gui care se actualizeaza folosesc metoda mainloop din tkinter.

Am realizat un fel de "protocol" de trimitere a datelor, facand padding pe tot ce se trimite ca sa nu trebuiasca sa
trimitem si alte informatii precum marimea mesajului si sa stim exact cat primim dintr-o parte in alta.

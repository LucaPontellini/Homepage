# 📌 Tabella comandi Git

| Comando               | Sintassi                                | Funzione |
|-----------------------|-----------------------------------------|----------|
| **add**               | `git add <file>`                        | Aggiunge un singolo file all’area di staging |
|                       | `git add <dir>/`                        | Aggiunge tutti i file di una cartella |
|                       | `git add .`                             | Aggiunge tutti i file della directory corrente e sottocartelle |
|                       | `git add -A`                            | Aggiunge tutte le modifiche (nuovi, modificati, rimossi) |
| **commit**            | `git commit -m "msg"`                   | Registra le modifiche nello storico |
| **branch**            | `git branch`                            | Elenca i branch locali |
|                       | `git branch <nome>`                     | Crea un nuovo branch (non ci sposta) |
| **branch -v**         | `git branch -v`                         | Elenco branch con ultimo commit |
| **checkout**          | `git checkout <nome>`                   | Passa a un branch esistente |
| **checkout -b**       | `git checkout -b <nome>`                | Crea e passa a un nuovo branch |
| **merge**             | `git merge <nome>`                      | Unisce un branch nel corrente |
| **push**              | `git push origin <nome>`                | Invia i commit al remoto |
| **fetch**             | `git fetch`                             | Scarica aggiornamenti dal remoto senza integrarli |
| **clone**             | `git clone <url>`                       | Clona un repository remoto |
| **pull**              | `git pull`                              | Scarica e integra aggiornamenti dal remoto |
| **reset**             | `git reset --hard <commit>`             | Riporta il repo a uno stato precedente |
| **log**               | `git log`                               | Mostra la cronologia dei commit |
| **diff**              | `git diff`                              | Mostra differenze tra versioni |
| **rm**                | `git rm <file>`                         | Rimuove file dal repo e dal disco |
| **rm --cached**       | `git rm --cached <file>`                | Rimuove file dal repo ma lo lascia sul disco |
| **remote add origin** | `git remote add origin <url>`           | Collega repo locale a remoto |
| **remote -v**         | `git remote -v`                         | Mostra i remoti configurati |
| **branch --set-upstream-to** | `git branch --set-upstream-to=origin/main` | Imposta branch remoto di riferimento |
| **revert**            | `git revert <commit>`                   | Annulla un commit creando un nuovo commit inverso |
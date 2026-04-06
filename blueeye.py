import subprocess
import os
import logo

os.system("clear")
logo.print_cyberday()
button = input("Press any button to start!:   ")
if button:
    os.system("clear")
    print("""
The scanning started...
Please wait: 
            """)

    open('devices.txt', 'w').close()

    while True:
        try:
            result = subprocess.run(["hcitool", "scan"], capture_output=True, text=True, check=True)
            lines = result.stdout.strip().split("\n")

            if lines:
                del lines[0]  # Suppression de la première ligne qui est l'en-tête

                with open("devices.txt", "r") as f:
                    devices_exists = f.read().splitlines()

                with open("devices.txt", "a") as f:
                    for ligne in lines:
                        if ligne not in devices_exists:
                            f.write(ligne + "\n")

            os.system('clear')
            catt = subprocess.run(["cat", "-n", "devices.txt"], capture_output=True, text=True, check=True)
            ligne_fichier = catt.stdout.splitlines()

            index = int(subprocess.run("cat devices.txt | wc -l", shell=True, capture_output=True, text=True,
                                       check=True).stdout.strip())
            mac_array = []
            for l_file in ligne_fichier:
                info = l_file.split()
                index=info[0]
                mac = info[1]
                name= ''.join(info[2])

                if name != "n/a":
                    print(index, "\t mac: ", mac, "\t name:", name)
                    mac_array.append(mac)
        except subprocess.CalledProcessError as e:
            print(f"Erreur lors de l'exécution de la commande : {e}")
        except KeyboardInterrupt:
            print("""
            See you soon buddy!
            """)
            exit()
else:
    print("Aborted!!!")

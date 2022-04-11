mdp =input("Entrer un mot de passe (min 8 caracteres) ")
mdp_trop_court = "votre mot de passe est trop court"
while True:
    break
    if len(mdp) == 0 :
        print(mdp_trop_court.upper())
    elif len(mdp) < 8:
        print(mdp_trop_court.capitalize())
    elif mdp.isdigit() :
        print("Votre mot de passe ne contient que des nombres")
    else:
        print("Inscription terminee") 